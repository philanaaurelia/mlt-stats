import json
import random
import requests

class Fellow:
    def __init__(self, name, email, profile, records, meter):
        self.name = name
        self.email = email
        self.profile= profile
        self.records = records
        self.meter_val = meter
        
    def __str__(self):
        return "name: " + self.name +'\n' + "email: " + self.email + "\n"
        
