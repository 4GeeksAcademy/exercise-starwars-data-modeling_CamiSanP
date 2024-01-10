import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    population = Column(Integer)

class Starship(Base):
    __tablename__= 'starships'
    id = Column(Integer, primary_key=True)
    model = Column(String(20), unique=True)
    starship_class = Column(String(30))
    length = Column(Integer)

class Character(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    height = Column(Integer)
    mass = Column(Integer)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet_id_relationship = relationship(Planets)
    starship_id = Column(Integer, ForeignKey('starships.id'))
    starship_id_relationship = relationship(Starship)
    
class FavoritesPlanets(Base):
    __tablename__= 'favplanets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet_id_relationship = relationship(Planets)

class FavoritesCharacters(Base):
    __tablename__= 'favcharacters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character_id_relationship = relationship(Character)

class FavoritesStarships(Base):
    __tablename__= 'favstarships'
    id = Column(Integer, primary_key=True)
    starship_id = Column(Integer, ForeignKey('starships.id'))
    starship_id_relationship = relationship(Starship)



#class Person(Base):
    #__tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
    #name = Column(String(250), nullable=False)

#class Address(Base):
    #__tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
    #street_name = Column(String(250))
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
