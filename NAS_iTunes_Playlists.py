from libpytunes import Library

l = Library("./Library.xml")

#for id, song in l.songs.items():
#    if song and song.rating:
#        if song.rating > 80:
#            print(song.name, song.rating)

playlists=l.getPlaylistNames()

#print(playlists)

for playlist in playlists:
    print("Now processing: " + playlist)
    filename="./playlists/" + playlist + ".m3u"
    f = open(filename, "w")
    for song in l.getPlaylist(playlist).tracks:
        #print("[{t}] {a} - {n}".format(t=song.track_number, a=song.artist, n=song.name))
        songpath = song.location
        songpath = songpath.replace("\\", "/")
        songpath = songpath.replace("D:/aniru/Music/iTunes/iTunes Media/Music/", "/media/music/music/")
        #f.write("# " + song.name + "\n")
        f.write(songpath + "\n")
    f.close

#for song in l.getPlaylist(playlists[0]).tracks:
#	print("[{t}] {a} - {n}".format(t=song.track_number, a=song.artist, n=song.name))
