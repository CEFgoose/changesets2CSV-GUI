
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



def delete_user_modal(main):
    main.directionPopup = QMessageBox()
    main.directionPopup.setGeometry(500,500,500,500)
    main.directionPopup.setWindowTitle("Delete User")
    main.directionPopup.setText("Are you sure you want to delete the selected users?")
    main.directionPopup.show()

    returnValue = main.directionPopup.exec()
    if returnValue == QMessageBox.Ok:
        for i in main.selected_user_ids:
            itemIndex=main.teamList.indexOfTopLevelItem(main.team_dict[i].list_entry)
            main.teamList.takeTopLevelItem(itemIndex)
            del main.team_dict[i]
            for index,value in enumerate(main.team_obj['users']):
                if value['user_id'] == i:
                    del main.team_obj['users'][index]            
    else:
        pass