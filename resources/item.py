from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store id."
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_username(name) #abrunebs obieqts
        if item:
            return item.json()
        else:
            return {'massage': "item not found"}, 404

    # add data base new itme
    def post(self, name):
        if ItemModel.find_by_username(name):
            return {'massage': f"the {name} is already exist"}

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])# vqmni axal obieqts
        try:
            item.save_to_db()
        except:
            return {"massage": "An error occurred insert item in items "}, 500  # internet server problem

        return item.json(), 201

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_username(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.save_to_db()
        return item.json()

    def delete(self, name):
        item = ItemModel.find_by_username(name)
        if item:
            item.delete_from_db()

        return {'massagae': 'item deleted'}


class ItemList(Resource):
    def get(self):
       return {'items': [x.json() for x in ItemModel.query.all()]}
