import json
import random
import requests

class Song:
    def __init__(self, song, artist, artist_link, song_image, artist_image):
        self.song = song
        self.artist = artist
        self.artist_link = artist_link
        self.song_image = song_image
        self.artist_image = artist_image
        
    def __str__(self):
        return "song: " + self.song +'\n' + "artist: " + self.artist + "\n" + "artist link: " +  self.artist_link + "\n" "song_image: "\
        + self.song_image  + "artist_image: " + self.artist_image
        
def get_song_data():
    # token = os.getenv('geni_token') - This is for Heroku
    token = '4oIEUPOC23z1eaTtYaRCWnr_0dX-n9UR3HIuw538MBb5kMVWhUBdWuh1mbVq1xUC'
    url = 'https://api.genius.com/search?q=Lauryn%20Hill&per_page=50'
    headers = {'Authorization': 'Bearer ' + token}
    
    response = requests.get(url, headers=headers)
    json_body = response.json()
    
    # Find the how many items (songs containing text or songs from an artist)
    size = len(json_body['response']['hits'])
    
    # Choose a random number for our indices
    index = random.randint(1 ,size-1)
    
    # Retrieve our information
    song = json_body['response']['hits'][index]['result']['title']
    artist = json_body['response']['hits'][index]['result']['primary_artist']['name']
    artist_link = json_body['response']['hits'][index]['result']['primary_artist']['url']
    song_image = json_body['response']['hits'][index]['result']['song_art_image_url']
    artist_image = json_body['response']['hits'][index]['result']['primary_artist']['image_url']
    
    song_data = Song(song, artist, artist_link, song_image, artist_image)
    
    return song_data