from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = 'mongodb://root:pass@mongodb:27017/mongo_database'
mongo = PyMongo(app)
db = mongo.db

class Index(Resource):
    def get(self):
        return jsonify({"message": "Hello, User!"})

class MongoTableResource(Resource):    
    # Query all documents from the collection
    def get(self):
        _objects = db.mongo_table.find()        
        item = {}
        data = []
        for object in _objects:
            item = {
                '_id': str(object['_id']),
                'id': str(object['id']),
                'name': object['name'],
                'type': object['type'],
                'value': str(object['value'])
            }
            data.append(item)        
        
        return jsonify(status=True, data=data)

    # Post a new document
    def post(self):
        new_object = request.get_json()
        db.mongo_table.insert_one(new_object)
        
        return jsonify(status=True, message='Object added successfully')

    # Update a document
    def put(self):
        object_id = request.args.get('id')
        
        # Check if there is a valid argument
        if not object_id:
            return {'status': False, 'message': 'Object ID is required for updating'}, 400

        # Check if the document with the given ID exists
        existing_object = db.mongo_table.find_one({"id": int(object_id)})
        if existing_object is None:
            return {'status': False, 'message': 'Object not found with the provided ID'}, 404

        # Update the document
        updated_object = request.get_json()
        db.mongo_table.update_one({"id": int(object_id)}, {'$set': updated_object})
        return {'status': True, 'message': 'Object updated successfully'}, 200

api.add_resource(MongoTableResource, '/api/mongo_table')
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) # Don't forget to turn debug off on release