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

def start_get_changesets(main):
    main.teamList.setColumnCount(5)
    main.teamList.setHeaderLabels(['Name','OSM Username','OSM User Id','Role','Changesets'])        
    for i in main.selected_user_ids:
        main.team_dict[i].new_changesets=get_changesets(i)
        count=len(main.team_dict[i].new_changesets)
        main.team_dict[i].list_entry.setText(4, str(count))

def get_changesets(user=None, start_time="2022-01-20", end_time="2022-01-21", bbox=None):
    query_params = {}
    if user:
        query_params["user"] = user
    if start_time and end_time:
        if type(start_time) is list and len(start_time) == 1:
            start_time = start_time[0].strftime("%Y-%m-%d")
        if type(end_time) is list and len(end_time) == 1:
            end_time = end_time[0].strftime("%Y-%m-%d")
        query_params["time"] = ",".join([start_time, end_time])
        print(query_params["time"])
    if bbox:
        query_params["bbox"] = ",".join(bbox)
    changesets = []
    #try:
    api_url = "https://api.openstreetmap.org/api/0.6/changesets"
    session = CacheControl(requests.session())
    result = session.get(api_url, params=query_params)
    entries=str(result.text)
    entries=entries.split("</changeset>")
    entries.pop(-1)
    entries[0]=str(entries[0].rsplit("""<?xml version="1.0" encoding="UTF-8"?>""",2)[1])
    entries[0]=str(entries[0].rsplit('/">',1)[1])
    #print(entries[0])
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
                    commentText.append(i)
            comment = str(commentText)
            comment=comment.replace("'","")
            comment=comment.replace("[","")
            comment=comment.replace("]","")
            comment=comment.replace(",","")
        except:
            logging.exception('e')

        changeset=CHANGESET(set_id,set_created,set_changes,set_closed,hashtags,source,comment)
        changesets.append(changeset)
        
    return changesets
    # print(len(entries))
    # print(entries[0])
    # entries=json.loads(entries)
    # entries=str(entries).split("</changeset>")
    #sprint(len(entries))

        # root = ET.fromstring(result.text)
        # sets = root.findall("changeset")
        # changesets.extend(sets)
        # dateFormat = "%Y-%m-%dT%H:%M:%SZ"
        # while len(sets) >= 100:
        #     new_end = datetime.strptime(
        #         sets[-1].get("closed_at"), dateFormat
        #     ) - timedelta(0, 5)
        #     new_end = new_end.strftime(dateFormat)
        #     start_time = "1970-01-01" if not start_time else start_time
        #     query_params["time"] = ",".join([start_time, new_end])
        #     result = session.get(api_url, params=query_params).text
        #     root = ET.fromstring(result)
        #     sets = root.findall("changeset")
        #     changesets.extend(sets)

    # except Exception as e:
    #     print("Error with calling the API: " + str(e))
    # entry=json.loads(changesets[0])
    # print(entry)
    #return changesets

