from db import db

class storeModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    #items shi modis iseti elementebi romlebshic stores.id == items.store_id
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod #find daba base in table items username
    def find_by_username(cls, name):
        return cls.query.filter_by(name=name).first()

    #insert data base new item in items
    def save_to_db(self):
        db.session.add(self) # tu aseti momxmarebeli arsebobs ubralod ganaaxlebs mas.
        db.session.commit()

     #update items in data base
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()