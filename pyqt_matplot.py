import sys
from PyQt4 import QtGui, QtCore
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt
import random, time

WINDOW_HEIGHT = 800
WINDOW_LENGTH = 1000

class Window(QtGui.QDialog):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,WINDOW_LENGTH,WINDOW_HEIGHT)
        self.mainLayout = QtGui.QVBoxLayout()
        self.setWindowTitle("CARDIO/GSR Sensor")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.subject_name = "Jane Doe"
        self.main_menu()
        self.record = False

        #Initializing the matplot figure. and button that will initialize the stuff
        self.figure = plt.figure()  #the matplotlib figure object
        #canvas widget that displays the figure
        #it take figure as parameter to init
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.record_data)
        self.stop_btn = QtGui.QPushButton('Stop')
        #initializes the record data function when the record button is pressed
        self.mainLayout.addWidget(self.toolbar)
        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.button)
        self.mainLayout.addWidget(self.stop_btn)
        self.setLayout(self.mainLayout)

        self.show()

        for i in range(20):
            self.record_data()
            time.sleep(0.5)

    def main_menu(self):
        logs_btn = QtGui.QPushButton("PREV_LOGS", self)
        logs_btn.move(0,0)
        logs_btn.clicked.connect(self.close_app) #TO-DO: bring up menu to list previous logs in folders
        self.mainLayout.addWidget(logs_btn)

        new_btn = QtGui.QPushButton("NEW SUBJECT", self)
        new_btn.move(WINDOW_HEIGHT/2, 0)
        new_btn.clicked.connect(self.new_subject)
        self.mainLayout.addWidget(new_btn)


    def record_data(self): #Plotting the data using matplotlib Backend

        data = [random.random() for i in range(420)]
        ax = self.figure.add_subplot(311)
            #gets rid of old graph when function is called
        ax.hold(False)
        ax.plot(data, "*-")
        #refresh the canvas
        data2 = [random.random() for i in range(30)]
        ax = self.figure.add_subplot(312)
        # gets rid of old graph when function is called
        ax.hold(False)
        ax.plot(data2, "*-")
        #the final draft
        data3 = [random.random() for i in range(200)]
        ax = self.figure.add_subplot(313)
        # gets rid of old graph when function is called
        ax.hold(False)
        ax.plot(data3, "*-")


        self.canvas.draw()
        app.processEvents()
        #also need to create function that will work with previous log Data


    def new_subject(self):
        print "Adding a new subject"
        ##=================TO-DO======== make a subject window for people too add new subject

    def close_app(self):
        print "Clicked the close app button"
        sys.exit()


print "yo"

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())