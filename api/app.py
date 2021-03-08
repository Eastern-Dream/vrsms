from sqlite3 import *
from sqlalchemy import *
from sqlalchemy.orm import *
from flask import Flask
import models

app = Flask(__name__)
models.main()

DATABASE = "sqlite:///database.db"

engine = create_engine(DATABASE)
session = Session(engine)

results = session.query(Customer).all()
print(results)