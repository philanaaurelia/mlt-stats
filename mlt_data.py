import requests
import json
import random
import os
from member import Member
from pathlib import Path

class MLT_Data:
    def __init__(self, filename):
        self.filename = filename
        self.myfile = Path("static/" + self.filename)
        self.myfile.touch(exist_ok = True)
        self.load_json()
        
    def load_json(self):
        with open(str(self.myfile),'r+') as file:
            # First we load existing data into a dict.
            if len(file.readlines()) == 0:
                data = {"members" : []}
                json.dump(data, file, indent = 4)
                
            # move cursor to beginning of file
            file.seek(0)
            file_data = file.read()
            self.json_data = json.loads(file_data)

            # print(self.json_data)
        
    def __str__(self):
        return "filename: " + self.filename + "\n";
        
    def create_user(self, name, email, memtype):
        self.user = {"name": name,
        "email": email,
        "type" : memtype,
        "record":[] }
    
    def create_record(self, date):
        self.record = {"date": date,
        "points": []
        }
        
    def calculate_meter(self, fellow):
        if 'org_pts' not in fellow:
            return -1
        org_val = (fellow['org_pts'] / (fellow['org_events'] * 20.0)) * 0.65
        print(fellow['org_pts'])
        coh_val = (fellow['coh_pts'] / (fellow['coh_events'] * 20.0)) * 0.35
        print(org_val)
        return (org_val + coh_val) * 100
    
    def get_member_data(self, email = None, name = None):
        # Get JSON of fellows
        if not name:
            # search for fellow
            for member in self.json_data['members']:
                if member['email'] == email:
                    name = member['name']
                    profile = member['profile_url'] if 'profile_url' in member else None
                    role = member['role'] if 'role' in member else None
                    records = member['records'] if 'records' in member else None
                    member_data = Member(name, role, email, profile, records, self.calculate_meter(member))
                    return member_data
                    
        if not email:
            # search for fellow
            for member in self.json_data['members']:
                if member['email'] == email:
                    name = member['name']
                    role = member['role'] if 'role' in member else None
                    
                    profile = member['profile_url'] if 'profile_url' in member else None
                    records = member['records'] if 'records' in member else None
                    member_data = Member(name, role, email, profile, records, self.calculate_meter(member))
                    return member_data
        return None
        
    def get_fellows_data(self, email):
        # Get JSON of fellows
        fellows = []
        
        if not self.json_data:
            self.load_json()
            
        for member in self.json_data['members']:
            coach = member['coach'] if 'coach' in member else None
            
            if coach == email:
                member_data = self.get_member_data(member['email'])
                fellows.append(member_data)
            
        return fellows
        

        
    def add_points(self, name, points):
        if not self.json_data:
            self.load_json()
            
            
        fellow = self.get_member_data(name)
    