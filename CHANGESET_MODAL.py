from re import L
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import sip
import datetime
import pandas
from PROCESS_FUNCTIONS import *

def changesets_mode_widget(main):
    main.display_mode='expanded'
    main.changeset_mode_widget=QWidget()
    main.changeset_mode_widget.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    main.mode_widget_layout1=QGridLayout()
    main.changeset_mode_widget.setLayout(main.mode_widget_layout1)
    
    mode_button_box=QGroupBox()
    main.mode_widget_layout1.addWidget(mode_button_box)
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




    main.manual_query_box=QGroupBox()
    main.manual_query_box_layout=QVBoxLayout()
    main.manual_query_box.setLayout(main.manual_query_box_layout)
    main.mode_widget_layout1.addWidget(main.manual_query_box)
    main.query_calendar=QCalendarWidget()
    main.query_calendar.clicked.connect(lambda:set_manual_dates(main))
    main.manual_query_box_layout.addWidget(main.query_calendar)
    
    main.manual_query_dates_box=QWidget()
    main.manual_query_dates_layout=QVBoxLayout()
    main.manual_query_dates_box.setLayout(main.manual_query_dates_layout)

    main.start_dates_box=QWidget()
    main.start_dates_layout=QHBoxLayout()
    main.start_dates_box.setLayout(main.start_dates_layout)

    main.manual_query_box_layout.addWidget(main.start_dates_box)

    main.group = QButtonGroup()
    main.group.setExclusive(True)  
    # main.group.buttonClicked.connect(main.check_buttons)


    main.start_date_button=QRadioButton()
    main.start_date_button.setText("Start Date")
    main.group.addButton(main.start_date_button)
    main.start_dates_layout.addWidget(main.start_date_button)

    main.start_date_field=QLineEdit()
    main.start_dates_layout.addWidget(main.start_date_field)

    main.end_dates_box=QWidget()
    main.end_dates_layout=QHBoxLayout()
    main.end_dates_box.setLayout(main.end_dates_layout)

    main.manual_query_box_layout.addWidget(main.end_dates_box)

    main.end_date_button=QRadioButton()
    main.end_date_button.setText("End Date")
    main.group.addButton(main.end_date_button)
    main.end_dates_layout.addWidget(main.end_date_button)

    main.end_date_field=QLineEdit()
    main.end_dates_layout.addWidget(main.end_date_field)
    main.changeset_mode_widget.show()

def query_proceed(main):
    if main.query_mode is not None:
        if main.query_mode =="Manual":
            get_dates(main,main.start_date,main.end_date)  
        start_get_changesets(main,main.query_days_list)

def set_mode(main,button):
    today = date.today()
    yesterday=today-timedelta(days=1)
    tomorrow=today+timedelta(days=1)
    if button.isChecked():
        main.query_mode= button.text()

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
        

def set_manual_dates(main):
    if main.start_date_button.isChecked():
        main.start_date=main.query_calendar.selectedDate()
        main.start_date=main.start_date.toString()
        main.start_date_field.setText(main.start_date)
        main.start_date=str(main.start_date).split(" ")[1:]
        main.start_date= ' '.join([str(elem) for elem in main.start_date])
        main.start_date = datetime.strptime(main.start_date, '%b %d %Y')

    elif main.end_date_button.isChecked():
        main.end_date=main.query_calendar.selectedDate()
        main.end_date=main.end_date.toString()
        main.end_date_field.setText(main.end_date)
        main.end_date=str(main.end_date).split(" ")[1:]
        main.end_date= ' '.join([str(elem) for elem in main.end_date])
        main.end_date = datetime.strptime(main.end_date, '%b %d %Y')

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


