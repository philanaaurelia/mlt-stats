import requests
import json
import random
import os
from pathlib import Path

class MLT_Data:
    def __init__(self, filename):
        self.filename = filename
        myfile = Path("static/" + self.filename)
        myfile.touch(exist_ok = True)

        with open(str(myfile),'r+') as file:
            # First we load existing data into a dict.
            if len(file.readlines()) == 0:
                data = {"fellows" : []}
                json.dump(data, file, indent = 4)
                
            # move cursor to beginning of file
            file.seek(0)
            file_data = file.read()
            json.loads(file_data)
          

            print("hello")
        
    def __str__(self):
        return "filename: " + self.filename + "\n";
        
    def create_user(self, name, email):
        self.user = {"name": name,
        "email": email,
        "record":[] }
    
    def create_record(self, month, year):
        self.record = {"month": month,
        "year": year,
        "points": []
        }
        
    ''' def create_points(self):
        self.point = {"multipler": mult,
        "name": severity,
        "value": value,
        "notes": notes } '''
        
        
        
''' def append_data(dta):
    # twit_key = os.getenv('twit_key') - This is for Heroku
    twit_key = 'tMhwBBDqqeEiozlZVgCkzzCVO' '''