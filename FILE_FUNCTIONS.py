# imports-----------------------------------------
from PyQt5.QtWidgets import *
import json
from EDITOR import *
from DELETE_USER_MODAL import *
from datetime import datetime, date, timedelta
from PyQt5 import sip
import keyring
import requests
API_PATH = "api/v2/users/find"
BASE_URL= "https://maproulette.org/"
KEY=keyring.get_password("maproulette",'')
from string import ascii_uppercase as alcUP
from string import ascii_lowercase as alcLOW

# import team json file---------------------------
def import_team_json(main):
    files = QFileDialog.getOpenFileNames(main, main.filters, main.importDirectory, main.select_filters)[0]
    if len(files)>0:
        main.team_file=files[0]
        with open(main.team_file, 'r') as team_file:
            team_obj=team_file.read()
            if main.team_obj == False:
                main.team_obj = json.loads(team_obj)
                main.loaded_team_obj=team_obj
            else:
                team_obj=json.loads(team_obj)
                for i in team_obj['users']:
                    main.team_obj['users'].append(i)
                main.loaded_team_obj=main.team_obj
                autosave_team_file(main)   
            main.team_name=main.team_obj['properties']['team']
            main.team_name_field.setText(main.team_name)
        parse_editors(main,main.team_obj)
        autosave_team_file(main)   
        if 'accepted_words' in main.team_obj['properties']:
            main.accepted_words=main.team_obj['properties']['accepted_words']
            for letter in alcUP:
                main.accepted_words.append("%s"%(letter))
            for letter in alcLOW:
                main.accepted_words.append("%s"%(letter))
        if 'accepted_hashtags' in main.team_obj['properties']:   
            main.accepted_hashtags=main.team_obj['properties']['accepted_hashtags']
            
            
# get user maproulette id--------------------            
            
def get_single_user_id_from_api(user):

    if KEY != None and KEY != '':
        response = requests.get(
            BASE_URL + API_PATH,
            headers={"apikey": KEY},
            params={"username": user},
            # verify=VERIFY_CERT,
        )
        if response.json():
            print(response.json()[0]["id"])
            return response.json()[0]["id"]
        
            
# parse editors from json file--------------------
def parse_editors(main,team_obj):
    main.team_dict={}
    for i in team_obj['users']:
        if not 'maproulette_id' in i.keys():
            user=i['username']
            print('mapillary_id not found for %s'%(user))
            maproulette_id = get_single_user_id_from_api(user)
            i['maproulette_id']=maproulette_id
            
            
            
        editor=EDITOR(i['name'],i['username'],i['user_id'],i['maproulette_id'],i['role']) 
        editor.construct_list_item(main)
        main.team_dict[editor.osm_user_id]=editor

# auto-save team file on close--------------------
def autosave_team_file(main):
    if len(main.team_obj['users'])>0:
        main.team_obj['properties']['team']=main.team_name
        main.team_obj['properties']['version']+=.1
        main.team_obj['properties']['last_modified']=str(date.today())
        main.team_file=main.team_file.rsplit("/",1)[0]
        main.team_file=main.team_file+'/%s.json'%(main.team_name)
        with open (main.team_file,'w+')as save_file:
            json.dump(main.team_obj, save_file)


# manual save team file----------------------------
def save_team_file(main):
    if main.team_obj:
        main.team_obj['properties']['team']=main.team_name
        main.team_obj['properties']['version']+=1
        main.team_obj['properties']['last_modified']=str(date.today())
        main.team_file=main.team_file.rsplit("/",1)[0]
        main.team_file=main.team_file+'/%s.json'%(main.team_name)
        with open (main.team_file,'w+')as save_file:
            json.dump(main.team_obj, save_file)

# save changed variables to settings---------------
def save_settings(main):
    main.team_obj['properties']['accepted_words']=main.accepted_words
    main.team_obj['properties']['accepted_hashtags']=main.accepted_hashtags
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

