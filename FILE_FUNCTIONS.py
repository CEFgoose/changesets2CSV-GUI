from PyQt5.QtWidgets import *
import json
from EDITOR import *

def import_team_json(main):
    files = QFileDialog.getOpenFileNames(main, main.filters, main.importDirectory, main.select_filters)[0]
    main.team_file=files[0]
    with open(main.team_file, 'r') as team_file:
        team_obj=team_file.read()
        team_obj = json.loads(team_obj)
    parse_editors(main,team_obj)


def parse_editors(main,team_obj):
    main.team_dict={}
    for i in team_obj['users']:
        editor=EDITOR(i['name'],i['username'],i['user_id'],i['role'])
        main.team_dict[editor.osm_user_id]=editor
    populate_team_list(main)

def populate_team_list(main):        
    for j in main.team_dict.values():
        item=QTreeWidgetItem()
        item.setText(0, j.name)
        item.setText(1, j.osm_username)
        item.setText(2, j.osm_user_id)
        item.setText(3, j.role)
        main.teamList.addTopLevelItem(item)
        j.list_entry=item          
    