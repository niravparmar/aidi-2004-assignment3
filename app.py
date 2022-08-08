from flask import Flask, request, render_template, jsonify
from flask_restful import Api
from resources.student import Home, AddStudent, GetStudent, UpdateStudent, DeleteStudent
from db import db

import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://QX3sGZ1TVj:ofZiwKGAwS@remotemysql.com:3306/QX3sGZ1TVj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

db.init_app(app)

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Home, '/')
api.add_resource(AddStudent, '/student/addstudent')
api.add_resource(UpdateStudent, '/student/updatestudent')
api.add_resource(GetStudent, '/student/getstudent')
api.add_resource(DeleteStudent, '/student/deletestudent')

app.run(port=5000, debug=True)
