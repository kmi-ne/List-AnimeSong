import json
import operator

year = input('Year: ')
filename = input('File name: ')
path = f'../{year}/song/json/{filename}.json'

with open(path, 'r', encoding='utf-8')as f1:
    dict_songs: dict = json.load(f1)
    list_songs = list(dict_songs.values())
    list_songs = sorted(list_songs, key=operator.itemgetter('type'), reverse=True)
    list_songs = sorted(list_songs, key=operator.itemgetter('premiere', 'anime_title_sort'))
    dict_songs = {song['song_title'] : song for song in list_songs}
    with open(path, 'w', encoding='utf-8') as f2:
        json.dump(dict_songs, f2, ensure_ascii=False, indent=4)
