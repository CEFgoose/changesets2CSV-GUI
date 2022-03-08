# imports------------------------------------------------------
import xml.etree.ElementTree as ET
import csv
import argparse
import requests
from cachecontrol import CacheControl
from datetime import datetime, date, timedelta
import os
import sys
import glob
import re
import time
from xlsxwriter.workbook import Workbook
import json
import logging
import os
from CHANGSET import *
from spellchecker import SpellChecker

# spell checker setup & variables-------------------------------
spell=SpellChecker()

# call get changesets for each selected editor------------------
def start_get_changesets(main,date_list):
    main.teamList.setColumnCount(12)
    main.teamList.setHeaderLabels(['Name','OSM Username','OSM User Id','Role','Changesets','Total Changes','Added','Modified','Deleted','Misspelled Comments', 'Misspelled Hashtags','Missing Hashtags'])        
    for i in main.selected_user_ids:
        new_changesets=[]
        total_count=0
        total_changes=0
        spell_count=0
        misspelled_hashtags=0
        missing_hashtags=0
        additions_count=0
        modification_count=0
        deleted_count=0
        for j in date_list:
            get_changeset_list=get_changesets(i,j[0],j[1])
            for k in get_changeset_list:
                new_changesets.append(k)
                additions_count +=k.added
                modification_count +=k.modified
                deleted_count +=k.deleted

            total_count+=len(get_changeset_list)

        for l in new_changesets:
            total_changes+=int(l.changes)
            misspelled = spell.unknown(l.comment)
            spell_count+=len(misspelled)
            for m in misspelled:
                if m in main.accepted_words:
                    spell_count-=1
                else:
                    main.team_dict[i].misspelled_words.append((m,l.id,l.date_created))
            for n in l.hashtags:
                if n not in main.accepted_hashtags:
                    misspelled_hashtags+=1
                    main.team_dict[i].misspelled_hastags.append((n,l.id,l.date_created))
            if len(l.hashtags)<2:
                diff=len(l.hashtags)
                if diff ==0:
                    diff=2
                missing_hashtags += diff
                main.team_dict[i].missing_hashtag_changeset_ids.append((diff,l.id,l.date_created))
        main.team_dict[i].set_changeset_info(new_changesets,total_count,misspelled_hashtags,missing_hashtags,spell_count,total_changes,additions_count,modification_count,deleted_count)
        main.team_dict[i].display_changeset_info()

# get changesets api call--------------------------------------------------
def get_changesets(user=None, start_time=None, end_time=None, bbox=None):
    query_params = {}
    if user:
        query_params["user"] = user
    if start_time and end_time:
        if type(start_time) is list and len(start_time) == 1:
            start_time = start_time[0].strftime("%Y-%m-%d")
        if type(end_time) is list and len(end_time) == 1:
            end_time = end_time[0].strftime("%Y-%m-%d")
        query_params["time"] = ",".join([start_time, end_time])

    if bbox:
        query_params["bbox"] = ",".join(bbox)
    changesets = []
    api_url = "https://api.openstreetmap.org/api/0.6/changesets"
    session = CacheControl(requests.session())
    result = session.get(api_url, params=query_params)
    entries=str(result.text)
    entries=entries.split("</changeset>")
    entries.pop(-1)
    if len(entries)>0:
        entries[0]=str(entries[0].rsplit("""<?xml version="1.0" encoding="UTF-8"?>""",2)[1])
        entries[0]=str(entries[0].rsplit('/">',1)[1])
        for i in entries:
            comment=""
            source=""
            hashtags=[]
            i=i.strip()
            entry=i.split('<tag k="source" v="')
            info=entry[0]
            info=info.split(" ")
            set_id=info[1].split('id="')[1]
            set_id=set_id.split('"')[0]
            set_created=info[2].split('created_at="')[1]
            set_created=set_created.split('"')[0]
            set_changes=info[5].split('changes_count="')[1]
            set_changes=int(set_changes.split('"')[0])
            set_closed=info[6].split('closed_at="')[1]
            set_closed=set_closed.split('"')[0]
            count_new_modified_deleted(set_id)
            try:
                tags=entry[1]
                tags=tags.strip()
                tags=tags.split("<tag k=")
                source = tags[0].split('"/>')[0]
                if ";" in source:
                    source =source.split(";")[-1]
                comment=tags[-1].split('"comment" v="')[1]
                comment=comment.split('"/>')[0]
                comment=comment.split(" ")
                hashtags=[]
                commentText=[]
                for i in comment:
                    if "#" in i:
                        hashtags.append(i)
                    else:
                        if "."in i:
                            i=i.split(".")[0]
                        if ","in i:
                            i=i.split(",")[0]
                        if i != '':
                            commentText.append(i)
                comment = commentText
                AMD_info= count_new_modified_deleted(set_id)
                added=AMD_info['Added']   
                modified=AMD_info['Modified'] 
                deleted=AMD_info['Deleted'] 
                changeset=CHANGESET(set_id,set_created,set_changes,set_closed,hashtags,source,comment,added,modified,deleted)
                changesets.append(changeset)
            except:
                logging.exception('e')
                pass

    return changesets

def count_new_modified_deleted(changesetID):
    api_url = "https://www.openstreetmap.org/api/0.6/changeset/{changesetID}/download".format(
        changesetID=changesetID
    )
    session = CacheControl(requests.session())
    result = session.get(api_url).text
    root = ET.fromstring(result)
    newModifiedDeleted = {}
    newModifiedDeleted["Added"] = len(root.findall("create"))
    newModifiedDeleted["Modified"] = len(root.findall("modify"))
    newModifiedDeleted["Deleted"] = len(root.findall("delete"))
    return(newModifiedDeleted)