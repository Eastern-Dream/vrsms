from sqlite3 import *
from sqlalchemy import *
from sqlalchemy.orm import *
from flask import Flask
import models

app = Flask(__name__)
models.main()

DATABASE = "sqlite:///database.db"

engine = create_engine(DATABASE)
models.Base.metadata.create_all(engine)

insert = insert(customer).values(first_name = "John", last_name = "Doe", license_id = "01234", 
birth_date = "2000-01-01", home_address = "123 Main St", email_address = "john@gmail.com")


results = engine.connect().execute(text("select * from customer")).fetchall()
print(results)