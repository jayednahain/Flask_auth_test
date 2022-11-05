from flask import Flask,request
from app import app
from user.models import User

@app.route('/user/signup',methods = ['POST'])
def signUp():
    #creating instance of user model class
    user = User()
    return user.signUp()

 