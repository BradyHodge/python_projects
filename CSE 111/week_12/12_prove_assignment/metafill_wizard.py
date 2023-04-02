"""
Made by Brady Hodge
CSE 111
"""

import os
import eyed3
import requests

API_key = input("Enter your API key: ")

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

"""

search_shazam returns this:
{"tracks":{"hits":[{"track":{"layout":"5","type":"MUSIC","key":"548030459","title":"Christmas Saves The Year","subtitle":"twenty one pilots","share":{"subject":"Christmas Saves The Year - twenty one pilots","text":"I used Shazam to discover Christmas Saves The Year by twenty one pilots.","href":"https://www.shazam.com/track/548030459/christmas-saves-the-year","image":"https://is3-ssl.mzstatic.com/image/thumb/Music124/v4/52/64/d0/5264d066-236f-1079-3135-e6a610411c2a/075679794536.jpg/400x400cc.jpg","twitter":"I used @Shazam to discover Christmas Saves The Year by twenty one pilots.","html":"https://www.shazam.com/snippets/email-share/548030459?lang=en-US&country=US","avatar":"https://is3-ssl.mzstatic.com/image/thumb/Music126/v4/ee/a5/67/eea567e6-e0a7-6ec0-e564-cb2bedf11608/pr_source.png/800x800cc.jpg","snapchat":"https://www.shazam.com/partner/sc/track/548030459"},"images":{"background":"https://is3-ssl.mzstatic.com/image/thumb/Music126/v4/ee/a5/67/eea567e6-e0a7-6ec0-e564-cb2bedf11608/pr_source.png/800x800cc.jpg","coverart":"https://is3-ssl.mzstatic.com/image/thumb/Music124/v4/52/64/d0/5264d066-236f-1079-3135-e6a610411c2a/075679794536.jpg/400x400cc.jpg","coverarthq":"https://is3-ssl.mzstatic.com/image/thumb/Music124/v4/52/64/d0/5264d066-236f-1079-3135-e6a610411c2a/075679794536.jpg/400x400cc.jpg","joecolor":"b:983f35p:fbf7e6s:f6ede8t:e7d3c3q:e3cac4"},"hub":{"type":"APPLEMUSIC","image":"https://images.shazam.com/static/icons/hub/ios/v5/applemusic_{scalefactor}.png","actions":[{"name":"apple","type":"applemusicplay","id":"1543103936"},{"name":"apple","type":"uri","uri":"https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/65/47/cb/6547cbe8-c01f-ab52-033a-2aab579a139c/mzaf_12691946955685157523.plus.aac.ep.m4a"}],"options":[{"caption":"OPEN","actions":[{"name":"hub:applemusic:deeplink","type":"applemusicopen","uri":"https://music.apple.com/us/album/christmas-saves-the-year/1543103935?i=1543103936&mttnagencyid=s2n&mttnsiteid=125115&mttn3pid=Apple-Shazam&mttnsub1=Shazam_ios&mttnsub2=5348615A-616D-3235-3830-44754D6D5973&itscg=30201&app=music&itsct=Shazam_ios"},{"name":"hub:applemusic:deeplink","type":"uri","uri":"https://music.apple.com/us/album/christmas-saves-the-year/1543103935?i=1543103936&mttnagencyid=s2n&mttnsiteid=125115&mttn3pid=Apple-Shazam&mttnsub1=Shazam_ios&mttnsub2=5348615A-616D-3235-3830-44754D6D5973&itscg=30201&app=music&itsct=Shazam_ios"}],"beacondata":{"type":"open","providername":"applemusic"},"image":"https://images.shazam.com/static/icons/hub/ios/v5/overflow-open-option_{scalefactor}.png","type":"open","listcaption":"Open in Apple Music","overflowimage":"https://images.shazam.com/static/icons/hub/ios/v5/applemusic-overflow_{scalefactor}.png","colouroverflowimage":false,"providername":"applemusic"},{"caption":"BUY","actions":[{"type":"uri","uri":"https://itunes.apple.com/us/album/christmas-saves-the-year/1543103935?i=1543103936&mttnagencyid=s2n&mttnsiteid=125115&mttn3pid=Apple-Shazam&mttnsub1=Shazam_ios&mttnsub2=5348615A-616D-3235-3830-44754D6D5973&itscg=30201&app=itunes&itsct=Shazam_ios"}],"beacondata":{"type":"buy","providername":"itunes"},"image":"https://images.shazam.com/static/icons/hub/ios/v5/itunes-overflow-buy_{scalefactor}.png","type":"buy","listcaption":"Buy on iTunes","overflowimage":"https://images.shazam.com/static/icons/hub/ios/v5/itunes-overflow-buy_{scalefactor}.png","colouroverflowimage":false,"providername":"itunes"}],"providers":[{"caption":"Open in Spotify","images":{"overflow":"https://images.shazam.com/static/icons/hub/ios/v5/spotify-overflow_{scalefactor}.png","default":"https://images.shazam.com/static/icons/hub/ios/v5/spotify_{scalefactor}.png"},"actions":[{"name":"hub:spotify:searchdeeplink","type":"uri","uri":"spotify:search:Christmas%20Saves%20The%20Year%20twenty%20one%20pilots"}],"type":"SPOTIFY"},{"caption":"Open in Deezer","images":{"overflow":"https://images.shazam.com/static/icons/hub/ios/v5/deezer-overflow_{scalefactor}.png","default":"https://images.shazam.com/static/icons/hub/ios/v5/deezer_{scalefactor}.png"},"actions":[{"name":"hub:deezer:searchdeeplink","type":"uri","uri":"deezer-query://www.deezer.com/play?query=%7Btrack%3A%27Christmas+Saves+The+Year%27%20artist%3A%27twenty+one+pilots%27%7D"}],"type":"DEEZER"}],"explicit":false,"displayname":"APPLE MUSIC"},"artists":[{"id":"42","adamid":"349736311"}],"url":"https://www.shazam.com/track/548030459/christmas-saves-the-year"}}]},"artists":{"hits":[{"artist":{"avatar":"https://is1-ssl.mzstatic.com/image/thumb/Music126/v4/ee/a5/67/eea567e6-e0a7-6ec0-e564-cb2bedf11608/pr_source.png/800x800bb.jpg","name":"twenty one pilots","verified":false,"weburl":"https://music.apple.com/us/artist/twenty-one-pilots/349736311","adamid":"349736311"}}]}}
"""

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
                audiofile.tag.album = track['strAlbum']
                audiofile.tag.album_artist = track['strArtist']
                audiofile.tag.track_num = track['intTrackNumber']
                audiofile.tag.genre = track['strGenre']
                audiofile.tag.release_date = track['intYearReleased']

                # Save the updated metadata to the mp3 file
                audiofile.tag.save()
            else:
                data = search_shazam(f"{audiofile.tag.artist} - {audiofile.tag.title}")
                if data['tracks']['hits']:
                    track = data['tracks']['hits'][0]['track']

                    # Update the metadata fields using the information from the online database
                    audiofile.tag.album = track['album']['title']
                    audiofile.tag.album_artist = track['artists'][0]['name']
                    audiofile.tag.track_num = track['trackPosition']
                    audiofile.tag.genre = track['sections'][0]['metadata']['genre']['name']
                    audiofile.tag.release_date = track['sections'][0]['metadata']['releaseDate']

                    # Save the updated metadata to the mp3 file
                    audiofile.tag.save()
        else:
            data = search_shazam(f"{mp3_file}")
            if data['tracks']['hits']:
                track = data['tracks']['hits'][0]['track']

                # Update the metadata fields using the information from the
                # online database
                audiofile.tag.album = track['album']['title']
                audiofile.tag.album_artist = track['artists'][0]['name']
                audiofile.tag.track_num = track['trackPosition']
                audiofile.tag.genre = track['sections'][0]['metadata']['genre']['name']
                audiofile.tag.release_date = track['sections'][0]['metadata']['releaseDate']

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