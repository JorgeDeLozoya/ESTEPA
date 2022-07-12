

#PARTS DEL CODI TEMPORALS
#////////////////////////////////////////////////////////////////// 

       # NETEJAR ELS VALORS                                                                            #10/7
    # def clean_values(self):                                                                                      
    #     widgets.txtLoadedValues.setPlainText("")

    # NETEJAR ELS RESULTATS
    # def clean_results(self):                                                                                      
    #     widgets.txtParametersResult.setPlainText("")

    #PRINT BUTTONS

    # def print_home(self):
    #     print("Home")

    # def print_analyze(self):
    #     print("Analyze")


    # def print_consult(self):
    #     print("Consult")


    # def print_about(self):
    #     print("About")

    # def print_results(self):
    #     print("Results")


    # PRINT MOUSE EVENTS
    #if event.buttons() == Qt.LeftButton:
    #    print('Mouse click: LEFT CLICK')
    #if event.buttons() == Qt.RightButton:
    #    print('Mouse click: RIGHT CLICK')

        #PRINT CONSOLA
        # widgets.HomeWindow.clicked.connect(self.print_home)
        # widgets.AnalyzeWindow.clicked.connect(self.print_analysis)
        # widgets.ConsultWindow.clicked.connect(self.print_consult)
        # widgets.btn_exit.clicked.connect(self.print_about)
        # widgets.VisualizeGraphsButton.clicked.connect(self.print_results)+
        # widgets.btnCorrelationFiles.clicked.connect(self.print_correlation)
        #widgets.OutlinerBox.currentIndexChanged.connect(self.print_outlinerbox)
        #widgets.btnAnalyzeFiles.clicked.connect(self.buttonClick)                             #Botó analitzar
        #widgets.VisualizeGraphsButton.clicked.connect(self.buttonClick)                    #Resultats grafiques
        #widgets.CleanResultsButton.clicked.connect(self.buttonClick)                        #Netejar els resultats
   
        
        #PAGE ESTEPA
        #widgets.btnAnalyzeFiles.clicked.connect(self.analyzeFiles)

        #LEFT MENUS
        #widgets.btn_widgets.clicked.connect(self.buttonClick)




        # BOTÓ PER CARREGAR LES DADES .DAT I .PPG           
        #if btnName == "LoadFilesButton":
            #DirectoryDat = 
            #DirectoryPpg = 
            #label.setText("Directory '% s' created" % DirectoryDat)
            #label.setText("Directory '% s' created" % DirectoryPpg)


        #BOTÓ CORRELATION
            
            #self.btnAnalyzeFiles.connect(self.getItems)
            #if per comprovar que s'han agafat dos opcions
            #if si no s'han agafat dos variables
            #else si no s'ha agat cap variable

            #Correlació (2 var.)
            #//////////////////////////////////////////////////////////////////  
            #correlation()   



        # BOTÓ ANALITZAR
            # if btnName == "btnAnalyzeFiles":
                
            #     file_dat = ResultFile("test.dat", "metrics")
            #     if file_dat.error:
            #         print("Error in file: " + file_dat.error_message)
            #     else:
            #         print(file_dat.print_info())
            #         print("Configuration: " + str(config_estepa_file))
            #         for param in file_dat.params_list:
            #             sEstepa = StatisticsEstepa(param, file_dat.param_to_list(param), config_estepa_file)
            #             print(param + " : " + str(sEstepa.data_list))
            #             print(" - Mean:   \t" + str(sEstepa.mean))
            #             print(" - Median: \t" + str(sEstepa.median))
            #             print(" - Stdev:  \t" + str(sEstepa.stdev))
            #             print("")
                    
            #     file_dat2 = ResultFile("12914-1CV100KHz.dat", "old")

            #     if file_dat2.error:
            #         print("Error in file 2: " + file_dat2.error_message)
            #     else:
            #         print(file_dat2.print_info())
            #         for param in file_dat2.params_list:
            #             if param == "cmax(pF)":
            #                 config_estepa_file2 = {
            #                     "method": "k-sigma",  # none, f-spread or k-sigma
            #                     "lna": False,
            #                     "limmin": 580.0,
            #                     "limmax": 600.0
            #                 }
            #                 sEstepa2 = StatisticsEstepa(param, file_dat2.param_to_list(param), config_estepa_file2)
            #             else:
            #                 sEstepa2 = StatisticsEstepa(param, file_dat2.param_to_list(param), config_estepa_file)
            #             # print(param + " : " + str(sEstepa2.data_list))
            #             print(param)
            #             print(" - Mean:   \t" + str(sEstepa2.mean))
            #             print(" - Median: \t" + str(sEstepa2.median))
            #             print(" - Stdev:  \t" + str(sEstepa2.stdev))
            #             print(" - Points:  \t" + str(sEstepa2.points_end) + "/" + str(sEstepa2.points_ini))
            #             print("")