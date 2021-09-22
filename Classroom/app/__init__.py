# app/__init__.py

# local imports
from config import app_config

# third-party imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import ast


class Users(Resource):
    def __init__(self):
        self.is_instructor = False

    def isInstructor(self):
        return self.is_instructor

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)

        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        if args['userId'] in list(data['userId']):
            return {
                'message': f"'{args['userId']}' already exists."
            }, 401  # 409

        else:
            new_data = pd.DataFrame({
                'userId': [args['userId']],
                'name': [args['name']],
                'city': [args['city']],
                'locations': [[]]
            })

            data = data.append(new_data, ignore_index=True)
            data.to_csv('users.csv', index=False)
            return {'data': data.to_dict()}, 200

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True)
        parser.add_argument('location', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        if args['userId'] in list(data['userId']):
            data['locations'] = data['locations'].apply(
                lambda x: ast.literal_eval(x)
            )

            user_data = data[data['userId'] == args['userId']]
            user_data['locations'] = user_data['locations'].values[0].append(args['location'])

            data.to_csv('users.csv', index=False)
            return {'data': data.to_dict()}, 200

        else:
            return {
                'message': f"'{args['userId']}' user not found."
            }, 404

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True)
        args = parser.parse_args()

        data = pd.read_csv('users.csv')

        if args['userId'] in list(data['userId']):
            data = data[data['userId'] != args['userId']]
            data.to_csv('users.csv', index=False)
            return {'data': data.to_dict()}, 200

        else:
            return {
                'message': f"'{args['userId']}' user not found."
            }, 404


class Instructors(Users):
    def __init__(self):
        Users.__init__(self)
        self.is_instructor = True
        self.data = pd.read_csv('app/data/instructors.csv')

    def get(self):
        return {'data': self.data.to_dict()}, 200


class Students(Users):
    def __init__(self):
        Users.__init__(self)
        self.data = pd.read_csv('app/data/students.csv')

    def get(self):
        return {'data': self.data.to_dict()}, 200


class Subjects(Resource):
    def __init__(self):
        self.data = pd.read_csv('app/data/subjects.csv')

    def get(self):
        return {'data': self.data.to_dict()}, 200


class Courses(Resource):
    def __init__(self):
        self.data = pd.read_csv('app/data/courses.csv')

    def get(self):
        return {'data': self.data.to_dict()}, 200


class Lessons(Resource):
    def __init__(self):
        self.data = pd.read_csv('app/data/lessons.csv')

    def get(self):
        return {'data': self.data.to_dict()}, 200


class Videos(Resource):
    def __init__(self):
        self.link = ''
        self.data = pd.read_csv('app/data/videos.csv')

    def get(self):
        return {'data': self.data.to_dict()}, 200


class Tags(Resource):
    def __init__(self):
        self.data = pd.read_csv('app/data/tags.csv')

    def get(self):
        return {'data': self.data.to_dict()}, 200


class Locations(Resource):
    def get(self):
        data = pd.read_csv('locations.csv')
        return {'data': data.to_dict()}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('locationId', required=True, type=int)
        parser.add_argument('name', required=True)
        parser.add_argument('rating', required=True, type=float)
        args = parser.parse_args()

        data = pd.read_csv('locations.csv')

        if args['locationId'] in list(data['locationId']):
            return {
                'message': f"'{args['locationId']}' already exists."
            }, 401  # 409

        else:
            new_data = pd.DataFrame({
                'locationId': [args['locationId']],
                'name': [args['name']],
                'rating': [args['rating']]
            })

            data = data.append(new_data, ignore_index=True)
            data.to_csv('locations.csv', index=False)
            return {'data': data.to_dict()}, 200

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument('locationId', required=True, type=int)
        parser.add_argument('name', store_missing=False)
        parser.add_argument('rating', store_missing=False, type=float)
        args = parser.parse_args()

        data = pd.read_csv('locations.csv')

        if args['locationId'] in list(data['locationId']):
            user_data = data[data['locationId'] == args['locationId']]

            if 'name' in args:
                user_data['name'] = args['name']
            if 'rating' in args:
                user_data['rating'] = args['rating']

            data[data['locationId'] == args['locationId']] = user_data
            data.to_csv('locations.csv', index=False)
            return {'data': data.to_dict()}, 200

        else:
            return {
                'message': f"'{args['locationId']}' location does not exist."
            }, 404

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('locationId', required=True, type=int)
        args = parser.parse_args()

        data = pd.read_csv('locations.csv')

        if args['locationId'] in list(data['locationId']):
            data = data[data['locationId'] != args['locationId']]
            data.to_csv('locations.csv', index=False)
            return {'data': data.to_dict()}, 200

        else:
            return {
                'message': f"'{args['locationId']}' location does not exist."
            }, 404


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)

    api = Api(app)
    api.add_resource(Instructors, '/instructors')
    api.add_resource(Students, '/students')
    api.add_resource(Subjects, '/subjects')
    api.add_resource(Courses, '/courses')
    api.add_resource(Lessons, '/lessons')
    api.add_resource(Videos, '/videos')
    api.add_resource(Tags, '/tags')

    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
