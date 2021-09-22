# https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f
# https://gist.github.com/jamescalam/0b309d275999f9df26fa063602753f73

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv')
        return {'data': data.to_dict()}, 200

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


api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')


if __name__ == '__main__':
    app.run()
