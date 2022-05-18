import csv
import os
from datetime import datetime, date, timedelta


def export_CSV(data,team_name,directory):
    print("EXPORT",directory)
    today = date.today()
    csv_columns = ['name','username','user_id','role','Total Chagesets','Total Changes','Total Additions','Total Modified','Total Deleted','Misspelled Hashtags','Missing Hashtags',"Misspelled Comments"]

    #cwd=os.getcwd()
    csv_file = "%s_stats_%s.csv"%(team_name,today)
    file_path=os.path.join(directory,csv_file)
    try:
        with open(file_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in data:
                writer.writerow(data)
    except IOError:
        print("I/O error")


def construct_csv_data(main):
    print("CONSTRUCT")
    returnData=[]
    if len(main.selected_user_ids)>1:
        for i in main.selected_user_ids:
            editor=main.team_dict[i]
            obj=editor.construct_csv_data()
            returnData.append(obj)
            export_CSV(returnData,main.team_name,main.exportDirectory)
    else:
        editor=main.team_dict[main.selected_user_ids[0]]
        obj=editor.construct_csv_data()
        returnData.append(obj)
        export_CSV(returnData,editor.name,main.exportDirectory)

