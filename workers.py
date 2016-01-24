from flask.ext.rq import job
from simple_converter import simple_converter
import couchdb, json

@job
def saveJSON2DB(jsonObj):
	couch = couchdb.Server()

	key = 'g' + jsonObj.keys()[0]

	try:
		db = couch[key]
	except couchdb.http.ResourceNotFound:
		db = couch.create(key)

	db.save(jsonObj.values()[0])

def eventsJSONWithGameId(game_id):
	couch = couchdb.Server()
	key = 'g' + str(game_id)

	db = couch[key]  # will throw if not found

	jsonList = []
	for id in db:
	    jsonList.append(db[id]['Game'])

	return {"game_id":game_id, "events": jsonList}

@job
def convertXML2JSON(xmlStr):
    return simple_converter(xmlStr)

@job
def saveEventFeed(feed):
	saveJSON2DB(convertXML2JSON(feed))
