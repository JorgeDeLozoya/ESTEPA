# Imports
# from PySide6 import QtWidgets
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
# import matplotlib
# import matplotlib.pyplot 

# # Ensure using PyQt5 backend
# matplotlib.use('QT5Agg')

# # Matplotlib canvas class to create figure
# class MplCanvas(Canvas):
#     def __init__(self):
#         self.fig = Figure()
#         self.ax = self.fig.add_subplot(111)
#         Canvas.__init__(self, self.fig)
#         Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#         Canvas.updateGeometry(self)

# # Matplotlib widget
# class MplWidget2(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
#         self.canvas = MplCanvas()                  # Create canvas object
#         self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
#         self.vbl.addWidget(self.canvas)
#         self.setLayout(self.vbl)

import sys
import time

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import numpy as np
from scipy.stats import norm

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        layout = QtWidgets.QVBoxLayout(self)
        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(static_canvas)
        self._static_ax = static_canvas.figure.subplots()
        

        data = np.random.normal(170, 10, 250)
        mu, std = norm.fit(data) 
        self._static_ax.hist(data, bins=25, density=True, alpha=0.2, color='b')
        xmin, xmax = self._static_ax.get_xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)

        self._static_ax.plot(x, p, 'k', linewidth=2)
        title = "Fit Values: {:.2f} and {:.2f}".format(mu, std)
        self._static_ax.set_title(title)
        self._static_ax.set_facecolor('white')