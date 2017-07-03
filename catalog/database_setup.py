import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

#create table 2 as users to store user's information
class User(Base):
    __tablename__ = 'user'
#mapper
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'email': self.email,
            'picture': self.picture
        }


#create table 1 as restaurant
class Restaurant(Base):
    __tablename__ = 'restaurant'
#mapper
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'user_id': self.user_id
        }



#create table 3 as recipes
class Recipe(Base):
    __tablename__ = 'recipes'
#mapper
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(4000))
    price = Column(String(8))
    course = Column(String(250))
    image_url = Column(String(400), nullable=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship('Restaurant', backref='restaurant_recipes', foreign_keys=[restaurant_id])
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(
        'User', backref='user_recipes', foreign_keys=[user_id])

# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
            'image_url': self.image_url,
            'restaurant_id': self.restaurant_id,
            'user_id': self.user_id
        }
engine = create_engine('sqlite:///restaurantmenuwithusers.db')


Base.metadata.create_all(engine)