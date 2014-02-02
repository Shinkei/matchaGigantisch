
import pymongo
import datetime
import sys


# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the students database
db = connection.students
grades = db.grades

def deleteLowerHomework():

    print "deletting the homewroks"

    query = {"type":"homework"}
	#find all the students

    students = grades.find(query).sort([("student_id",pymongo.ASCENDING),("score",pymongo.ASCENDING)])
    print "students finded"
    tempId = -1
    for student in students:
    	if student["student_id"] != tempId:
    	    tempId = student["student_id"]
    	    grades.remove(student) #remove the document everytime the id chages(this means that you should only run it once)
    	    print "Student to be deleted ",student





deleteLowerHomework()