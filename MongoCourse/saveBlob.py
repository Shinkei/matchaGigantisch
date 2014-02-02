import pymongo
import gridfs
import sys

#stablish a connection to he database
connection = pymongo.Connection('mongodb://localhost', safe=True)

#get a handle to the school database
db = connection.test
videos_meta = db.videos_meta

def main():
	grid = gridfs.GridFS(db, 'videos')
	fin = open('video.mp4', 'r')

	_id = grid.put(fin)
	fin.close()

	print "id of files is", _id

	videos_meta.insert({'gris_id':_id, 'filename':'video.mp4'})


main()