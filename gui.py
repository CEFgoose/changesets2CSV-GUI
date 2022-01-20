
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject,QTimer,QTime,QThread,QEventLoop
from PyQt5.QtWidgets import(QMainWindow,QApplication,QWidget,
QGridLayout,QHBoxLayout,QVBoxLayout,
QMenuBar,QMenu,QAction,QStatusBar,
QGroupBox,QSplitter,QTabWidget,QFrame,
QPushButton,QRadioButton,QLabel,
QListView,QTableView,QHeaderView,
QLCDNumber,QCalendarWidget)
import os
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("CHANGESETS TO CSV")
        self.resize(2060,1110)
        self.move(10,20)
        self.mainWidget = QWidget()
        self.layout= QHBoxLayout()
        self.mainWidget.setLayout(self.layout)
        self.setCentralWidget(self.mainWidget)
        self.topLeftFrame=QFrame(self)
        self.topLeftFrame.setFrameShape(QFrame.StyledPanel)
        self.layout.addWidget(self.topLeftFrame)

        
def main(args):
        app = QApplication(args)
        main=MainWindow()
        main.show()
        sys.exit(app.exec_())


##### MAIN LOOP INIT ####
while  True:
    main(sys.argv)