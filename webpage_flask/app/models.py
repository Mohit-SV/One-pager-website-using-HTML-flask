from app import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_title = db.Column(db.String(140))
    image_url = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    description = db.Column(db.String(250))

    def __repr__(self):
        return '<Product {}>'.format(self.product_title)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    mobile = db.Column(db.Integer, index=True)
    message = db.Column(db.String(250), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)