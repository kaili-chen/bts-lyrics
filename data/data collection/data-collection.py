import os
import re
import csv

from ALBUMS import ALBUMS
from genius import get_lyrics, get_album_tracks


retry = []

print('retrieving album tracks...')
for album in ALBUMS:
    album_title = album['name']
    album_tracks = get_album_tracks(album['eng_url'])

    for track in album_tracks:
        # clear out initial 'BTS - '
        track_title = track['title'][6:]
        # remove trailing english translation indicator
        track_title = re.sub(r'\(English Translation\)', '', track_title)
        # print('\t', track_title)

        retry.append({'track_title': track_title, 'url': track['link'], 'album_title': album_title, 'album_rd': album['release_date']})

print('retrieving lyrics for', len(retry), 'tracks...')
track_lyrics = []
while len(retry) > 0:
    for r in retry:
        lyrics_dict = get_lyrics(r['url'])

        if lyrics_dict is None:
            print('failed:', r['track_title'])
            continue

        lyrics = lyrics_dict['lyrics']
        track_lyrics.append({
            'album_title': r['album_title'],
            'album_rd': r['album_rd'],
            'track_title': r['track_title'],
            'lyrics': lyrics.strip()
        })
        retry.remove(r)
        print('\tremaining:', len(retry))

print('writing to file...')
f = open('lyrics.csv', 'w',  encoding="utf-8")
with f:
    fnames = ['album_title', 'album_rd', 'track_title', 'lyrics']
    writer = csv.DictWriter(f, fieldnames=fnames)

    writer.writeheader()
    for row in track_lyrics:
        writer.writerow(row)
        # writer.writerow({'first_name' : 'Robert', 'last_name': 'Brown'})
        # writer.writerow({'first_name' : 'Julia', 'last_name': 'Griffin'})

f.close()
print('done')
# URL = 'https://genius.com/Bts-intro-2-cool-4-skool-lyrics'
# lyrics = get_lyrics(URL)
# print(lyrics)
#
# if lyrics is not None:
#     file = open(os.path.join('lyrics', '2 cool 4 skool', re.sub(r'[^\w\s]', '', lyrics['title'])+'.txt').lower(), 'w')
#     file.write(lyrics['lyrics'])

# album_url = 'https://genius.com/albums/Bts/2-cool-4-skool'
# print(get_album_tracks(album_url))


# for kr, er in zip(kor_rows, eng_rows):
#     kor_song_url = kr.find('a')['href']
#     eng_song_url = er.find('a')['href']
#
#     kor_chart_row = kr.find('h3', class_='chart_row-content-title')
#     kor_chart_row.find('span').decompose()
#     kor_song_title = kor_chart_row.text.strip()
#
#     eng_chart_row = er.find('h3', class_='chart_row-content-title')
#     eng_chart_row.find('span').decompose()
#     eng_song_title = eng_chart_row.text.strip()
#
#     print(kor_song_title, '---', eng_song_title)
