import os
import requests
import musicbrainzngs
from mutagen.easyid3 import EasyID3

musicbrainzngs.set_useragent("python-musicbrainzngs-example", "0.1", "https://github.com/alastair/python-musicbrainzngs/")

def get_metadata(file_path):
    audio = EasyID3(file_path)
    if 'title' not in audio:
        song_name = os.path.basename(file_path).split('.')[0]
        audio['title'] = song_name
    if 'artist' not in audio:
        audio['artist'] = 'Unknown'
    if 'album' not in audio:
        song_name = os.path.basename(file_path).split('.')[0]
        result = musicbrainzngs.search_recordings(song_name)
        if 'recording-list' in result:
            recording = result['recording-list'][0]
            if 'artist-credit' in recording:
                audio['artist'] = recording['artist-credit'][0]['artist']['name']
            if 'title' in recording:
                audio['title'] = recording['title']
            if 'release-list' in recording:
                release_id = recording['release-list'][0]['id']
                release = musicbrainzngs.get_release_by_id(release_id, includes=['artists', 'recordings'])
                if 'release' in release:
                    release = release['release']
                    if 'title' in release:
                        audio['album'] = release['title']
    audio.save()

def main():
    folder_path = input("Enter the folder path: ")
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.mp3'):
            file_path = os.path.join(folder_path, file_name)
            get_metadata(file_path)

if __name__ == '__main__':
    main()