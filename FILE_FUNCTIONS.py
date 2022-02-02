# imports-----------------------------------------
from PyQt5.QtWidgets import *
import json
from EDITOR import *
from DELETE_USER_MODAL import *
from datetime import datetime, date, timedelta

# import team json file---------------------------
def import_team_json(main):
    files = QFileDialog.getOpenFileNames(main, main.filters, main.importDirectory, main.select_filters)[0]
    if len(files)>0:
        main.team_file=files[0]
        with open(main.team_file, 'r') as team_file:
            team_obj=team_file.read()
            if not main.team_obj:
                main.team_obj = json.loads(team_obj)
                main.loaded_team_obj=team_obj
            else:

                team_obj=json.loads(team_obj)
                for i in team_obj['users']:
                    main.team_obj['users'].append(i)
                
                main.loaded_team_obj=main.team_obj
                autosave_team_file(main)   
        parse_editors(main,main.team_obj)

# parse editors from json file--------------------
def parse_editors(main,team_obj):
    main.team_dict={}
    for i in team_obj['users']:
        editor=EDITOR(i['name'],i['username'],i['user_id'],i['role']) 
        item=QTreeWidgetItem()
        editor.list_entry=item
        editor.display_basic_info()
        main.teamList.addTopLevelItem(editor.list_entry)
        main.team_dict[editor.osm_user_id]=editor

# auto-save team file on close--------------------
def autosave_team_file(main):
    if main.team_obj:
        main.team_obj['properties']['version']+=.1
        main.team_obj['properties']['last_modified']=str(date.today())
        with open (main.team_file,'w+')as save_file:
            json.dump(main.team_obj, save_file)


# manual save team file----------------------------
def save_team_file(main):
    if main.team_obj:
        main.team_obj['properties']['version']+=1
        main.team_obj['properties']['last_modified']=str(date.today())
        with open (main.team_file,'w+')as save_file:
            json.dump(main.team_obj, save_file)

# save changed variables to settings---------------
def save_settings(main):
    with open('settings.py', 'w+') as settings_file:
        settings_file.truncate()
        settings_file.seek(0)
        settings_file.writelines('ACCEPTED_HASHTAGS=%s\n'%(main.accepted_hashtags))
        settings_file.writelines('ACCEPTED_WORDS=%s\n'%(main.accepted_words))
        settings_file.writelines('TEAM_NAME="%s"\n'%(main.team_name))

# unlock teamname reset button----------------
def unlock_reset_button(main):
    main.team_name_reset_button.setDisabled(False)

# save new team name--------------------------
def save_team_name(main):  
    main.team_name=main.team_name_field.text()
    main.team_name_reset_button.setDisabled(True)
    
# reset team name--------------------------
def reset_team_name(main):  
    main.team_name_field.setText(main.team_name)
    main.team_name_reset_button.setDisabled(True)

