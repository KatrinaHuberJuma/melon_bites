from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

class Customer(db.Model):

    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)


class MelonType(db.Model):
    
    __tablename__ = "melon_types"
    
    melon_type_id = db.Column(db.Integer, primary_key=True)
    max_slices = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    # relationionship: melons (list of related Melon objects)



class StorageSpace(db.Model):

    __tablename__ = "storage_spaces"

    storage_space_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    # relationionship: melons (list of related Melon objects)



class Melon(db.Model):

    __tablename__ = "melons"
    melon_id = db.Column(db.Integer, primary_key=True)
    initial_slices = db.Column(db.Integer, nullable=False)
    arrival_date = db.Column(db.Date, nullable=False)
    melon_type_id = db.Column(db.Integer, db.ForeignKey("melon_types.melon_type_id"), nullable=False)
    storage_space_id = db.Column(db.Integer, db.ForeignKey("storage_spaces.storage_space_id"))

    melon_type = db.relationship("MelonType", backref="melons")
    storage_space = db.relationship("StorageSpace", backref="melons")

class Order(db.Model):

    __tablename__ = "orders"
    order_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.datetime.now())
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"), nullable=False)

    customer = db.relationship("Customer", backref="orders")



class MelonOrder(db.Model):

    __tablename__ = "melon_orders"
    melon_order_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    melon_id = db.Column(db.Integer, db.ForeignKey("melons.melon_id"), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.order_id"), nullable=False)

    melon = db.relationship("Melon", backref="melon_orders")
    order = db.relationship("Order", backref="melon_orders")

    

# ======================================

def connect_to_db(app, db_name):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"

    # this would output the raw SQL, currently off as it can be noisy
    # app.config["SQLALCHEMY_ECHO"] = True

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)




if __name__ == "__main__":
    from flask import Flask
    import os
    

    os.system("dropdb melon_bites --if-exists")
    os.system("createdb melon_bites")


    app = Flask(__name__)
    connect_to_db(app, "melon_bites")

    # Make our tables
    db.create_all()

    cust1 = Customer(name="fred the vampire", password="accountant4unlife", address="charlotte manner")
    cust2 = Customer(name="bubba the werepony", password="nightmare", address="charlotte manner")

    cren = MelonType(name="crenshaw", max_slices=25)
    musk = MelonType(name="muskmelon", max_slices=15)

    space1 = StorageSpace(location="warehouse in  Richmond", capacity=400)

    melon1 = Melon(initial_slices=20, arrival_date="2021-10-01" )
    cren.melons.append(melon1) # uses sqlalchemy relationship from the MelonType instance
    space1.melons.append(melon1)

    melon2 = Melon(initial_slices=15, 
                    arrival_date=datetime.datetime.now(), 
                    melon_type=cren, storage_space=space1) # uses the sqlalchmey relationship from the Melon instance
                    # passing in a MelonType object
    
    melon3 = Melon(initial_slices=20, arrival_date="2021-09-29", melon_type=musk)
    
    melon_order1 = MelonOrder(melon=melon1, quantity=7, order=Order(customer=cust2))

    order1 = Order(customer=cust1)
    order1.melon_orders.append(MelonOrder(melon=melon2, quantity=5)) 
    order1.melon_orders.extend([MelonOrder(melon=melon3, quantity=5)])

    



    
    
    db.session.add_all([cust1, cren, space1, melon1])

    db.session.commit()


