# imports----------------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from settings import *

# edit user modal layout-------------------------------------------------
def hashtag_widget(main):
    main.hashtag_widget=QWidget()
    main.hashtag_widget.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    main.hashtag_widget.setWindowTitle("Edit Accepted Hashtags")

    hashtag_widget_layout=QGridLayout()
    main.hashtag_widget.setLayout(hashtag_widget_layout)
    splitter_box=QGroupBox()
    splitter_box_layout=QGridLayout()
    splitter_box.setLayout(splitter_box_layout)
    hashtag_widget_layout.addWidget(splitter_box)

    Hsplitter=QSplitter(Qt.Horizontal)
    splitter_box_layout.addWidget(Hsplitter)

    list_box=QGroupBox() 
    list_box.setTitle("list")
    list_box_layout=QGridLayout()
    list_box.setLayout(list_box_layout)

    Hsplitter.addWidget(list_box)

    hashtag_list=QTreeWidget()
    hashtag_list.setColumnCount(1)
    hashtag_list.setHeaderLabels([''])
    list_box_layout.addWidget(hashtag_list)

    control_box=QGroupBox()
    control_box.setTitle("controls")
    control_box_layout=QVBoxLayout()
    control_box.setLayout(control_box_layout)
    Hsplitter.addWidget(control_box)

    edit_field=QLineEdit()
    control_box_layout.addWidget(edit_field)

    edit_button=QPushButton()
    edit_button.setText("Edit")
    edit_button.clicked.connect(lambda:edit_hashtag(hashtag_list,edit_field,edit_button))
    control_box_layout.addWidget(edit_button)

    add_button=QPushButton()
    add_button.setText("Add")
    add_button.clicked.connect(lambda:add_hashtag(main,hashtag_list,edit_field))
    control_box_layout.addWidget(add_button)

    delete_button=QPushButton()
    delete_button.setText("Delete")
    delete_button.clicked.connect(lambda:delete_hashtag(hashtag_list))
    control_box_layout.addWidget(delete_button)

    save_button=QPushButton()
    save_button.setText("Save")
    save_button.clicked.connect(lambda:save_hashtags(main,hashtag_list))
    control_box_layout.addWidget(save_button)

    clear_button=QPushButton()
    clear_button.setText("Clear")
    clear_button.clicked.connect(lambda:clear_hashtag(edit_field,edit_button))
    control_box_layout.addWidget(clear_button)

    populate_hashtag_list(main,hashtag_list)
    main.hashtag_widget.show()
    
def populate_hashtag_list(main,hashtag_list):
    for i in main.accepted_hashtags:
        item=QTreeWidgetItem()
        item.setText(0,i)
        hashtag_list.addTopLevelItem(item)

def edit_hashtag(hashtag_list,text_field,button):
    selected_hashtag=hashtag_list.selectedItems()[0]
    if button.text()=="Edit":
        text_field.setText(selected_hashtag.text(0))
        button.setText("Apply")
    elif button.text()=='Apply':
        selected_hashtag.setText(0,text_field.text())
        text_field.setText('')
        button.setText("Edit") 

def add_hashtag(main,hashtag_list,text_field):
    if text_field.text() not in main.accepted_hashtags:
        item=QTreeWidgetItem()
        item.setText(0,text_field.text())
        text_field.setText("")
        hashtag_list.addTopLevelItem(item)

def delete_hashtag(hashtag_list):
    selected_hashtag=hashtag_list.selectedItems()[0]
    itemIndex=hashtag_list.indexOfTopLevelItem(selected_hashtag)
    hashtag_list.takeTopLevelItem(itemIndex)

def clear_hashtag(text_field,button):
    text_field.setText('')
    button.setText("Edit")

def save_hashtags(main,hashtag_list):
    main.accepted_hashtags=[]
    root = hashtag_list.invisibleRootItem()
    child_count = root.childCount()
    for i in range(child_count):
        item = root.child(i)
        hashtag = item.text(0) # text at first (0) column
        main.accepted_hashtags.append(hashtag)
    main.hashtag_widget.close()    

