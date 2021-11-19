from sqlalchemy import Column, String, create_engine, Integer, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
import os
import datetime


database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''
actor_movie = db.Table(
  'actor_movie',
  Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True),
  Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True)
)


class Actor(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  age = Column(Integer, nullable=False)
  gender = Column(String, nullable=False)
  create_time = Column(DateTime, default=datetime.datetime.utcnow)

  def __init__(self, name, age, gender):
      self.name = name
      self.age = age
      self.gender= gender

  def insert(self):
      db.session.add(self)
      db.session.commit()

  def delete (self):
      db.session.delete(self)
      db.session.commit()

  def update(self):
      db.session.commit()

  def __repr__(self):
      return f'<{self.id} - {self.name}>'

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'gender': self.gender,
      'create_time': self.create_time
    }