from __future__ import print_function

import os.path

from oauth2client.service_account import ServiceAccountCredentials
import gspread

# If modifying these scopes, delete the file token.json.
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']

NAME_COL_TITLE = "Name"
EMAIL_COL_TITLE = "Email"
worksheet = None

def init():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)
    
    # get the instance of the Spreadsheet
    sheet = client.open_by_key('1Prtbjay-dvzveI6RidZRJ9BuM3W-64sO7vAmuo-qKr4')
        #  client.open('https://docs.google.com/spreadsheets/d/1JhVbyzW1cHmUMbCERdHZcgpegb3JU38D18xtSItam-4/edit?usp=sharing')
    
    # get the first sheet of the Spreadsheet
    worksheet = sheet.get_worksheet(0)
    
    # get the total number of columns
    print(sheet_instance.col_count)
    ## >> 26
    
    
    # get the value at the specific cell
    print(sheet_instance.cell(col=3,row=2).value)
    ## >> <Cell R2C3 '63881'>
    
    
# def 
    
def get_fellow_data(email):
    return ""
    
def get_fellow_names():
    fellows : [str] = []
    
    if not worksheet:
        init();
    
    cell = worksheet.find(NAME_COL_TITLE)
    
    return worksheet.col_values(cell.col)
    
    
    