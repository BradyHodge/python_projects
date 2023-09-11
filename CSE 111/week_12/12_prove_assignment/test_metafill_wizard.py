import os
import pytest
from unittest import mock
import eyed3
from metafill_wizard import search_audioDB, search_shazam, update_metadata, add_album_art

def test_search_audioDB():
    with mock.patch('main.requests.request') as mock_request:
        mock_request.return_value.json.return_value = {'album': [{'strAlbum': 'test', 'strArtist': 'test', 'intYearReleased': '2022', 'intTrackNumber': '1', 'strGenre': 'test'}]}
        data = search_audioDB('test_artist', 'test_title')
        assert data['album'][0]['strAlbum'] == 'test'

def test_search_shazam():
    with mock.patch('main.requests.request') as mock_request:
        mock_request.return_value.json.return_value = {'tracks': {'hits': [{'track': {'album': {'title': 'test'}, 'artists': [{'name': 'test_artist'}], 'trackPosition': 1, 'sections': [{'metadata': {'genre': {'name': 'test'}, 'releaseDate': '2022'}}]}}]}}
        data = search_shazam('test')
        assert data['tracks']['hits'][0]['track']['album']['title'] == 'test'

def test_update_metadata(tmp_path):
    test_file = tmp_path / "test.mp3"
    with open(test_file, 'w') as f:
        f.write('')
    with mock.patch('main.search_audioDB') as mock_search_audioDB, \
         mock.patch('main.search_shazam') as mock_search_shazam, \
         mock.patch('main.eyed3.load') as mock_eyed3_load, \
         mock.patch('main.eyed3.Tag') as mock_eyed3_tag:
        # Test case where artist and title tags are present
        mock_eyed3_load.return_value.tag.artist = 'test_artist'
        mock_eyed3_load.return_value.tag.title = 'test_title'
        mock_search_audioDB.return_value = {'album': [{'strAlbum': 'test', 'strArtist': 'test', 'intYearReleased': '2022', 'intTrackNumber': '1', 'strGenre': 'test'}]}
        update_metadata(tmp_path)
        mock_eyed3_tag.assert_called_with()
        mock_eyed3_load.return_value.tag.save.assert_called_with()

        # Test case where artist and title tags are not present, but file name is used instead
        mock_eyed3_load.return_value.tag.artist = None
        mock_eyed3_load.return_value.tag.title = None
        mock_search_shazam.return_value = {'tracks': {'hits': [{'track': {'album': {'title': 'test'}, 'artists': [{'name': 'test_artist'}], 'trackPosition': 1, 'sections': [{'metadata': {'genre': {'name': 'test'}, 'releaseDate': '2022'}}]}}]}}
        update_metadata(tmp_path)
        mock_eyed3_tag.assert_called_with()
        mock_eyed3_load.return_value.tag.save.assert_called_with()

@pytest.fixture
def mp3_path():
    return "test.mp3"

@pytest.fixture
def image_url():
    return "https://example.com/image.jpg"

def test_add_album_art(mp3_path, image_url):
    # Create a mock response object for the requests.get function
    mock_response = mock.Mock()
    mock_response.content = b"image data"
    mock_get = mock.Mock(return_value=mock_response)

    # Patch the requests.get function to return the mock response
    with mock.patch("requests.get", mock_get):
        # Call the add_album_art function
        add_album_art(mp3_path, image_url)

    # Load the MP3 file using eyed3 and check if the album art was added
    tag = eyed3.load(mp3_path)
    assert tag.tag.images[0].image_data == b"image data"

    # Remove the test file
    os.remove(mp3_path)

pytest.main(["-v", "--tb=line", "-rN", __file__])
