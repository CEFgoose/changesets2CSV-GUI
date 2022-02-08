
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import sip


def delete_user_modal(main):
    if len(main.selected_user_ids)>0:
        main.delete_user_warning = QMessageBox()
        main.delete_user_warning.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        main.delete_user_warning.setGeometry(500,500,500,500)
        main.delete_user_warning.setWindowTitle("Delete User")
        main.delete_user_warning.setText("Are you sure you want to delete the selected users?")
        main.delete_user_warning.show()
        returnValue = main.delete_user_warning.exec()
        if returnValue == QMessageBox.Ok:
            for i in main.selected_user_ids:
                itemIndex=main.teamList.indexOfTopLevelItem(main.team_dict[i].list_entry)
                main.teamList.takeTopLevelItem(itemIndex)
                del main.team_dict[i]
                for index,value in enumerate(main.team_obj['users']):
                    if value['user_id'] == i:
                        del main.team_obj['users'][index]            
        elif returnValue == QMessageBox.Cancel:
            main.delete_user_warning.close()
        restack_list(main)

def restack_list(main):
    main.teamList.clear()
    for i in main.team_dict.values():
        i.construct_list_item(main)


