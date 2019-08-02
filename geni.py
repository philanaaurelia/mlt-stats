import json
import random
import requests

class Song:
    def __init__(self, song, artist, song_image, artist_image):
        self.song = song
        self.artist = artist
        self.song_image = song_image
        self.artist_image = artist_image
        
    def __str__(self):
        return "song: " + self.song +'\n' + "artist: " + self.artist + "\n" + "song_image: "\
        + self.song_image  + "artist_image: " + self.artist_image
        
def get_song_data():
    token = 'GbCCGKGuXbyQGcnHvrFsoBgsQgUO3u7cMSrbefQHKKdpGIKaO2-vi740pdyzSsQK'
    url = 'https://api.genius.com/search?q=Lauryn%20Hill&per_page=50'
    headers = {'Authorization': 'Bearer ' + token}
    
    response = requests.get(url, headers=headers)
    json_body = response.json()
 
    # print json.dumps(json_body, indent=2)
    
    # Find the how many items (songs containing text or songs from an artist)
    size = len(json_body['response']['hits'])
    
    # Choose a random number for our indices
    index = random.randint(1 ,size-1)
    
    # Retrieve our information
    song = json_body['response']['hits'][index]['result']['title']
    artist = json_body['response']['hits'][index]['result']['primary_artist']['name']
    song_image = json_body['response']['hits'][index]['result']['song_art_image_url']
    artist_image = json_body['response']['hits'][index]['result']['primary_artist']['image_url']
    
    song_data = Song(song, artist, song_image, artist_image)
    
    return song_data