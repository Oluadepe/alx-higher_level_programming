#!/usr/bin/python3


from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """
    This class Inherits from Base and links to the MySQL table states.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
