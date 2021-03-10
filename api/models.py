from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def main():
    

    customer = Table(
        "customer",
        Base.metadata,
        Column("customer_id", Integer),
        Column("first_name", String),
        Column("last_name", String),
        Column("license_id", String),
        Column("birth_date", Date),
        Column("home_address", String),
        Column("email_address", String)
    )

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
        customer_id = Column(Integer, primary_key = True)
        first_name = Column(String)
        last_name = Column(String)
        license_id = Column(String)
        birth_date = Column(Date)
        home_address = Column(String)
        phone_number = Column(String)
        email_address = Column(String)

    class Employee(Base):
        __tablename__ = "employee"
        employee_id = Column(Integer, primary_key = True)
        username = Column(String)
        password_hash = Column(String)
        first_name = Column(String)
        last_name = Column(String)
        home_address = Column(String)
        phone_number = Column(String)
        work_availability = Column(Boolean)
        hour_worked = Column(Integer)

    class Dvd(Base):
        __tablename__ = "dvd"
        dvd_id = Column(Integer, primary_key = True)
        title = Column(String)
        actor = Column(String)
        director = Column(String)
        genre = Column(String)
        rent_price = Column(Float)
        sell_price = Column(Float) 
        amount_instock = Column(Integer)
        amount_bought = Column(Integer)
        amount_sold = Column(Integer)

    class Administrator(Base):
        __tablename__ = "administrator"
        admin_id = Column(Integer, primary_key = True)
        username = Column(String)
        password_hash = Column(String)

    class Credit_card(Base):
        __tablename__ = "credit_card"
        card_number = Column(String, primary_key = True)
        customer_id = relationship("Customer", backref = "customer_id")
        first_name = Column(String)
        last_name = Column(String)
        expire_date = Column(Date)

    class Rental(Base):
        __tablename__ = "rental"
        rental_id = Column(Integer, primary_key = True)
        customer_id = relationship("Customer", backref = "customer_id")
        dvd_id = relationship("Dvd", backref = "dvd_id")
        rent_date = Column(Date)

    class Request(Base):
        __tablename__ = "request"
        request_id = Column(Integer, primary_key = True)
        #customer_id = relationship("Customer", backref = "customer_id")
        customer_id = Column(Integer, ForeignKey('customer.customer_id'))
        #dvd_id = relationship("Dvd", backref = "dvd_id")
        dvd_id = Column(Integer, ForeignKey('dvd.dvd_id'))
        #__table_args__ = (UniqueConstraint('customer_id','dvd_id'),)
        #__table_args__ = (ForeignKeyConstraint(["customer_id", "dvd_id"], ["Customer.customer_id", "Dvd.dvd_id"]),{})
        

if __name__ == "__main__":
    main()