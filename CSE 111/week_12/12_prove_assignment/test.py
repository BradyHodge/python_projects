import os
import eyed3
import requests
from tqdm import tqdm

def update_metadata(directory_path, api_key):
    # Get a list of all mp3 files in the specified directory
    mp3_files = [f for f in os.listdir(directory_path) if f.endswith('.mp3')]

    # Loop through each mp3 file
    for mp3_file in tqdm(mp3_files):
        # Load the mp3 file using eyed3
        audiofile = eyed3.load(os.path.join(directory_path, mp3_file))

        # Check if artist and title tags are present
        if audiofile.tag.artist and audiofile.tag.title:
            # Search for the song on the online music database using the artist and title tags
            response = requests.get(f'https://api.musixmatch.com/ws/1.1/track.search?q_artist={audiofile.tag.artist}&q_track={audiofile.tag.title}&apikey={api_key}')
            data = response.json()

            # Check if a result was found
            if data['message']['header']['status_code'] == 200 and data['message']['body']['track_list']:
                # Get the first result
                track = data['message']['body']['track_list'][0]['track']

                # Update the metadata fields using the information from the online database
                audiofile.tag.album = track['album_name']
                audiofile.tag.album_artist = track['album_artist']
                audiofile.tag.track_num = track['track_number']
                audiofile.tag.genre = track['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name']

                # Save the updated metadata to the mp3 file
                audiofile.tag.save()

# Prompt user for directory path and API key
directory_path = input('Enter directory path: ')
api_key = input('Enter API key: ')

# Update metadata for all mp3 files in specified directory
update_metadata(directory_path, api_key)