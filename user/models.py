from flask import Flask,jsonify,request
import uuid

from passlib.hash import pbkdf2_sha256 as enPass
import pymongo
from dbConfigaration.mongoConnection import db



# mongoClient = pymongo.MongoClient('localhost',27017)
# db = mongoClient.AttendenceSystemDB

# connectionString = "mongodb+srv://flaskAuth:<flask12345>@flask-cluster.u3hsi39.mongodb.net/?retryWrites=true&w=majority"
# client = pymongo.MongoClient(connectionString)
# dataBase = client.get_database('flaskDataBase')
# userCollection = pymongo.collection.Collection(dataBase, 'flaskTest')
# from dbConfigaration.mongoConnection import db

class User:

    def signUp(self):
        #create object which represents use
        print("pellaow")
        userData = request.get_json()
        user = {
            "_id":uuid.uuid4().hex,
            "name":userData['name'],
            "password":userData['password'],
            "officeId":userData['officeId'],
            "email":userData['email'],
        }
        

        #encrypt password
        user['password'] = enPass.encrypt(user['password'])
        # dataBase.flaskDataBase.insert_one(user)

        


        db.AttendenceSystemCollection.insert_one(user)
        

        return jsonify(user),200