# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgresql+psycopg2://vgdb:vgdb@/vgdb?host=/cloudsql/vgdb-224122:us-central1:vgdb')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres@localhost:5432/mydb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Game(db.Model):
  __tablename__ = 'games'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(160), nullable = True)
  release_date = db.Column(db.String(80), nullable = True)
  platforms = db.Column(db.String(80), nullable = True)
  rating = db.Column(db.Integer, nullable = True)
  #dev
  developers = db.Column(db.ARRAY(db.String(80)))
  developer_ids = db.Column(db.ARRAY(db.Integer))
  #engines
  engines = db.Column(db.ARRAY(db.String(80)))
  engine_ids = db.Column(db.ARRAY(db.Integer))

  cover = db.Column(db.String(160), nullable = True)

class Engine(db.Model):
  __tablename__ = 'engines'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable = True) 

  #games
  games = db.Column(db.ARRAY(db.String(80)))
  game_ids = db.Column(db.ARRAY(db.Integer))

  platforms = db.Column(db.ARRAY(db.String(80)))
  logo = db.Column(db.String(200), nullable = True)
  created_at = db.Column(db.Integer, nullable = True)

  #companies
  company_ids = db.Column(db.ARRAY(db.Integer))
  companies = db.Column(db.ARRAY(db.String(80)))

  founding = db.Column(db.String(80), nullable = True)

class Developer(db.Model):
  __tablename__ = 'developers'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable = True)

  #games
  games = db.Column(db.ARRAY(db.String(80)))
  game_ids = db.Column(db.ARRAY(db.Integer))

  #engines
  engines = db.Column(db.ARRAY(db.String(80)))
  engine_ids = db.Column(db.ARRAY(db.Integer))

  founding = db.Column(db.String(80), nullable = True)

  country = db.Column(db.String(80), nullable = True)
  website = db.Column(db.String(80), nullable = True)
  start_date = db.Column(db.String(80), nullable = True)
  logo = db.Column(db.String(80), nullable = True)
  description = db.Column(db.String(10000), nullable = True)

db.drop_all()
db.create_all()


# End of models.py
