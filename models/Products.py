from app import db, ma

class ProductsModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(500))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

    # Add a product
    def add_product(self):
        db.session.add(self)
        db.session.commit()
    

    # Get all records
    def get_all_products(cls):
        return cls.query.all()

    # Check if product with such name exists
    @classmethod
    def check_product_exists(cls, pname):
        return cls.query.filter_by(name = pname).first()

    # Updating a product 
    @classmethod
    def update_product(cls, id, new_name, new_description, new_price, new_qty):
        product = cls.query.get(id)
        if product:
            product.name = new_name if new_name else product.name
            product.description = new_description if new_description else product.description
            product.price = new_price if new_price else product.price
            product.qty = new_qty if new_qty else product.qty
            db.session.commit()
        return(product)


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields= ('id','name','description','price','qty')


# Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
