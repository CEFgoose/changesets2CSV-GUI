
# imports----------------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore

# edit user modal layout-------------------------------------------------
def comment_report_widget(main,editor):
    main.comments_report_widget=QWidget()
    main.comments_report_widget.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    main.comments_report_widget.setWindowTitle("Editor Comments Report")

    comments_report_widget_layout=QGridLayout()
    main.comments_report_widget.setLayout(comments_report_widget_layout)
    splitter_box=QGroupBox()
    splitter_box_layout=QGridLayout()
    splitter_box.setLayout(splitter_box_layout)
    comments_report_widget_layout.addWidget(splitter_box)

    Hsplitter=QSplitter(Qt.Horizontal)
    splitter_box_layout.addWidget(Hsplitter)

    comment_list_box=QGroupBox() 
    comment_list_box.setTitle("Misspelled Comments")
    comment_list_box_layout=QGridLayout()
    comment_list_box.setLayout(comment_list_box_layout)

    Hsplitter.addWidget(comment_list_box)

    comments_list=QTreeWidget()
    comments_list.setColumnCount(2)
    comments_list.setHeaderLabels(["Misspelled Word","Changeset ID"])
    comment_list_box_layout.addWidget(comments_list)

    hashtag_list_box=QGroupBox()
    hashtag_list_box.setTitle("Misspelled Hashtags")
    hashtag_list_box_layout=QVBoxLayout()
    hashtag_list_box.setLayout(hashtag_list_box_layout)
    Hsplitter.addWidget(hashtag_list_box)


    hashtag_list=QTreeWidget()
    hashtag_list.setColumnCount(2)
    hashtag_list.setHeaderLabels(["Misspelled Hashtag","Changeset ID"])
    hashtag_list_box_layout.addWidget(hashtag_list)



    missing_hashtag_list_box=QGroupBox()
    missing_hashtag_list_box.setTitle("Missing Hashtags")
    missing_hashtag_list_box_layout=QVBoxLayout()
    missing_hashtag_list_box.setLayout(missing_hashtag_list_box_layout)
    Hsplitter.addWidget(missing_hashtag_list_box)


    missing_hashtag_list=QTreeWidget()
    missing_hashtag_list.setColumnCount(2)
    missing_hashtag_list.setHeaderLabels(["Hashtags Missing","Changeset ID"])
    missing_hashtag_list_box_layout.addWidget(missing_hashtag_list)

    # edit_field=QLineEdit()
    # control_box_layout.addWidget(edit_field)

    # edit_button=QPushButton()
    # edit_button.setText("Edit")
    # edit_button.clicked.connect(lambda:edit_hashtag(comments_list,edit_field,edit_button))
    # control_box_layout.addWidget(edit_button)

    # add_button=QPushButton()
    # add_button.setText("Add")
    # add_button.clicked.connect(lambda:add_comment(main,comments_list,edit_field))
    # control_box_layout.addWidget(add_button)

    # delete_button=QPushButton()
    # delete_button.setText("Delete")
    # delete_button.clicked.connect(lambda:delete_comment(comments_list))
    # control_box_layout.addWidget(delete_button)

    # save_button=QPushButton()
    # save_button.setText("Save")
    # save_button.clicked.connect(lambda:save_comments(main,comments_list))
    # control_box_layout.addWidget(save_button)

    # clear_button=QPushButton()
    # clear_button.setText("Clear")
    # clear_button.clicked.connect(lambda:clear_comment(edit_field,edit_button))
    # control_box_layout.addWidget(clear_button)

    populate_comment_report_list(main,editor,comments_list,hashtag_list,missing_hashtag_list)
    main.comments_report_widget.show()
    
def populate_comment_report_list(main,editor,comments_list,hashtag_list,missing_hashtag_list):
    for i in editor.misspelled_words:
        item=QTreeWidgetItem()
        item.setText(0,i[0])
        item.setText(1,i[1])
        comments_list.addTopLevelItem(item)
    for i in editor.misspelled_hashtags:
        item=QTreeWidgetItem()
        item.setText(0,i[0])
        item.setText(1,i[1])
        hashtag_list.addTopLevelItem(item)  
    for i in editor.missing_hashtags:
        item=QTreeWidgetItem()
        item.setText(0,i[0])
        item.setText(1,i[1])
        missing_hashtag_list.addTopLevelItem(item)  
# def edit_hashtag(comments_list,text_field,button):
#     selected_comment=comments_list.selectedItems()[0]
#     if button.text()=="Edit":
#         text_field.setText(selected_comment.text(0))
#         button.setText("Apply")
#     elif button.text()=='Apply':
#         selected_comment.setText(0,text_field.text())
#         text_field.setText('')
#         button.setText("Edit") 

# def add_comment(main,comments_list,text_field):
#     if text_field.text() not in main.accepted_words:
#         item=QTreeWidgetItem()
#         item.setText(0,text_field.text())
#         text_field.setText("")
#         comments_list.addTopLevelItem(item)

# def delete_comment(comments_list):
#     selected_comment=comments_list.selectedItems()[0]
#     itemIndex=comments_list.indexOfTopLevelItem(selected_comment)
#     comments_list.takeTopLevelItem(itemIndex)

# def clear_comment(text_field,button):
#     text_field.setText('')
#     button.setText("Edit")

# def save_comments(main,comments_list):
#     main.accepted_words=[]
#     root = comments_list.invisibleRootItem()
#     child_count = root.childCount()
#     for i in range(child_count):
#         item = root.child(i)
#         word = item.text(0) # text at first (0) column
#         main.accepted_words.append(word)
#     main.comments_widget.close()    

