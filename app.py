from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'products.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Product(db.Model):
    __tablenme__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    price = db.Column(db.Float)
    quantity = db.Column(db.Float)

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price', 'quantity')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@app.route('/', methods=['POST'])
def add_product():
    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']
    product = Product(name=name, price=price, quantity=quantity)
    db.session.add(product)
    db.session.commit()
    return product_schema.jsonify(product)


@app.route('/', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    result = products_schema.dump(products)
    return jsonify(result)


@app.route('/<id>', methods=['GET'])
def get_product_by_id(id):
    product = Product.query.get(id)
    if product:
        return product_schema.jsonify(product)
    else:
        return {'id': 'incorrect id'}


@app.route('/<id>', methods=['PUT'])
def change_product_info(id):
    product = Product.query.get(id)
    if product:
        product.name = request.json['name']
        product.price = request.json['price']
        product.quantity = request.json['quantity']
        db.session.commit()
        return product_schema.jsonify(product)
    else:
        return {'id': 'incorrect id'}


@app.route('/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return product_schema.jsonify(product)
    else:
        return {'id': 'incorrect id'}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()



