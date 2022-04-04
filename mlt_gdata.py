from __future__ import print_function

import os.path

from oauth2client.service_account import ServiceAccountCredentials
import gspread
from member import Member

# If modifying these scopes, delete the file token.json.
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']

NAME_COL_TITLE = "Name"
EMAIL_COL_TITLE = "Email"
CALL_SCHED_TITLE = "Scheduling"
CALL_ATTEND_TITLE = "Attendance"
CALL_ASSIGN_TITLE = "Assignment"
CALL_EVENT_TITLE = "Title"
NOTES_TITLE = "Notes"
TOTAL_TITLE = "Total"


worksheet = None

def init():
    
    
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    global worksheet
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)
    
    # get the instance of the Spreadsheet
    sheet = client.open_by_key('1Prtbjay-dvzveI6RidZRJ9BuM3W-64sO7vAmuo-qKr4')
        #  client.open('https://docs.google.com/spreadsheets/d/1JhVbyzW1cHmUMbCERdHZcgpegb3JU38D18xtSItam-4/edit?usp=sharing')
    
    # get the first sheet of the Spreadsheet
    worksheet = sheet.get_worksheet(0)
    
def get_fellow_data(name):
    email: str
    records = []
    record = {}
    points = []
    meter_value = 0.0
    point_count = 0

    if worksheet is None:
        init();
        
    # TODO update what to do if name is not found
    name_cell = worksheet.find(name)
    cur_cell = worksheet.acell('C1')
    
    all_titles = worksheet.row_values(1);
    all_titles.pop(0)
    all_titles.pop(0)
    
    # create a monthly points object
    for title in all_titles:
        val = worksheet.cell(name_cell.row, cur_cell.col).value
        
        if val is None:
            val = ""
            
        val = int(val) if val.isnumeric() else val
        
        if CALL_SCHED_TITLE in cur_cell.value:
            points.append({'name' : cur_cell.value[9:], 'value' : int(val), 'total' : 5})
        elif CALL_ATTEND_TITLE in cur_cell.value:
            points.append({'name' : cur_cell.value[9:], 'value' : int(val), 'total' : 10})
        elif CALL_ASSIGN_TITLE in cur_cell.value:
            points.append({'name' : cur_cell.value[9:], 'value' : int(val), 'total' : 5})
        # elif CALL_EVENT_TITLE in cur_cell.value:
        #    points.append({'name' : cur_cell.value[9:], 'value' : int(val)})
            
        # calculate point percentage total
        if TOTAL_TITLE in cur_cell.value:
            total_val = worksheet.cell(name_cell.row, cur_cell.col).value
            if total_val.isnumeric():
                meter_value += int(total_val) / 20.0
                point_count += 1
                
        if NOTES_TITLE in cur_cell.value:
            notes_val = worksheet.cell(name_cell.row, cur_cell.col).value
            record.update({'notes' : notes_val})
            record.update({'date' : cur_cell.value[0:8]})
            record.update({'points' : points})
            records.append(record)
            print(points)
            points = []
            record = {}
                
        
        cur_cell = worksheet.cell(cur_cell.row, cur_cell.col + 1)  
        name = name_cell.value.split(' ')[0]        
        email = worksheet.cell(name_cell.row, name_cell.col + 1).value

    meter_total = ((meter_value / point_count) * 100.0) if point_count !=  0 else 0
    member_data = Member(name, "", email, "", records, meter_total )
    return member_data

    
def get_fellow_names():
    fellows : [str] = []
    
    if worksheet is None:
        init();
        
    cell = worksheet.find(NAME_COL_TITLE)
    fellows = worksheet.col_values(cell.col)
    fellows.pop(0) # remove title
    
    return fellows