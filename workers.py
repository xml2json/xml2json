from flask.ext.rq import job
import couchdb
import json

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

    print("Implemented! saveJSON2DB")

@job
def returnJSON2Clint(game_id):
	couch = couchdb.Server()
	key = 'g' + str(aame_id)

	try:
	    db = couch[key]
	except couchdb.http.ResourceNotFound:
		return "Game not Found"

	jsonList = []
	for id in db:
	    jsonList.append(db[id]['Game'])

	return jsonList

@job
def convertXML2JSON(xmlStr):
    return converter(xmlStr)

@job
def sleepForThreeSeconds():
    import time
    time.sleep(3)
    with open('temp.txt', 'a') as file:
        file.write("Done sleeping for 3 seconds!\n")
