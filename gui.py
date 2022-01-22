
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject,QTimer,QTime,QThread,QEventLoop
from PyQt5.QtWidgets import(QMainWindow,QApplication,QWidget,
QGridLayout,QHBoxLayout,QVBoxLayout,
QMenuBar,QMenu,QAction,QStatusBar,
QGroupBox,QSplitter,QTabWidget,QFrame,
QPushButton,QRadioButton,QLabel,
QLCDNumber,QCalendarWidget)
import os
import sys
from CHANGESET_MODAL import *
from EDIT_USER_MODAL import *
from PROCESS_FUNCTIONS import *
from FILE_FUNCTIONS import *
from LIST_FUNCTIONS import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.query_mode=None
        self.display_mode='basic'
        self.filters = ""
        self.select_filters = "JSON (*.json)"
        self.importDirectory=os.getcwd()
        self.exportDirectory=os.path.join(self.importDirectory,"Changeset_reports")
        if not os.path.isdir(self.exportDirectory):
            os.makedirs(self.exportDirectory)
        #---------------------------------------
        self.setWindowTitle("CHANGESETS TO CSV")
        self.resize(2060,1110)
        self.move(10,20)
        self.mainWidget = QWidget()
        self.layout= QHBoxLayout()
        self.mainWidget.setLayout(self.layout)
        self.setCentralWidget(self.mainWidget)
        self.centralFrame=QFrame(self)
        self.centralFrame.setFrameShape(QFrame.StyledPanel)
        self.layout.addWidget(self.centralFrame)
        self.centralFrameLayout=QGridLayout()
        self.centralFrame.setLayout(self.centralFrameLayout)

        self.Vsplitter=QSplitter(Qt.Horizontal)
        self.centralFrameLayout.addWidget(self.Vsplitter)

        self.teamFrame=QFrame(self)
        self.teamFrame.setFrameShape(QFrame.StyledPanel)
        self.teamFrameLayout=QGridLayout()
        self.teamFrame.setLayout(self.teamFrameLayout)
        self.Vsplitter.addWidget(self.teamFrame)

        self.teamBox=QGroupBox()
        self.teamBox.setTitle("Team")
        self.teamBoxLayout=QGridLayout()
        self.teamBox.setLayout(self.teamBoxLayout)
        self.teamList=QTreeWidget()
        self.teamList.setColumnCount(4)
        self.teamList.setHeaderLabels(['Name','OSM Username','OSM User Id','Role'])
        self.teamList.setSizePolicy (QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.teamList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.teamList.clicked.connect(lambda:team_list_clicked(self))
        self.teamBoxLayout.addWidget(self.teamList)
        self.teamFrameLayout.addWidget(self.teamBox)



        self.buttonFrame=QFrame(self)
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrameLayout=QGridLayout()
        self.buttonFrame.setLayout(self.buttonFrameLayout)
        self.Vsplitter.addWidget(self.buttonFrame)

        self.controlBox=QGroupBox()
        self.controlBox.setTitle("Controls")
        self.buttonFrameLayout.addWidget(self.controlBox)

        self.controlBoxLayout=QVBoxLayout()
        self.controlBox.setLayout(self.controlBoxLayout)

        
        # self.calendarBox = QGroupBox()
        # self.controlBoxLayout.addWidget(self.calendarBox)
        # self.calendarBoxLayout=QHBoxLayout()
        # self.calendarBox.setLayout(self.calendarBoxLayout)

        # self.calendar=QCalendarWidget()
        # self.calendarBoxLayout.addWidget(self.calendar)

        self._createMenuBar()

    def _createMenuBar(self):
            menuBar = self.menuBar()
            fileMenu = menuBar.addMenu("&File")
            editMenu = menuBar.addMenu("&Edit")
            processMenu = menuBar.addMenu("&Process")
# file menu-------------------------------------------
            self.import_team_action = QAction("Import Team List",self)
            self.import_team_action.triggered.connect(lambda:import_team_json(self))
            fileMenu.addAction(self.import_team_action) 
            self.save_team_action = QAction("Save Team List",self)
            #self.save_team_action.triggered.connect(lambda:import_team_json(self))
            fileMenu.addAction(self.save_team_action) 
# process menu----------------------------------------
            self.get_changesets = QAction("Get OSM Changesets",self)
            self.get_changesets.triggered.connect(lambda:changesets_mode_widget(self))
            processMenu.addAction(self.get_changesets) 
# edit menu-------------------------------------------
            self.edit_user_action = QAction("Edit User",self)
            self.edit_user_action.triggered.connect(lambda:open_edit_user_widget(self,self.selected_user_ids))
            editMenu.addAction(self.edit_user_action) 

            self.delete_user_action = QAction("Delete User",self)
            #self.delete_user_action.triggered.connect(lambda:import_team_json(self))
            editMenu.addAction(self.delete_user_action) 

        # #---------------------------------------
        # self.importEditorsButton=QPushButton()
        # self.importEditorsButton.setText("Import Editor List")
        # self.importEditorsButton.clicked.connect(lambda:import_editor_json(self))
        # self.centralFrameLayout.addWidget(self.importEditorsButton)
        # #----------------------------------------
        # self.getChangesetsButton=QPushButton()
        # self.getChangesetsButton.setText("get changesets")
        # self.getChangesetsButton.clicked.connect(lambda:get_changesets("10626695"))
        # self.centralFrameLayout.addWidget(self.getChangesetsButton)
def main(args):
        app = QApplication(args)
        main=MainWindow()
        main.show()
        sys.exit(app.exec_())


##### MAIN LOOP INIT ####
while  True:
    main(sys.argv)