
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
    comments_list.setColumnCount(3)
    comments_list.doubleClicked.connect(lambda:comment_list_clicked(main,comments_list))
    comments_list.setHeaderLabels(["Misspelled Word","Changeset ID","Date"])
    comment_list_box_layout.addWidget(comments_list)

    hashtag_list_box=QGroupBox()
    hashtag_list_box.setTitle("Misspelled Hashtags")
    hashtag_list_box_layout=QVBoxLayout()
    hashtag_list_box.setLayout(hashtag_list_box_layout)
    Hsplitter.addWidget(hashtag_list_box)


    hashtag_list=QTreeWidget()
    hashtag_list.setColumnCount(3)
    hashtag_list.setHeaderLabels(["Misspelled Hashtag","Changeset ID","Date"])
    hashtag_list_box_layout.addWidget(hashtag_list)



    missing_hashtag_list_box=QGroupBox()
    missing_hashtag_list_box.setTitle("Missing Hashtags")
    missing_hashtag_list_box_layout=QVBoxLayout()
    missing_hashtag_list_box.setLayout(missing_hashtag_list_box_layout)
    Hsplitter.addWidget(missing_hashtag_list_box)


    missing_hashtag_list=QTreeWidget()
    missing_hashtag_list.setColumnCount(3)
    missing_hashtag_list.setHeaderLabels(["Hashtags Missing","Changeset ID","Date"])
    missing_hashtag_list_box_layout.addWidget(missing_hashtag_list)


    populate_comment_report_list(main,editor,comments_list,hashtag_list,missing_hashtag_list)
    main.comments_report_widget.show()
    
def populate_comment_report_list(main,editor,comments_list,hashtag_list,missing_hashtag_list):
    for i in editor.misspelled_words:
        item=QTreeWidgetItem()
        item.setText(0,i[0])
        item.setText(1,i[1])
        item.setText(2,i[2])
        comments_list.addTopLevelItem(item)
    for i in editor.misspelled_hashtags:
        item=QTreeWidgetItem()
        item.setText(0,i[0])
        item.setText(1,i[1])
        item.setText(2,i[2])
        hashtag_list.addTopLevelItem(item)  
    for i in editor.missing_hashtag_changeset_ids:

        item=QTreeWidgetItem()
        item.setText(0,str(i[0]))
        item.setText(1,str(i[1]))
        item.setText(2,str(i[2]))
        missing_hashtag_list.addTopLevelItem(item)  

def comment_list_clicked(main,inList):
    main.selected_word=inList.selectedItems()[0].text(0)
    accept_word_modal(main)

def accept_word_modal(main):
    main.accept_word_widget=QMessageBox()
    main.accept_word_widget.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    main.accept_word_widget.setGeometry(500,500,500,500)
    main.accept_word_widget.setWindowTitle("Add accepted word")
    main.accept_word_widget.setText('Are you sure you want to add "%s" to accepted comment words?'%(main.selected_word))
    main.accept_word_widget.show()
    returnValue = main.accept_word_widget.exec()
    if returnValue == QMessageBox.Ok:
        if main.selected_word not in main.accepted_words:
            main.accepted_words.append(main.selected_word)
            
    elif returnValue == QMessageBox.Cancel:
        main.accept_word_widget.close()