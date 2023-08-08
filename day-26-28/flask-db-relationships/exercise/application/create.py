from application import app, db
from application.models import Orders, Products, OrdersProducts

# create the database schema or even just test db connection
with app.app_context():
    db.drop_all()  # this should be removed if we don't want to delete existing data
    db.create_all()

    # add examples to orders table
    order1 = Orders(order_date="2023/08/08")
    db.session.add(order1)
    db.session.commit()

    order2 = Orders(order_date="2023/08/03")
    db.session.add(order2)
    db.session.commit()

    # add examples to products table
    soap = Products(product_name="Soap")
    db.session.add(soap)
    db.session.commit()

    apple_juice = Products(product_name="Apple Juice")
    db.session.add(apple_juice)
    db.session.commit()

    # creating many-to-many relationships
    orders_products1 = OrdersProducts(orders=order1, products=soap)
    orders_products2 = OrdersProducts(orders=order1, products=apple_juice)
    orders_products3 = OrdersProducts(orders=order2, products=soap)
    orders_products4 = OrdersProducts(orders=order2, products=soap)

    db.session.add(orders_products1)
    db.session.add(orders_products2)
    db.session.add(orders_products3)
    db.session.add(orders_products4)
    db.session.commit()

    print(f"Order 1 on date {order1.order_date}")
    print(f"Order 2 on date {order2.order_date}")
    print(f"Product 1 is: {soap.product_name}")
    print(f"Product 2 is: {apple_juice.product_name}")
    # TOOD: Search how to query orders_products table to get full info
