from flask_sqlalchemy import SQLAlchemy


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

# storage_spaces
    # storage_space_id
    # location
    # capacity

# melons
    # initial_slices
    # arrival_date
    # melon_type_id (fk)
    # storage_space_id (fk)

# orders
    # order_id
    # date
    # customer_id

# melon_orders
    # melon_order_id
    # melon_id (fk)
    # order_id (fk)

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
    
    cren = MelonType(name="crenshaw", max_slices=25)
    
    db.session.add_all([cust1, cren])

    db.session.commit()


