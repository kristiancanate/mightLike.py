# Algorithum for SL

def formatMusic(fileName):
    songLib = open(fileName,"r")
    songLib_data = []
    for line in songLib:
        number_songs = line.split("\t")
        songs = [n for n in number_songs]
        songLib_data.append(songs)
    for song in songLib_data:
        song[16] = (song[16][:1])
    songLib_data_tuple = tuple(songLib_data)
    return songLib_data_tuple

songList = formatMusic("songLib.tsv")
print(songList)

#if SongLGen == uGen:
    #print()
#else:
 #   print()
