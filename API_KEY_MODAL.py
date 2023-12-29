
import keyring
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import(
QMainWindow,QApplication,QWidget,
QGridLayout,QHBoxLayout,QVBoxLayout,
QAction,QGroupBox,QSplitter,
QFrame,QPushButton,QLabel,QDialog,QLineEdit
)

def set_api_key_modal(main):
    main.select_upload_project_widget=QDialog()
    main.select_upload_project_widget.setWindowModality(Qt.WindowModality.ApplicationModal)
    main.select_upload_project_widget_layout=QGridLayout()
    main.select_upload_project_widget.setLayout(main.select_upload_project_widget_layout)
    main.select_upload_project_widget.setGeometry(200,200,500,500)
    main.select_upload_project_widget.setWindowTitle("Add Mapillary API Key ")

    main.api_key_label=QLabel()
    main.api_key_label.setText('API KEY:')
    main.select_upload_project_widget_layout.addWidget(main.api_key_label ,0,0,1,1)

    main.api_key_field=QLineEdit()
    main.api_key_field.setPlaceholderText('Mapillary API Key')
    main.select_upload_project_widget_layout.addWidget(main.api_key_field ,0,1,1,1)
    
    confirm_button=QPushButton()
    confirm_button.setText("Confirm")
    confirm_button.clicked.connect(lambda:confrim_add_api_key(main))
    main.select_upload_project_widget_layout.addWidget(confirm_button,1,1,1,1)
    
    cancel_button=QPushButton()
    cancel_button.setText("Cancel")
    cancel_button.clicked.connect(lambda:cancel_add_api_key(main))
    main.select_upload_project_widget_layout.addWidget(cancel_button,1,0,1,1)
    
    main.select_upload_project_widget.show()
    returnValue = main.select_upload_project_widget.exec()
    return returnValue

def cancel_add_api_key(main):
    main.select_upload_project_widget.close()
    
def confrim_add_api_key(main):
    key=main.api_key_field.text()
    if key != '' and key !=None:
        keyring.set_password(service_name="maproulette", username="", password=key)
    main.select_upload_project_widget.close()