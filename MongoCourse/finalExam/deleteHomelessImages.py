
import pymongo
import datetime
import sys


# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the students database
db = connection.photography
albums = db.albums
images = db.images

def deleteHuerphanImages():

    print "deletting the images"

    query = {}
	#find all the images

    images_list = images.find(query).sort([("_id",pymongo.ASCENDING)])
    print images_list.count()
    temp = 0

    for image in images_list:

        id_imagen = image['_id']
        query2 = {'images': id_imagen}
        album = albums.find(query2)

        if album.count() == 0:
            temp += 1
            images.remove(image)
    print temp
    	#if student["student_id"] != tempId:
    	#    tempId = student["student_id"]
    	#    grades.remove(student) #remove the document everytime the id chages(this means that you should only run it once)
    	#    print "Student to be deleted ",student





deleteHuerphanImages()