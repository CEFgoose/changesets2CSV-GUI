from PyQt5.QtWidgets import *
import json
from EDITOR import *
from DELETE_USER_MODAL import *
from datetime import datetime, date, timedelta
def import_team_json(main):
    files = QFileDialog.getOpenFileNames(main, main.filters, main.importDirectory, main.select_filters)[0]
    main.team_file=files[0]
    with open(main.team_file, 'r') as team_file:
        team_obj=team_file.read()
        main.team_obj = json.loads(team_obj)
    main.loaded_team_obj=team_obj
    parse_editors(main,main.team_obj)


def parse_editors(main,team_obj):
    main.team_dict={}
    for i in team_obj['users']:
        editor=EDITOR(i['name'],i['username'],i['user_id'],i['role']) 
        item=QTreeWidgetItem()
        editor.list_entry=item
        editor.display_basic_info()
        main.teamList.addTopLevelItem(editor.list_entry)
        main.team_dict[editor.osm_user_id]=editor


def save_team_file(main):
    main.team_obj['properties']['version']+=.1
    main.team_obj['properties']['last_modified']=str(date.today())
    with open (main.team_file,'w+')as save_file:
        json.dump(main.team_obj, save_file)
        #save_file.writelines(main.team_obj)

def delete_users(main):  
    delete_user_modal(main) 

