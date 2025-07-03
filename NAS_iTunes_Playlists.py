from libpytunes import Library
import argparse

parser = argparse.ArgumentParser(description="Generate M3U playlists from an iTunes Library XML file.")
parser.add_argument('library', nargs='?', default='./Library.xml', help='Path to the iTunes Library XML file (default: ./Library.xml)')
parser.add_argument('--src-prefix', default='D:/aniru/Music/iTunes/iTunes Media/Music/', help='Source music path prefix to replace (default: D:/aniru/Music/iTunes/iTunes Media/Music/)')
parser.add_argument('--dst-prefix', default='/media/music/music/', help='Destination music path prefix (default: /media/music/music/)')
args = parser.parse_args()

l = Library(args.library)

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
        songpath = songpath.replace(args.src_prefix, args.dst_prefix)
        #f.write("# " + song.name + "\n")
        f.write(songpath + "\n")
    f.close

#for song in l.getPlaylist(playlists[0]).tracks:
#	print("[{t}] {a} - {n}".format(t=song.track_number, a=song.artist, n=song.name))
