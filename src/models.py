from flask_sqlalchemy import SQLAlchemy
from datetime import timezone,datetime 

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "password": self.password,
            # do not serialize the password, its a security breach
        }
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.String(120), unique=False, nullable=False)
    img = db.Column(db.String(500), unique=True, nullable=False)
    continent = db.Column(db.String(120), unique=False, nullable=False)
    country = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=False)
    

    def __repr__(self):
        return '<Favorites %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "img": self.img,
            "continent": self.continent,
            "country": self.country,
            "description": self.description
            # do not serialize the password, its a security breach
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    price = db.Column(db.String(120), unique=False, nullable=False)
    img = db.Column(db.String(500), unique=False, nullable=False)
    continent = db.Column(db.String(120), unique=False, nullable=False)
    country = db.Column(db.String(120), unique=False, nullable=False)
    


    def __repr__(self):
        return '<Product %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "img": self.img,
            "continent": self.continent
            # do not serialize the password, its a security breach
        }

class Cart_Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    price = db.Column(db.String(120), unique=False, nullable=False)
    img = db.Column(db.String(500), unique=False, nullable=False)
    continent = db.Column(db.String(120), unique=False, nullable=False)
    country = db.Column(db.String(120), unique=False, nullable=False)
    


    def __repr__(self):
        return '<Cart_Product %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "img": self.img,
            "continent": self.continent
            # do not serialize the password, its a security breach
        }

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.String(120), unique=True, nullable=False)
    continent = db.Column(db.String(120), unique=True, nullable=False)
    quantity = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, default = datetime.utcnow, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<Orders %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
             "price": self.price,
             "continent": self.continent,
             "quantity": self.quantity,
             "date": self.date,
            # do not serialize the password, its a security breach
        }
class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.String(120), unique=True, nullable=False)
    transaction_id = db.Column(db.String(120), unique=True, nullable=False)
    quantity = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, default = datetime.utcnow, nullable=False)
    # i need to change card number////
    card_number = db.Column(db.DateTime, default = datetime.utcnow, nullable=False) 
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<Orders %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
             "price": self.price,
             "transaction_id": self.transaction_id,
             "quantity": self.quantity,
             "date": self.date,
             "card_number": self.card_number,
            # do not serialize the password, its a security breach
        }

