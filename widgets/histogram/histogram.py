from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import matplotlib.pyplot as plt
import numpy as np

class histogram(QWidget):
    def __init__(self, layout):
        super().__init__()
        plt.style.use('dark_background')

        fig, ax = plt.subplots()

        L = 6
        x = np.linspace(0, L)
        ncolors = len(plt.rcParams['axes.prop_cycle'])
        shift = np.linspace(0, L, ncolors, endpoint=False)
        for s in shift:
            ax.plot(x, np.sin(x + s), 'o-')
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_title("'dark_background' style sheet")

        plt.show()