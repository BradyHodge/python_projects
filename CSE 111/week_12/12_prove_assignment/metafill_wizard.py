"""
Made by Brady Hodge
CSE 111
"""

import os
import eyed3
import requests

API_key = ''

# get the directory path from the user
# loop through all the files in the directory
# if the file is an mp3 file
# get the artist and title
# if the artist and title are not empty
# search for the song on the TheAudioDB database
# if the artist and title are empty or the song is not found
# use the file name to search Shazam database
# update the metadata fields using the information from the online database
# save the updated metadata to the mp3 file



def main():
    # Prompt user for directory path
    directory_path = input('Enter directory path: ')

    # Update metadata for all mp3 files in specified directory
    update_metadata(directory_path)


def search_audioDB(artist, title):
    url = "https://theaudiodb.p.rapidapi.com/searchalbum.php"

    querystring = {"s":f"{artist}","t":f"{title}"}

    headers = {
        "X-RapidAPI-Key": API_key,
        "X-RapidAPI-Host": "theaudiodb.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()

def search_shazam(term):
    url = "https://shazam.p.rapidapi.com/search"

    querystring = {"term":f"{term}","locale":"en-US","offset":"0","limit":"5"}

    headers = {
        "X-RapidAPI-Key": API_key,
        "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


def update_metadata(directory_path):
    # Get a list of all mp3 files in the specified directory
    mp3_files = [f for f in os.listdir(directory_path) if f.endswith('.mp3')]

    # Loop through each mp3 file
    for mp3_file in mp3_files:
        # Load the mp3 file using eyed3
        audiofile = eyed3.load(os.path.join(directory_path, mp3_file))

        # Check if artist and title tags are present
        if audiofile.tag.artist and audiofile.tag.title:
            # Search for the song on the online music database using the artist and title tags
            data = search_audioDB(audiofile.tag.artist, audiofile.tag.title)

            # Check if a result was found
            if data['album'] and data['album'][0]['strAlbum'] and data['album'][0]['strArtist'] and data['album'][0]['intYearReleased']:
                # Get the first result
                track = data['album'][0]

                # Update the metadata fields using the information from the online database
                try:
                    audiofile.tag.album = track['strAlbum']
                    audiofile.tag.album_artist = track['strArtist']
                    audiofile.tag.track_num = track['intTrackNumber']
                    audiofile.tag.genre = track['strGenre']
                    audiofile.tag.release_date = track['intYearReleased']
                except KeyError:
                    print (f"Error: {mp3_file}")

                # Save the updated metadata to the mp3 file
                audiofile.tag.save()
            else:
                data = search_shazam(f"{audiofile.tag.artist} - {audiofile.tag.title}")
                if data['tracks']['hits']:
                    track = data['tracks']['hits'][0]['track']

                    # Update the metadata fields using the information from the online database
                    try:
                        audiofile.tag.album = track['album']['title']
                        audiofile.tag.album_artist = track['artists'][0]['name']
                        audiofile.tag.track_num = track['trackPosition']
                        audiofile.tag.genre = track['sections'][0]['metadata']['genre']['name']
                        audiofile.tag.release_date = track['sections'][0]['metadata']['releaseDate']
                    except KeyError:
                        print (f"Error: {mp3_file}")

                    # Save the updated metadata to the mp3 file
                    audiofile.tag.save()
        else:
            data = search_shazam(f"{mp3_file}")
            try:
                if data['tracks']['hits']:
                    track = data['tracks']['hits'][0]['track']
            except KeyError:
                print (f"Error: {mp3_file}")

                # Update the metadata fields using the information from the
                # online database
                try:
                    audiofile.tag.album = track['album']['title']
                    audiofile.tag.album_artist = track['artists'][0]['name']
                    audiofile.tag.track_num = track['trackPosition']
                    audiofile.tag.genre = track['sections'][0]['metadata']['genre']['name']
                    audiofile.tag.release_date = track['sections'][0]['metadata']['releaseDate']
                except KeyError:
                    print (f"Error: {mp3_file}")

def add_album_art(mp3_path, image_url):
    # Download the image from the URL
    response = requests.get(image_url)
    image_data = response.content

    # Load the MP3 file
    tag = eyed3.Tag()
    tag.link(mp3_path)

    # Add the album art to the MP3 file
    tag.addImage(0x08, image_data)
    tag.update()

if __name__ == '__main__':
    main()