import pymongo

mongoClient = pymongo.MongoClient('localhost',27017)
db = mongoClient.AttendenceSystemDB

# localhost:27017