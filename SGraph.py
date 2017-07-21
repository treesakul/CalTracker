import sys
from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

class Graph(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Graph, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget

        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)
        #self.exercise = []
        self.dates = []
        #self.goal = []
        self.food = []
        self.num = 0
        
    def add_list(self,n,lis,dates, ex, num):
        self.exercise = ex
        self.dates = dates
        self.net = n
        #self.goal = go
        self.food = lis
        self.num = num
        
    def plot(self):
        ''' plot some random stuff '''
        temp = []
        for i in range(self.num):
            temp.append(i)

        # random data

        # create an axis
        ax = self.figure.add_subplot(111)

        
        # discards the old graph
        ax.hold(False)

        # plot data
        ax.plot(temp,self.food, self.exercise, '*-')
        
        ax.set_xticks(temp)
        ax.set_xticklabels(self.dates,rotation='vertical', fontsize=5)
        # refresh canvas
        self.canvas.draw()


