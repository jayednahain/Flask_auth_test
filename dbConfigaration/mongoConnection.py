import pymongo

# connection to local host
mongoClient = pymongo.MongoClient('localhost',27017)
db = mongoClient.AttendenceSystemDB

# localhost:27017