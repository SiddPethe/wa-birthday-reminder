import defs as d
import csv
from datetime import date


def getTodayBdayList(value:bool):
    if value:
        # Get today day and month
        today = date.today()
        # Empty list to be filled
        bday_list = []
        with open('/Users/siddhantpethe/python_dev/wishes/list_folder/list.csv', mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bday = row['date'].split('-')
                # check if dates match and add to info to list.
                if d.checkIfDatesMatch(today,bday):
                    bday_list.append([row['name'],row['date']])
            
            return bday_list
    else:
        return None
