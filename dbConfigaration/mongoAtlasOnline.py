import pymongo

# connection to local host


CONNECTION_STRING = "mongodb+srv://test:test@flask-mongodb-atlas-1g8po.mongodb.net/test?retryWrites=true&w=majority"
CONNECTION_STRING= "mongodb+srv://flaskAuth:ULpUcox11b0akC7J@flask-cluster.u3hsi39.mongodb.net/?retryWrites=true&w=majority"

mongoClient = pymongo.MongoClient(CONNECTION_STRING)
db = mongoClient.flaskAuth

# localhost:27017