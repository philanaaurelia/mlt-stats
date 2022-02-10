import requests
import json
import random
import os
from fellow import Fellow
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
            self.json_data = json.loads(file_data)

            print(self.json_data)
        
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
        
    def calculate_meter(self, fellow):
        org_val = (fellow['org_pts'] / (fellow['org_events'] * 20.0)) * 0.65
        print(fellow['org_pts'])
        coh_val = (fellow['coh_pts'] / (fellow['coh_events'] * 20.0)) * 0.35
        print(org_val)
        return (org_val + coh_val) * 100
    
    def get_fellow_data(self, email):
        # Get JSON of fellows
        
        # search for fellow
        for fellow in self.json_data['fellows']:
            if fellow['email'] == email:
                name = fellow['name']
                profile = fellow['profile_url']
                records = fellow["records"]
                fellow_data = Fellow(name, email, profile, records, self.calculate_meter(fellow))
                return fellow_data
        return None
        

        
    ''' def create_points(self):
        self.point = {"multipler": mult,
        "name": severity,
        "value": value,
        "notes": notes } '''
        
        
        
''' def append_data(dta):
    # twit_key = os.getenv('twit_key') - This is for Heroku
    twit_key = 'tMhwBBDqqeEiozlZVgCkzzCVO' '''