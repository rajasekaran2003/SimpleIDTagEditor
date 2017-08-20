import os
import sys
from mutagen.easyid3 import EasyID3
import eyed3

def walk_through_files(dir):
	for root, dirs, files in os.walk(dir):
		for name in files:
			songName = os.path.join(root, name)
			artist,album,title = songName.split("\\")
			# if your folder structure is just Artist and Song
			#artist,title = songName.split("\\")
			modifyIDVtagV1(artist, album, title, songName)
			modifyIDVtagV2(artist, album, title, songName)

def modifyIDVtagV1(artist, album, title, songName):
	file = EasyID3(songName)
	file['title'] = str(title)
	file['artist'] = str(artist)
	file['album'] = str(album)
	file['composer'] = str(artist)
	file.save()
	print(songName)

def modifyIDVtagV2(artist, album, title, songName):
	audiofile = eyed3.load(songName)
	audiofile.tag.artist = str(artist)
	audiofile.tag.album = str(album)
	audiofile.tag.album_artist = str(artist)
	audiofile.tag.title = str(title)
	audiofile.tag.save()
	print(songName)
	
walk_through_files(sys.argv[1])