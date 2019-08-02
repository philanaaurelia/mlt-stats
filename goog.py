import requests
import random
import json
import os
# 
class imageLoc:
    def __init__(self,link):
        self.l = link
    def __str__(self):
        return self.l
        
     
def getIMG():
    # api_key = os.getenv('pixy_key')
    api_key = 'AIzaSyAuQo0MS-TgejKC75M9uGTeU0WXnyxeOww'
    custom_search_id = '013643261414232163987:vg80_3efar8'
    print ("this is api_key %s",api_key)
    url = "https://www.googleapis.com/customsearch/v1?q=Lauryn%20Hill&cx=" + custom_search_id + "&searchType=image&imgSize=xxlarge&key=" + api_key
    # url = "https://pixabay.com/api/?key=" + api_key + "&q=purple+flowers&image_type=photo"
    response = requests.get(url)
    # removed the headers=header from function
    imgs = response.json()
    # print ("this is the response %s",imgs)
    size = len(imgs['items'])
    i = random.randint(1,size-1)
    print ("rand int: %s", i)
    uri = imgs['items'][i]['link']
    
    print ("this is the image link %s",uri)
    img = imageLoc(uri)
    
    
    return img