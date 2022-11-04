import os
import numpy as np
from datetime import datetime

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt



from functools import partial


class Wafer(QMainWindow):
    def __init__(self,wafer_parameters):
        # QMainWindow.__init__(self)
        # wafer parameters, array with 15 parameters
        self.wafer_error = False
        self.waferwindow = ""
        self.wafer_parameters = wafer_parameters
        try:
            if len(wafer_parameters)>=13:
                self.wafer_name = wafer_parameters["wafer_name"]
                self.wafer_size_inch = float(wafer_parameters["wafer_size"])
                self.wafer_size_mm = 0
                self.thickness = 0
                self.set_wafer_size()
                self.xsize = float(wafer_parameters["xsize"])
                self.ysize = float(wafer_parameters["ysize"])

                # xmax & ymax optionals
                if "xmax" in wafer_parameters:
                    self.xmax = int(wafer_parameters["xmax"])
                else:
                    self.xmax = 0

                if "ymax" in wafer_parameters:
                    self.ymax = int(wafer_parameters["ymax"])
                else:
                    self.ymax = 0
                

                self.ymax = 0
                self.nchips = int(wafer_parameters["nchips"])
                self.nmodules = int(wafer_parameters["nmodules"])
                self.origin_chip = wafer_parameters["origin_chip"]
                self.home_chip = wafer_parameters["home_chip"]
                self.flat_orientation = int(wafer_parameters["flat_orientation"])
                self.wafer_positions = wafer_parameters["wafer_positions"]
                self.wafer_modules = wafer_parameters["wafer_modules"]
                self.real_origin_chip = wafer_parameters["real_origin_chip"]
                self.navigation_options = wafer_parameters["navigation_options"]

            else:
                self.wafer_parameters = ""
                self.wafer_error = True
                self.wafer_message = "Problem with ppg parameters"
                # retval = messageBox(self,"Problem with ppg parameters","Wafer file not initialized","error")

        except:
            self.wafer_parameters = ""
            self.wafer_error = True
            self.wafer_message = "Problem initializing class Wafer"
            # retval = messageBox(self,"Problem initializing class Wafer","Wafer file not initialized","error")

    def set_wafer_size(self):
        wafer_size_inch = int(self.wafer_size_inch)
        if wafer_size_inch==1:
            self.wafer_size_mm = 25
            self.thickness = 1
        if wafer_size_inch==2:
            self.wafer_size_mm = 51
            self.thickness = 275
        if wafer_size_inch==3:
            self.wafer_size_mm = 76
            self.thickness = 375
        if wafer_size_inch==4:
            self.wafer_size_mm = 100
            self.thickness = 525
        if wafer_size_inch==5: # 4.9 inch
            self.wafer_size_mm = 125
            self.thickness = 625
        if wafer_size_inch==6: # 5.9 inch
            self.wafer_size_mm = 150
            self.thickness = 675
        if wafer_size_inch==8: # 7.9 inch
            self.wafer_size_mm = 200
            self.thickness = 725
        if wafer_size_inch==12: # 11.8 inch
            self.wafer_size_mm = 300 
            self.thickness = 775
                
        

    def check_wafer_parameters(self):
        check_wafer_parameters = True
        # check wafer_positions & nchips
        if len(self.wafer_positions)!=int(self.nchips):
            check_wafer_parameters = False
            print("Error checking number of chips (" + str(self.nchips) + ") <> wafer_positions size ( " + str(len(self.wafer_positions)) + ")")
        # check wafer_size
        if self.wafer_size_mm==0 or self.thickness==0:
            check_wafer_parameters = False
            print("Error checking wafer_size_mm and wafer thickness...")
        # check xsize and ysize
        wafer_size_um = float(self.wafer_size_mm*1000)
        if wafer_size_um<self.xsize or wafer_size_um<self.ysize:
            check_wafer_parameters = False
            print("Error checking xsize & ysize...")
        # check home chip (is possible home chip not in wafer_position to measure)
        # if self.home_chip not in self.wafer_positions:
        #     check_wafer_parameters = False
        #     print("Error checking home chip...")
        # check origin chip 
        if self.origin_chip not in self.wafer_positions:
            check_wafer_parameters = False
            print("Error checking origin chip...")
        # check flat orientation
        flat_orientation_array = [0,90,180,270]
        if self.flat_orientation not in flat_orientation_array:
            check_wafer_parameters = False
            print("Error checking flat orientation...")
        # set xmax & ymax
        if check_wafer_parameters:
            xmax_detected = 0
            ymax_detected = 0
            elementos_x_detected = []
            elementos_y_detected = []
            for elemento in self.wafer_positions:
                elemento_array = elemento.split()
                if len(elemento_array)!=2:
                    check_wafer_parameters = False
                    break
                # init variables
                elemento_x = elemento_array[0]
                elemento_y = elemento_array[1]
                buscar_x = False
                buscar_y = False
                num_elemento_x = 0
                num_elemento_y = 0
                if elemento_x not in elementos_x_detected:
                    elementos_x_detected = np.append(elementos_x_detected, elemento_x)
                    buscar_x = True
                if elemento_y not in elementos_y_detected:
                    elementos_y_detected = np.append(elementos_y_detected, elemento_y)
                    buscar_y = True
                if buscar_x and buscar_y:
                    for elemento_buscar in self.wafer_positions:
                        elemento_buscar_array = elemento_buscar.split()
                        if elemento_buscar_array[0] == elemento_x:
                            num_elemento_y += 1 # cambiamos el eje porque buscamos sumatorio en vertical
                        if elemento_buscar_array[1] == elemento_y:
                            num_elemento_x += 1 # cambiamos el eje porque buscamos sumatorio en horizontal

                    if num_elemento_x>xmax_detected:
                        xmax_detected = num_elemento_x
                    if num_elemento_y>ymax_detected:
                        ymax_detected = num_elemento_y

            # if xmax or ymax not initialized then equal to detected
            if self.xmax==0:
                self.xmax = xmax_detected
            if self.ymax==0:
                self.ymax = ymax_detected

            if xmax_detected!=self.xmax and ymax_detected!=self.ymax:
                check_wafer_parameters = False
                print("Error checking xmax (" + str(xmax_detected) + ") & ymax (" + str(ymax_detected) + ")...")

        # check navigation options
        if len(self.navigation_options)!=3:
            check_wafer_parameters = False
            print("Error checking navigation options, not all parameters passed!")
        else:
            # verify parameters
            starting_location = self.navigation_options[0]
            if not starting_location in ["UPPER-LEFT","UPPER-RIGHT","BOTTOM-LEFT","BOTTOM-RIGHT"]:
                check_wafer_parameters = False
                print("Error checking navigation options (starting location). " + starting_location + " not allowed value!")   
            else :
                direction_movement = self.navigation_options[1]
                if not direction_movement in ["BI-DIRECTIONAL","UNI-DIRECTIONAL"]:
                    check_wafer_parameters = False
                    print("Error checking navigation options (directional movement). " + direction_movement + " not allowed value!")   
                else :
                    move_by = self.navigation_options[2]
                    if not move_by in ["ROW","COLUMN"]:
                        check_wafer_parameters = False
                        print("Error checking navigation options (move by). " + move_by + " not allowed value!")   
        
        # verifiy wafer_position according to navigation_options
        

        return check_wafer_parameters

    def calculate_real_coordinate(self, from_coordinate):   #En funció de la coordenada, diu la dif. respecte al origin chip
        to_coordinate=self.real_origin_chip
        from_array = from_coordinate.split()
        to_array = to_coordinate.split()
        X_from = int(from_array[0])
        Y_from = int(from_array[1])
        X_to = int(to_array[0])
        Y_to = int(to_array[1])
        movement_X = (X_to+X_from) # change sign axis X
        movement_Y = (Y_from+Y_to) # same sign axis Y
        # adjust flat orientation
        if self.flat_orientation!=0:
            if self.flat_orientation==180:
                movement_X = movement_X*-1
                movement_Y = movement_Y*-1
            else:
                if self.flat_orientation==90:
                    movement_X, movement_Y = movement_Y, movement_X*-1
                else:
                    if self.flat_orientation==270:
                        movement_X, movement_Y = movement_Y*-1, movement_X
                        
        
        return str(movement_X) + " " + str(movement_Y)

    def calculate_prober_movement(self,from_coordinate,to_coordinate,coordinates=True):
        # return X & Y movement
        # get coordinates X & Y
        if coordinates:
            from_array = from_coordinate.split()
            to_array = to_coordinate.split()
            X_from = int(from_array[0])
            Y_from = int(from_array[1])
            X_to = int(to_array[0])
            Y_to = int(to_array[1])
            # calculate movement in um & change signs
            movement_X = (X_to-X_from)*self.xsize # change sign axis X
            movement_Y = (Y_from-Y_to)*self.ysize # same sign axis Y
        else:
            movement_X = from_coordinate
            movement_Y = to_coordinate

        # adjust flat orientation
        if self.flat_orientation!=0:
            if self.flat_orientation==180:
                movement_X = movement_X*-1
                movement_Y = movement_Y*-1
            else:
                if self.flat_orientation==90:
                    movement_X, movement_Y = movement_Y, movement_X*-1
                else:
                    if self.flat_orientation==270:
                        movement_X, movement_Y = movement_Y*-1, movement_X
                        
        
        return [movement_X,movement_Y]

    def calculate_init_prober_movement(self):
        if self.home_chip!=self.origin_chip:
            return self.calculate_prober_movement(self.home_chip,self.origin_chip)
        return [0,0]

    def calculate_process_percentage(self,die,module):
        nchips = self.nchips
        nmodules = self.nmodules
        total = nchips * nmodules
        calc = int(die)*int(module)/int(total) * 100
        percentage = "{:.2f}".format(calc)
        return float(percentage)

    def calculate_finish_time(self,date_init,die,module):
        date_now = datetime.now()
        difference = date_now-date_init
        nchips = self.nchips
        nmodules = self.nmodules
        total = nchips * nmodules
        total_seconds = difference * int(total) /(((int(die)-1) * int(nmodules)) + int(module))
        finish_time = date_init + total_seconds
        return finish_time.strftime('%Y-%m-%d %H:%M:%S')


    def is_home(self,x,y):
        # pass x,y position
        if self.real_origin_chip!="" and self.home_chip!="":
            real_origin_chipX , real_origin_chipY = self.real_origin_chip.split()
            home_chipX , home_chipY = self.home_chip.split()
            if int(x)*-1 - int(real_origin_chipX) == int(home_chipX) and int(y)*-1 - int(real_origin_chipY) == int(home_chipY):
                return True
        return False

    def is_origin(self,x,y):
        # pass x,y position
        if self.real_origin_chip!="":
            real_origin_chipX , real_origin_chipY = self.real_origin_chip.split()
            origin_chipX , origin_chipY = self.origin_chip.split()
            if int(x)*-1 - int(real_origin_chipX) == int(origin_chipX) and int(y)*-1 - int(real_origin_chipY) == int(origin_chipY):
                return True
        return False

    def is_in(self,x,y):
        # (x-a)² + (y-b)² = R²
        # miramos si los 4 puntos estan dentro 
        is_in = True
        R = self.wafer_size_mm/2
        xstep = self.xsize/1000
        ystep = self.ysize/1000
        a1 = int(abs(x))*xstep
        b1 = int(abs(y))*ystep
        a = { 1:a1, 2:a1+xstep, 3:a1, 4:a1+xstep}
        b = { 1:b1, 2:b1, 3:b1+ystep, 4:b1+ystep}
        for i in range(1,5):
            if pow(R-a[i],2)+pow(R-b[i],2)>pow(R,2):
                # is out
                is_in = False
                break

        return is_in

    def is_to_measure(self,x,y):
        is_to_measure = False
        if len(self.wafer_positions)>0:
            if self.real_origin_chip!="":
                real_origin_chipX , real_origin_chipY = self.real_origin_chip.split()
                realX = -int(x) - int(real_origin_chipX)
                realY = -int(y) - int(real_origin_chipY)
                realpos = str(realX) + " " + str(realY)
                if realpos in self.wafer_positions:
                    is_to_measure = True
        return is_to_measure

    def save_wafermap(self):

        dir_wafermaps = os.getcwd() + base_dir + wafermaps_dir + "/"
        nameFile, _ = QFileDialog.getSaveFileName(self, 'Save wafermap', dir_wafermaps,"Wafermaps (*.py)")
        # and then you need to adjust wafer_parameters
        texto = 'global wafer_parameters\n\
\n\
\n\
# Configuration wafer parameters\n\
wafer_name = "' + self.wafer_name + '"\n\
wafer_size = ' + str(self.wafer_size_inch) + '\n\
xsize = ' + str(self.xsize) + '\n\
ysize = ' + str(self.ysize) + '\n\
nchips = ' + str(self.nchips) + '\n\
nmodules = ' + str(self.nmodules) + '\n\
\n\
real_origin_chip = "' + str(self.real_origin_chip) + '"\n\
origin_chip = "' + str(self.origin_chip) + '" # normaly start with 0,0\n\
home_chip = "' + str(self.home_chip) + '" # home (0um , 0um) could be different to origin (first die to measure)\n\
flat_orientation = ' + str(self.flat_orientation) + ' # flat orientation: 0, 90, 180 or 270\n\
\n\
# navigation options\n\
navigation_options = ' + str(self.navigation_options) + '\n\
\n\
# wafer positions\n\
wafer_positions = ' + str(self.wafer_positions) + '\n\
# distances from chip origin\n\
wafer_modules = ' + str(self.wafer_modules) + '\n\
\n\
# wafer parameters\n\
wafer_parameters = {\n\
\n\
"wafer_name": wafer_name,\n\
"wafer_size": wafer_size,\n\
"xsize": xsize,\n\
"ysize": ysize,\n\
"nchips": nchips,\n\
"nmodules": nmodules,\n\
"origin_chip": origin_chip,\n\
"home_chip": home_chip,\n\
"flat_orientation": flat_orientation,\n\
"wafer_positions": wafer_positions,\n\
"wafer_modules": wafer_modules,\n\
"real_origin_chip": real_origin_chip,\n\
"navigation_options": navigation_options\n\
\n\
}'

        if nameFile!="":
            # create texto
            with open(nameFile, 'w') as f:
                f.write(texto)
            retval = messageBox(self,"Save wafermap","Wafermap file saved!","info") 
            
        


