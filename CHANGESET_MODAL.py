from re import L
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import datetime
import pandas
from PROCESS_FUNCTIONS import *

def changesets_mode_widget(main):
    main.display_mode='expanded'
    main.changeset_mode_widget=QWidget()
    main.changeset_mode_widget.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    main.changeset_mode_widget.setWindowTitle("Query Mode")
    mode_widget_layout=QGridLayout()
    main.changeset_mode_widget.setLayout(mode_widget_layout)
    
    mode_button_box=QGroupBox()
    mode_widget_layout.addWidget(mode_button_box)
    mode_button_box_layout=QVBoxLayout()
    mode_button_box.setLayout(mode_button_box_layout)

    select_mode_label=QLabel()
    select_mode_label.setText("Query Mode:")
    mode_button_box_layout.addWidget(select_mode_label)

    daily_button=QRadioButton()
    daily_button.setText('Daily')
    daily_button.toggled.connect(lambda:set_mode(main,daily_button))
    mode_button_box_layout.addWidget(daily_button)

    weekly_button=QRadioButton()
    weekly_button.setText('Weekly')
    weekly_button.toggled.connect(lambda:set_mode(main,weekly_button))
    mode_button_box_layout.addWidget(weekly_button)

    monthly_button=QRadioButton()
    monthly_button.setText('Monthly')
    monthly_button.toggled.connect(lambda:set_mode(main,monthly_button))
    mode_button_box_layout.addWidget(monthly_button)

    manual_button=QRadioButton()
    manual_button.setText('Manual')
    manual_button.toggled.connect(lambda:set_mode(main,manual_button))
    mode_button_box_layout.addWidget(manual_button)

    proceed_button=QPushButton()
    proceed_button.setText("Proceed")
    proceed_button.clicked.connect(lambda:query_proceed(main))
    mode_button_box_layout.addWidget(proceed_button)
    main.changeset_mode_widget.show()

def query_proceed(main):
    if main.query_mode is not None:
        start_get_changesets(main,main.query_days_list)

def set_mode(main,button):
    today = date.today()
    yesterday=today-timedelta(days=1)
    tomorrow=today+timedelta(days=1)
    if button.isChecked():
        main.query_mode=button.text()
    if main.query_mode =="Daily":
        main.query_start_date=yesterday
        main.query_end_date=tomorrow
        get_dates(main,main.query_start_date,main.query_end_date)
    elif main.query_mode =='Weekly':
        main.query_start_date=today-timedelta(days=7)
        main.query_end_date=tomorrow
        get_dates(main,main.query_start_date,main.query_end_date)
    elif main.query_mode =="Monthly":
        main.query_start_date=today-timedelta(days=31)
        main.query_end_date=tomorrow
        get_dates(main,main.query_start_date,main.query_end_date)
    elif main.query_mode =="Manual":
        pass

def get_dates(main,start,end):
    today = date.today()
    main.query_days_list=pandas.date_range(start,end-timedelta(days=1),freq='d').tolist()
    tempList=[]
    tupList=[]
    for i in main.query_days_list:
        i=str(i)
        i=i.split(' ')[0]
        tempList.append(i)
    tempList.append(str(today))
    for index,value in enumerate(tempList[:-1]):
        tup=(value,tempList[index+1])
        tupList.append(tup)
    main.query_days_list=tupList


