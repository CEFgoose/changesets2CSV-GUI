from PyQt5.QtWidgets import *
from PyQt5 import QtCore


def open_edit_user_widget(main,users):
    count=len(users)
    counter=0
    if count <= 0:
        edit_user_widget(main)
    else:
        user=main.team_dict[users[0]]
        edit_user_widget(main,user=user)



def edit_user_widget(main,user=None):

    main.edit_user_widget=QWidget()
    main.edit_user_widget.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    if user is not None:
        main.edit_user_widget.setWindowTitle("Edit User")
    else:
        main.edit_user_widget.setWindowTitle("Add User")
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

    edit_role_field=QLineEdit()
    textfield_box_layout.addWidget(edit_role_field)
    if user is not None:
        edit_user_label.setText("Edit User: %s"%(user.name))
        main.edit_name_field.setText(user.name)
        main.edit_username_field.setText(user.osm_username)
        main.edit_userid_field.setText(user.osm_user_id)
        edit_role_field.setText(user.role)
    else:
        edit_user_label.setText("Add New User:")    

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
    cancel_button.clicked.connect(lambda:cancel(main,user))
    button_box_layout.addWidget(cancel_button)

    main.edit_user_widget.show()



def save(main,user):
    user.name=main.edit_name_field.text()
    user.username=main.edit_username_field.text()
    user.user_id=main.edit_userid_field.text()
    user.role=main.edit_role_field.text()
def cancel(main):
    main.edit_user_widget.close()
    
    # daily_button=QRadioButton()
    # daily_button.setText('Daily')
    # daily_button.toggled.connect(lambda:set_mode(main,daily_button))
    # mode_button_box_layout.addWidget(daily_button)

    # weekly_button=QRadioButton()
    # weekly_button.setText('Weekly')
    # weekly_button.toggled.connect(lambda:set_mode(main,weekly_button))
    # mode_button_box_layout.addWidget(weekly_button)

    # monthly_button=QRadioButton()
    # monthly_button.setText('Monthly')
    # monthly_button.toggled.connect(lambda:set_mode(main,monthly_button))
    # mode_button_box_layout.addWidget(monthly_button)

    # manual_button=QRadioButton()
    # manual_button.setText('Manual')
    # manual_button.toggled.connect(lambda:set_mode(main,manual_button))
    # mode_button_box_layout.addWidget(manual_button)

    # proceed_button=QPushButton()
    # proceed_button.setText("Proceed")
    # proceed_button.clicked.connect(lambda:query_proceed(main))
    # mode_button_box_layout.addWidget(proceed_button)
    # main.changeset_mode_widget.show()
