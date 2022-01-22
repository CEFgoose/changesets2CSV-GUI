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
    edit_name_field=QLineEdit()
    textfield_box_layout.addWidget(edit_name_field)
    edit_username_field=QLineEdit()
    textfield_box_layout.addWidget(edit_username_field)
    edit_userid_field=QLineEdit()
    textfield_box_layout.addWidget(edit_userid_field)
    edit_role_field=QLineEdit()
    textfield_box_layout.addWidget(edit_role_field)
    if user is not None:
        edit_user_label.setText("Edit User: %s"%(user.name))
        edit_name_field.setText(user.name)
        edit_username_field.setText(user.osm_username)
        edit_userid_field.setText(user.osm_user_id)
        edit_role_field.setText(user.role)
    else:
        edit_user_label.setText("Add New User:")     
    
    main.edit_user_widget.show()


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
