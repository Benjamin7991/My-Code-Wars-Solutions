def song_decoder(song):
    new_song = song.replace('WUB', ' ')
    newest_song = new_song.split()
    newest_song = ' '.join(newest_song)
    return newest_song
