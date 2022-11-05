from flask import Flask
from flask import jsonify
import pymongo

app = Flask(__name__)
#import routes from user
from user import routes


# connectionString = "mongodb+srv://flaskAuth:<flask12345>@flask-cluster.u3hsi39.mongodb.net/?retryWrites=true&w=majority"
# client = pymongo.MongoClient(connectionString)
# dataBase = client.get_database('flaskDataBase')
# userCollection = pymongo.collection.Collection(dataBase, 'flaskTest')





@app.route('/')
def homePage():
   
    return jsonify("hellow jayed")



if __name__ == "__main__":
    app.run(debug=True)
