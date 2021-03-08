from flask_restful import Resource
from models.store import storeModel

class store(Resource):
    def get(self, name):
        store = storeModel.find_by_username(name)
        if store:
            return store.json()
        return {'massage': 'Store not found'}, 404

    def post(self, name):
        if storeModel.find_by_username(name):
            return {'massage': "A store with name '{}' already exists.".format(name)}, 400
        store = storeModel(name)
        try:
            store.save_to_db()
        except:
            return {'massage': 'An error occurred while creating the store.'}, 500
        return store.json(), 201

    def delete(self, name):
        store = storeModel.find_by_username(name)
        if store:
            store.delete_from_db()
        return {'massage': 'store is deleted'}


class storelist(Resource):
    def get(self):
        return {'stores': [store.json() for store in storeModel.query.all()]}