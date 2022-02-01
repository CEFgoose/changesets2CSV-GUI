# imports----------------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from EDITOR import EDITOR

# open edit user modal---------------------------------------------------
def open_edit_user_widget(main,users):
    count=len(users)
    counter=0
    user=main.team_dict[users[0]]
    edit_user_widget(main,user=user)

# edit user modal layout-------------------------------------------------
def edit_user_widget(main,user=None):
    main.edit_user_widget=QWidget()
    main.edit_user_widget.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    main.edit_user_widget.setWindowTitle("Edit User")
    edit_user_widget_layout=QGridLayout()
    main.edit_user_widget.setLayout(edit_user_widget_layout)
    textfield_box=QGroupBox()
    edit_user_widget_layout.addWidget(textfield_box)
    textfield_box_layout=QVBoxLayout()
    textfield_box.setLayout(textfield_box_layout)
    edit_user_label=QLabel()
    textfield_box_layout.addWidget(edit_user_label)
    name_label=QLabel()
    name_label.setText("Name")
    textfield_box_layout.addWidget(name_label)
    main.edit_name_field=QLineEdit()
    textfield_box_layout.addWidget(main.edit_name_field)
    username_label=QLabel()
    username_label.setText("Username")
    textfield_box_layout.addWidget(username_label)
    main.edit_username_field=QLineEdit()
    textfield_box_layout.addWidget(main.edit_username_field)
    userid_label=QLabel()
    userid_label.setText("User ID")
    textfield_box_layout.addWidget(userid_label)
    main.edit_userid_field=QLineEdit()
    textfield_box_layout.addWidget(main.edit_userid_field)
    role_label=QLabel()
    role_label.setText("Role")
    textfield_box_layout.addWidget(role_label)
    main.edit_role_field=QLineEdit()
    textfield_box_layout.addWidget(main.edit_role_field)
    edit_user_label.setText("Edit User: %s"%(user.name))
    main.edit_name_field.setText(user.name)
    main.edit_username_field.setText(user.osm_username)
    main.edit_userid_field.setText(user.osm_user_id)
    main.edit_role_field.setText(user.role)
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
    main.edit_user_widget.show()
    
# save changes to selected editor--------------------------------------
def save(main,user):
    if user is not None:
        user.updateBasicInfo(main.edit_name_field.text(),main.edit_username_field.text(),main.edit_userid_field.text(),main.edit_role_field.text())
        for i in  main.team_obj['users']:
            if i['user_id']==user.osm_user_id:
                i['name']=user.name 
                i['username']=user.osm_username
                i['user_id']=user.osm_user_id
                i['role']=user.role
    main.edit_user_widget.close()

# discard changes and close edit user modal---------------------------
def cancel(main):
    main.edit_user_widget.close()
