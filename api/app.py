from sqlite3 import *
from sqlalchemy import *
from flask import Flask
import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

Base = declarative_base()

# customer = Table(
#     "customer",
#     Base.metadata,
#     Column("customer_id", Integer),
#     Column("first_name", String),
#     Column("last_name", String),
#     Column("license_id", String),
#     Column("birth_date", Date),
#     Column("home_address", String),
#     Column("email_address", String)
# )

# employee = Table(
#     "employee",
#     Base.metadata,
#     Column("employee_id", Integer),
#     Column("username", String),
#     Column("password_hash", String),
#     Column("first_name", String),
#     Column("last_name", String),
#     Column("home_address", String),
#     Column("phone_number", String),
#     Column("work_availability", Boolean),
#     Column("hour_worked", Integer)
# )

# dvd = Table(
#     "dvd",
#     Base.metadata,
#     Column("dvd_id", Integer),
#     Column("title", String),
#     Column("actor", String),
#     Column("director", String),
#     Column("genre", String),
#     Column("rent_price", Float),
#     Column("sell_price", Float),
#     Column("amount_instock", Integer),
#     Column("amount_bought", Integer),
#     Column("amount_sold", Integer)
# )

# administrator = Table(
#     "administrator",
#     Base.metadata,
#     Column("admin_id", Integer),
#     Column("username", String),
#     Column("password_hash", String)
# )

# credit_card = Table(
#     "credit_card",
#     Base.metadata,
#     Column("card_number", String),
#     Column("customer_id", Integer, ForeignKey("customer.customer_id")),
#     Column("first_name", String),
#     Column("last_name", String),
#     Column("expire_date", Date)
# )

# rental = Table(
#     "rental",
#     Base.metadata,
#     Column("rental_id", Integer),
#     Column("customer_id", Integer, ForeignKey("customer.customer_id")),
#     Column("dvd_id", Integer, ForeignKey("dvd.dvd_id")),
#     Column("rent_date", Date)
# )

# request = Table(
#     "request",
#     Base.metadata,
#     Column("customer_id", Integer, ForeignKey("customer.customer_id")),
#     Column("dvd_id", Integer, ForeignKey("dvd.dvd_id"))
# )

class Customer(Base):
    __tablename__ = "customer"
    __table_args__ = ({"extend_existing" : True})
    customer_id = Column("customer_id",Integer, primary_key = True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    license_id = Column("license_id", String)
    birth_date = Column("birth_date", Date)
    home_address = Column("home_address", String)
    phone_number = Column("phone_number", String)
    email_address = Column("email_address", String)

class Employee(Base):
    __tablename__ = "employee"
    __table_args__ = ({"extend_existing" : True})
    employee_id = Column("employee_id", Integer, primary_key = True)
    username = Column("username", String)
    password_hash = Column("password_hash", String)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    home_address = Column("home_address", String)
    phone_number = Column("phone_number", String)
    work_availability = Column("work_availability", Boolean)
    hour_worked = Column("hour_worked", Integer)

class Dvd(Base):
    __tablename__ = "dvd"
    __table_args__ = ({"extend_existing" : True})
    dvd_id = Column("dvd_id", Integer, primary_key = True)
    title = Column("title", String)
    actor = Column("actor", String)
    director = Column("director", String)
    genre = Column("genre", String)
    rent_price = Column("rent_price", Float)
    sell_price = Column("sell_price", Float) 
    amount_instock = Column("amount_instock", Integer)
    amount_bought = Column("amount_bought", Integer)
    amount_sold = Column("amount_sold", Integer)

class Administrator(Base):
    __tablename__ = "administrator"
    __table_args__ = ({"extend_existing" : True})
    admin_id = Column("admin_id", Integer, primary_key = True)
    username = Column("username", String)
    password_hash = Column("password_hash", String)

class Credit_card(Base):
    __tablename__ = "credit_card"
    __table_args__ = ({"extend_existing" : True})
    card_number = Column("card_number", String, primary_key = True)
    customer_id = relationship("Customer", backref = "customer_id")
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    expire_date = Column("expire_date", Date)

class Rental(Base):
    __tablename__ = "rental"
    __table_args__ = ({"extend_existing" : True})
    rental_id = Column("rental_id", Integer, primary_key = True)
    customer_id = relationship("Customer", backref = "customer_id")
    dvd_id = relationship("Dvd", backref = "dvd_id")
    rent_date = Column("rent_date", Date)

class Request(Base):
    __tablename__ = "request"
    __table_args__ = ({"extend_existing" : True})
    request_id = Column("request_id", Integer, primary_key = True)
    #customer_id = relationship("Customer", backref = "customer_id")
    customer_id = Column("customer_id", Integer, ForeignKey('customer.customer_id'))
    #dvd_id = relationship("Dvd", backref = "dvd_id")
    dvd_id = Column("dvd_id", Integer, ForeignKey('dvd.dvd_id'))
    #__table_args__ = (UniqueConstraint('customer_id','dvd_id'),)
    #__table_args__ = (ForeignKeyConstraint(["customer_id", "dvd_id"], ["Customer.customer_id", "Dvd.dvd_id"]),{})
    
DATABASE = "sqlite:///database.db"

engine = create_engine(DATABASE)
Base.metadata.create_all(engine)

# insert = insert(Customer).values(first_name = "John", last_name = "Doe", license_id = "01234", 
# birth_date = datetime.date(2000, 1, 1), home_address = "123 Main St", phone_number = "123456789", email_address = "john@gmail.com")

# insert = insert(Dvd).values(title = "Title", actor = "Actor", director = "Director", genre = "Genre", 
# rent_price = 9.99, sell_price = 19.99, amount_instock = 10, amount_bought = 5, amount_sold = 3)

insert = insert(Rental).values(customer_id = 1, dvd_id = 1, rent_date = datetime.date(2021, 3, 14))

engine.connect().execute(insert)

results = engine.connect().execute(text("select * from rental")).fetchall()
print(results)