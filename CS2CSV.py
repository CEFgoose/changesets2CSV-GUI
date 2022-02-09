# imports-----------------------------------------------
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import(
QMainWindow,QApplication,QWidget,
QGridLayout,QHBoxLayout,QVBoxLayout,
QAction,QGroupBox,QSplitter,
QFrame,QPushButton,QLabel,
)
import logging
import os 
import sys
from CHANGESET_MODAL import *
from EDIT_USER_MODAL import *
from PROCESS_FUNCTIONS import *
from FILE_FUNCTIONS import *
from LIST_FUNCTIONS import *
from ADD_USER_MODAL import *
from HASHTAGS_MODAL import *
from COMMENTS_MODAL import *
from CSV_EXPORT import *
from COMMENT_REPORT_MODAL import *
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# main window class setup-------------------------------
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
# main window variables---------------------------------
        self.team_name=''
        self.selected_user_ids=[]
        self.team_dict=False
        self.team_obj=False
        self.loaded_team_obj=False
        self.query_mode=None
        self.display_mode='basic'
        self.filters = ""
        self.select_filters = "JSON (*.json)"
        desktop=os.path.expanduser("~/Desktop/")
        self.exportDirectory=os.path.join(desktop,"Changeset_reports")
        if not os.path.isdir(self.exportDirectory):
            os.makedirs(self.exportDirectory)
        self.importDirectory=os.path.expanduser("~/Documents/")


# main gui layout---------------------------------------
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
        self.control_box_layout=QVBoxLayout()
        self.controlBox.setLayout(self.control_box_layout)

        self.team_box=QGroupBox()
        self.team_box.setMaximumHeight(200)
        self.team_box.setTitle("Team")
        self.team_box_layout=QVBoxLayout()
        self.team_box.setLayout(self.team_box_layout)

        self.control_box_layout.addWidget(self.team_box)
        self.team_name_label=QLabel()
        self.team_name_label.setText("Team Name:")
        self.team_box_layout.addWidget(self.team_name_label)

        self.team_name_field=QLineEdit()
        self.team_name_field.setText(self.team_name)
        self.team_box_layout.addWidget(self.team_name_field)

        self.team_name_button_box=QGroupBox()
        self.team_name_button_box.setMaximumHeight(60)
        self.team_name_button_box_layout=QHBoxLayout()
        self.team_name_button_box.setLayout( self.team_name_button_box_layout)
        self.team_box_layout.addWidget(self.team_name_button_box)  

        self.team_name_save_button=QPushButton()      
        self.team_name_save_button.setText("Save")
        self.team_name_save_button.clicked.connect(lambda:save_team_name(self))
        self.team_name_button_box_layout.addWidget(self.team_name_save_button)

        self.team_name_reset_button=QPushButton()      
        self.team_name_reset_button.setText("Reset")
        self.team_name_reset_button.setDisabled(True)
        self.team_name_reset_button.clicked.connect(lambda:reset_team_name(self))
        self.team_name_button_box_layout.addWidget(self.team_name_reset_button)
        self.team_name_field.textChanged.connect(lambda:unlock_reset_button(self))
        self.team_box_layout.addStretch()

        self._createMenuBar()
# construct menu bar----------------------------------
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
            self.save_team_action.triggered.connect(lambda:save_team_file(self))
            fileMenu.addAction(self.save_team_action) 
            self.export_csv_action = QAction("Export CSV",self)
            self.export_csv_action.triggered.connect(lambda:construct_csv_data(self))
            fileMenu.addAction(self.export_csv_action) 
# process menu----------------------------------------
            self.get_changesets = QAction("Get OSM Changesets",self)
            self.get_changesets.triggered.connect(lambda:changesets_mode_widget(self))
            processMenu.addAction(self.get_changesets) 

            self.comment_report = QAction("Comment & Hashtag Report",self)
            self.comment_report.triggered.connect(lambda:comment_report_widget(self, self.team_dict[self.selected_user_ids[0]]))
            processMenu.addAction(self.comment_report) 
# edit menu-------------------------------------------
            self.add_user_action = QAction("Add User",self)
            self.add_user_action.triggered.connect(lambda:add_user_widget(self,self.selected_user_ids))
            editMenu.addAction(self.add_user_action) 

            self.edit_user_action = QAction("Edit User",self)
            self.edit_user_action.triggered.connect(lambda:open_edit_user_widget(self,self.selected_user_ids))
            editMenu.addAction(self.edit_user_action) 

            self.delete_user_action = QAction("Delete User",self)
            self.delete_user_action.triggered.connect(lambda:delete_user_modal(self))
            editMenu.addAction(self.delete_user_action) 

            self.edit_accepted_hashtags = QAction("Edit Accepted Hashtags",self)
            self.edit_accepted_hashtags.triggered.connect(lambda:hashtag_widget(self))
            editMenu.addAction(self.edit_accepted_hashtags) 

            self.edit_accepted_comments = QAction("Edit Accepted Comments",self)
            self.edit_accepted_comments.triggered.connect(lambda:comments_widget(self))
            editMenu.addAction(self.edit_accepted_comments)             

# close ewindow event---------------------------------
    def closeEvent(self, event):
        save_settings(self)
        if self.team_obj != self.loaded_team_obj:
            autosave_team_file(self)
        self.deleteLater()
        try:
            self.changeset_mode_widget.close()
        except Exception as e:
            print(str(e))
        self.close()
# main loop-------------------------------------------
def main(args):
        app = QApplication(args)
        main=MainWindow()
        main.show()
        sys.exit(app.exec_())

def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback) 
    sys.exit(1) 
sys.excepthook = exception_hook
# main loop init--------------------------------------
while  True:
    main(sys.argv)