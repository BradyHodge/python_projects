import os
import requests
from mutagen.easyid3 import EasyID3

def fill_metadata(file_path):
    # Open the MP3 file and read its existing metadata
    audio = EasyID3(file_path)
    
    # Check if the file already has a title and artist, and exit if it does
    if 'title' in audio and 'artist' in audio:
        print(f"Metadata already exists for {file_path}")
        return
    
    # Construct the URL for the online metadata source based on the file's name and artist
    filename = os.path.basename(file_path)
    artist = audio.get('artist', [''])[0]
    url = f'https://musicbrainz.org/ws/2/recording/?query=recording:{filename} AND artist:{artist}&fmt=json'
    
    # Fetch the metadata from the online source
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch metadata for {file_path}")
        return
    metadata = response.json()
    
    # Update the MP3 metadata with the new values
    audio['title'] = metadata.get('title', '')
    audio['artist'] = metadata.get('artist', '')
    audio.save()
    
    print(f"Metadata updated for {file_path}")
