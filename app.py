import os
import markdown
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api, abort, reqparse
from config.Config import Development

app = Flask(__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

# Import Models and Schema
from models.Products import * 

@app.before_first_request
def create_tables():
    # db.drop_all()
    db.create_all() 


@app.route('/')
def index():
    with open(os.path.dirname(app.root_path)+ '/products-api/README.md','r') as markdown_file:
        
        content = markdown_file.read()

        return markdown.markdown(content) 


class ProductList(Resource):
    def get(self):
        productsObj = ProductsModel.query.all()
        result = products_schema.dump(productsObj)
        
        return jsonify(result)
    
    def post(self):
        name = request.json['name'].capitalize()
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']


        if ProductsModel.query.filter_by(name = name).first():
            return make_response(jsonify({ 'error': 'Product already exists' }), 400)

        new_product = ProductsModel(name, description, price, qty)

        new_product.add_product()

        return product_schema.jsonify(new_product)


class Products(Resource):
    def get(self, identifier):
        product = ProductsModel.query.get(identifier)
        if product == None:
            return make_response(jsonify({ 'error': f'Product with the id of {identifier} does not exist' }), 400)
     
        return product_schema.jsonify(product)
    
    def put(self, identifier):
        product = ProductsModel.query.get(identifier)
        if product == None:
            return make_response(jsonify({ 'error': f'Product with the id of {identifier} does not exist' }), 400)

        name = request.json['name'].capitalize()
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']

        if ProductsModel.query.filter_by(name = name).first():
            return make_response(jsonify({ 'error': 'Product already exists' }), 400)

        upd_product = ProductsModel.update_product(identifier, name, description, price, qty)

        return product_schema.jsonify(upd_product)
    
    def delete(self, identifier):
        product = ProductsModel.query.get(identifier)
        if product == None:
            return make_response(jsonify({ 'error': f'Product with the id of {identifier} does not exist' }), 400)

        db.session.delete(product)
        db.session.commit()
        return make_response(jsonify({ 'message': f'Product with the id of {identifier} has been deleted' }), 200)

# Register apis
api.add_resource(ProductList, '/api/products')
api.add_resource(Products, '/api/products/<int:identifier>')

if __name__ == "__main__":
    app.run(debug=True)