
"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favorites,Cart_Product,Orders,Transactions

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/favorites/<int:id>', methods=['GET'])
def get_single_favorite(id):

    single_favorite = Favorites.query.get(id)
    if single_favorite is None:
        raise APIException("Not favorites was Found", status_code=404)
    
    return jsonify(single_favorite.serialize()),200


@app.route('/favorites', methods=['GET'])
def get_all_favorites():

    all_favorites = Favorites.query.all()
    if all_favorites is None:
        raise APIException("Not favorites was Found", status_code=404)
    
    return jsonify([single_favorites.serialize() for single_favorites in all_favorites]),200

@app.route('/favorites', methods=['POST'])
def create_favorites():

    body = request.get_json()
    item = body["item"]
    print(body)
    if body is None:
        raise APIException("Invalid Body", status_code=400)
    new_favorites = Favorites(
        name= item["name"],
        price=item["price"],
        img=item["img"],
        continent=item["continent"],
        country=item["country"],
        description=item["description"]

    )
   
    db.session.add(new_favorites) 
    db.session.commit()
    return jsonify(new_favorites.serialize()), 200

@app.route('/favorites/<int:favorites_id>', methods=['PUT'])
def update_favorites(favorites_id): 

    body = request.get_json()
    print(body)
    if body is None:
        raise APIException("Invalid Body", status_code=400)
    favorites_1 = Favorites.query.get(favorites_id)
    favorites_1.name= body["name"]
    db.session.commit()      
    # update_item = update_item.serialize()
    return jsonify(favorites_1.serialize()),200
    

@app.route('/favorites/<int:id>', methods=['DELETE'])
def detelete_favorite(id):

    favorite = Favorites.query.get(id)
    if favorite is None:
        raise APIException('the favorite is not exist', status_code = 404) 
    db.session.delete(favorite)
    db.session.commit()
    favorites = Favorites.query.all()
    favorites = list(map(lambda x: x.serialize(), favorites))
    return jsonify(favorites), 200



@app.route('/cart_product/<int:id>', methods=['GET'])
def get_single_cart(id):

    single_cart = Cart_Product.query.get(id)
    if single_cart is None:
        raise APIException("Not cart was Found", status_code=404)
    
    return jsonify(single_cart.serialize()),200


@app.route('/cart_product', methods=['GET'])
def get_all_cart():

    all_cart_product = Cart_Product.query.all()
    if all_cart_product is None:
        raise APIException("Not favorites was Found", status_code=404)
    
    return jsonify([single_cart.serialize() for single_cart in all_cart_product]),200


@app.route('/cart_product', methods=['POST'])
def create_cart_product():

    body = request.get_json()
    item = body
    print(body)
    if body is None:
        raise APIException("Invalid Body", status_code=400)
    new_cart_product = Cart_Product(
        name= item["name"],
        price=item["price"],
        img=item["img"],
        continent=item["continent"],
        country=item["country"],
       

    )
   
    db.session.add(new_cart_product) 
    db.session.commit()
    return jsonify(new_cart_product.serialize()), 200




# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)













































# """
# This module takes care of starting the API Server, Loading the DB and Adding the endpoints
# """
# import os
# from flask import Flask, request, jsonify, url_for
# from flask_migrate import Migrate
# from flask_swagger import swagger
# from flask_cors import CORS
# from utils import APIException, generate_sitemap
# from admin import setup_admin
# from models import db, User
# #from models import Person

# app = Flask(__name__)
# app.url_map.strict_slashes = False
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# MIGRATE = Migrate(app, db)
# db.init_app(app)
# CORS(app)
# setup_admin(app)

# # Handle/serialize errors like a JSON object
# @app.errorhandler(APIException)
# def handle_invalid_usage(error):
#     return jsonify(error.to_dict()), error.status_code

# # generate sitemap with all your endpoints
# @app.route('/')
# def sitemap():
#     return generate_sitemap(app)

# @app.route('/user', methods=['GET'])
# def handle_hello():

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200

# # this only runs if `$ python src/main.py` is executed
# if __name__ == '__main__':
#     PORT = int(os.environ.get('PORT', 3000))
#     app.run(host='0.0.0.0', port=PORT, debug=False)
