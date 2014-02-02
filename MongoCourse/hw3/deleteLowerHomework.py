import pymongo

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db = connection.school
studentsCollection = db.students


def deleteLowerHomework():
    print
    "deletting the homewroks"


    students = studentsCollection.find({})

    for student in students:
        scores = student['scores']

        lowerHomework = 999.9
        position = 100
        pos = -1
        for score in scores:
            pos += 1
            if score['type'] == 'homework':
                if lowerHomework > score['score']:
                    lowerHomework = score['score']
                    position =pos
        #set query to the lowest homework

        scores.pop(position)

        studentsCollection.update({'_id':student['_id']},student,safe=True)

        print "student: %s, score: %i" % (student['_id'], lowerHomework)
        print student



deleteLowerHomework()