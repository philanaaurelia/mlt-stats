import json
import random
import requests

class Member:
    def __init__(self, name = "", email = "", profile =" ", records = [], meter = 0.0):
        self.name = name
        self.email = email
        
        if profile != "":
            self.profile = profile
        else:
            self.profile = "https://www.kindpng.com/picc/m/99-997900_headshot-silhouette-person-placeholder-hd-png-download.png"
           
        self.records = records
        self.meter_val = meter
        
    def __str__(self):
        return "name: " + self.name +'\n' + "email: " + self.email + "\n"
        
