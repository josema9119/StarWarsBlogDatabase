import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique= True)
    favorites = relationship("Favorites")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters = relationship("Characters")
    planets = relationship("Planets")
    vehicles = relationship("Vehicles")

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    birth_year = Column (Integer)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
  
class vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    cargo_capacity = Column(Integer)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')