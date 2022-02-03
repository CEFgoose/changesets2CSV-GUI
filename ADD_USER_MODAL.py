from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from EDITOR import EDITOR
from PyQt5 import sip
from datetime import datetime, date, timedelta

def add_user_widget(main,user=None):
    main.add_user_widget=QWidget()
    main.add_user_widget.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    main.add_user_widget.setWindowTitle("add User")
    add_user_widget_layout=QGridLayout()
    main.add_user_widget.setLayout(add_user_widget_layout)
    textfield_box=QGroupBox()
    add_user_widget_layout.addWidget(textfield_box)
    textfield_box_layout=QVBoxLayout()
    textfield_box.setLayout(textfield_box_layout)
    add_user_label=QLabel()
    textfield_box_layout.addWidget(add_user_label)
    name_label=QLabel()
    name_label.setText("Name")
    textfield_box_layout.addWidget(name_label)
    main.add_name_field=QLineEdit()
    textfield_box_layout.addWidget(main.add_name_field)
    username_label=QLabel()
    username_label.setText("Username")
    textfield_box_layout.addWidget(username_label)
    main.add_username_field=QLineEdit()
    textfield_box_layout.addWidget(main.add_username_field)
    userid_label=QLabel()
    userid_label.setText("User ID")
    textfield_box_layout.addWidget(userid_label)
    main.add_userid_field=QLineEdit()
    textfield_box_layout.addWidget(main.add_userid_field)
    role_label=QLabel()
    role_label.setText("Role")
    textfield_box_layout.addWidget(role_label)
    main.add_role_field=QLineEdit()
    textfield_box_layout.addWidget(main.add_role_field)
    add_user_label.setText("add new user")
    button_box=QGroupBox()
    button_box_layout=QHBoxLayout()
    button_box.setLayout(button_box_layout)
    textfield_box_layout.addWidget(button_box)
    save_button=QPushButton()
    save_button.setText("Save")
    save_button.clicked.connect(lambda:save(main,user))
    button_box_layout.addWidget(save_button)
    cancel_button=QPushButton()
    cancel_button.setText("Cancel")
    cancel_button.clicked.connect(lambda:cancel(main))
    button_box_layout.addWidget(cancel_button)
    main.add_user_widget.show()

def save(main,user):
    user=EDITOR(main.add_name_field.text(),main.add_username_field.text(),main.add_userid_field.text(),main.add_role_field.text())
    user.list_entry=QTreeWidgetItem()
    main.teamList.addTopLevelItem(user.list_entry)
    user.display_basic_info()
    if main.team_dict:
        main.team_dict[user.osm_user_id]=user

    else:
        today = date.today()
        main.team_obj={}
        main.team_obj['users']=[]
        main.team_obj['properties']={
            'team':'TEAM',
            'version':0.1,
            'date_created':str(today),
            'last_modified':str(today)
        }
        main.team_dict={}
        main.team_dict[user.osm_user_id]=user

    user_obj={
        'role':user.role,
        'name':user.name,
        'username':user.osm_username,
        'user_id':user.osm_user_id
    }
    main.team_obj['users'].append(user_obj)
    main.add_user_widget.close()

def cancel(main):
    main.add_user_widget.close()
