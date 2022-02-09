import json
import random
import requests

class Fellow:
    def __init__(self, name, email, profile, records):
        self.name = name
        self.email = email
        self.profile= profile
        self.records = records
        
    def __str__(self):
        return "name: " + self.name +'\n' + "email: " + self.email + "\n"
        
