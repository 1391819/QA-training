from application import db

# purpose of backref
# we reference the country that London belongs to using "country".
# this is what we named the backref variable in db.relationship()
# i.e. Cities(name="London", country=uk)


class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime(), nullable=False)
    orders_products = db.relationship("OrdersProducts", backref="orders")


class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    orders_products = db.relationship("OrdersProducts", backref="products")


class OrdersProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(
        "order_id", db.Integer, db.ForeignKey("orders.order_id"), nullable=False
    )
    product_id = db.Column(
        "product_id", db.Integer, db.ForeignKey("products.product_id"), nullable=False
    )
