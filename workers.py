from flask.ext.rq import job
from converter import converter
import couchdb, json

@job
def saveJSON2DB(jsonStr):
	#how to I access the database???
	couch = couchdb.Server()

	jsonObj = json.loads(jsonStr)

    ##Because couchdb require that the name of a database to begin with letter
	key = 'g' + jsonObj.keys()[0]

	##test if the database with game_id exist
	try:
		#could raise ResourceNotFound error
		db = couch[key]
	except couchdb.http.ResourceNotFound:
		#if doesn't exist, create a new database
		db = couch.create(key)

	db.save(jsonObj.values()[0])

def eventsJSONWithGameId(game_id):
	couch = couchdb.Server()
	key = 'g' + game_id

	db = couch[key]  # will throw if not found

	jsonList = []
	for id in db:
	    jsonList.append(db[id]['Game'])

	return {"game_id":game_id, "events": jsonList}

@job
def convertXML2JSON(xmlStr):
    return converter(xmlStr)

@job
def saveEventFeed(feed):
	saveJSON2DB(convertXML2JSON(feed))
