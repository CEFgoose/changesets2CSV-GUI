import csv
import os
from datetime import datetime, date, timedelta


def export_CSV(main,data):
    today = date.today()
    if main.target_metric=='OSM':
        csv_columns = ['name','username','user_id','role','Total Chagesets','Total Changes','Total Additions','Total Modified','Total Deleted','Misspelled Hashtags','Missing Hashtags',"Misspelled Comments"]
    else:
        csv_columns = ['name','username','maproulette_id','role','Tasks Completed', 'Score','Average Time']
    #cwd=os.getcwd()
    csv_file = "%s_%sstats_%s.csv"%(main.team_name,main.target_metric,today)
    file_path=os.path.join(main.exportDirectory,csv_file)
    try:
        with open(file_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in data:
                writer.writerow(data)
    except IOError:
        print("I/O error")


def construct_csv_data(main):
    returnData=[]
    if len(main.selected_user_ids)>1:
        for i in main.selected_user_ids:
            editor=main.team_dict[i]
            obj=editor.construct_csv_data(main.target_metric)
            returnData.append(obj)
            export_CSV(main,returnData)
    else:
        editor=main.team_dict[main.selected_user_ids[0]]
        obj=editor.construct_csv_data(main.target_metric)
        returnData.append(obj)
        export_CSV(main,returnData)

