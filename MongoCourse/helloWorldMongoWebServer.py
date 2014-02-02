import bottle
import pymongo

#This is the handler for the default path fot the web server

@bottle.route('/')
def index():

	#Connect to mongodb
	connection = pymongo.MongoClient('localhost', 27017)

	#attach to test data base
	db = connection.test

	#get handler for names collection
	names = db.names

	#find a single document
	item = names.find_one()

	return '<b>Hello %s</b>' % item['name']

bottle.run(host='localhost', port=8082)