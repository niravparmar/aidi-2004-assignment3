from flask_restful import Resource, reqparse
from models.student import News
import json
import datetime
import math


class Home(Resource):

    def get(self):
        try:
            return {'message': "Welcome to AIDI 2004 Assignment 3 APIs-SQL"}, 200
        except:
            return {'message': 'Error from server side'}, 500

class GetStudent(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        response = News.get_student(self)
        return {
            
            "data": response
        }, 200

class UpdateStudent(Resource):
    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument('student_id', type=int)
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        parser.add_argument('date_of_birth', type=str)
        parser.add_argument('amount_due', type=int)
        data = parser.parse_args()

        response = News.update_db(self, data['student_id'], data['first_name'], data['last_name'], data['date_of_birth'],
        data['amount_due'])


        return {
            "data": "student Data is updated",
        }, 200

class DeleteStudent(Resource):
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('student_id', type=int)
        data = parser.parse_args()

        response = News.delete_student(self, data['student_id'])


        return {
            "data": "student Data is Deleted",
        }, 200


class AddStudent(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('first_name', type=str)
    parser.add_argument('last_name', type=str)
    parser.add_argument('date_of_birth', type=str)
    parser.add_argument('amount_due', type=int)


    def post(self):
        data = AddStudent.parser.parse_args()

        if data['first_name'] and data['last_name'] and data['date_of_birth'] and data[
            'amount_due']:

            try:
                News(
                    data['first_name'], data['last_name'], data['date_of_birth'],
                    data['amount_due']
                ).save_to_db()

                return {
                           "message": "Student added"
                       }, 200

            except:
                return {
                           "meta": {
                               "statusCode": 42,
                               "messageClient": "Validation error",
                               "messageServer": "string",
                               "errorDetail": "string"
                           }
                       }, 400

        else:
            return {
                       "meta": {
                           "statusCode": 42,
                           "messageClient": "Validation error",
                           "messageServer": "string",
                           "errorDetail": "string"
                       }
                   }, 400
