'''
Contains methods to assist in extracting lyrics from genius.com.

Functions:
    get_album_tracks(string) --> list object
    get_lyrics(string) --> dictionary object

Last updated 23 July 2020, 9:43 PM
'''

import requests
from bs4 import BeautifulSoup
import json
import datetime
import re

if __name__ == '__main__':
    pass


def get_album_tracks(url):
    '''
    Returns a list of tracks and from an album url from genius.com.

    Parameters:
        url (string) : genius.com url for the album

    Returns:
        tracks (list) : list of tracks extracted from url
    '''
    page = requests.get(url)
    if (page.status_code != 200):
        print(page.status_code)

    soup = BeautifulSoup(page.content, 'html.parser')
    chart_rows = soup.find_all('div', class_='chart_row-content')

    tracks = []
    for row in chart_rows:
        link = row.find('a')['href']

        track = row.find('h3', class_='chart_row-content-title')
        track.find('span').decompose()
        track_title = track.text.strip()

        tracks.append({
            'title': track_title,
            'link': link
        })

    return tracks


def get_lyrics(url):
    '''
    Returns a dictionary with a track's lyrics and from a track url from genius.com.

    Parameters:
        url (string) : genius.com url for the track

    Returns:
        lyrics (dictionary) : contains track's lyrics and title
    '''
    page = requests.get(url)
    if (page.status_code != 200):
        print(page.status_code)

    soup = BeautifulSoup(page.content, 'html.parser')

    h1 = soup.find('h1')
    if h1 is not None:
        song_title = h1.text.strip()
    else:
        # if no song title retrieved, use untitled with datetime
        song_title = 'untitled' + datetime.datetime.now().replace(microsecond=0).isoformat().replace(':', '')

    lyrics_div = soup.find('div', class_='lyrics')
    for fail_count in range(0, 5):
        if lyrics_div is not None:
            break;

        lyrics_div = soup.find('div', class_='lyrics')

        if fail_count == 4 and lyrics_div is None:
            print('last retry failed, exiting')
            return None

        print(fail_count, "no lyrics found, retrying...")

    lyrics = lyrics_div.text.strip()

    return { 'title': song_title, 'lyrics': lyrics }
