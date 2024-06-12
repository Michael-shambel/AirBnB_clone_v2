#!/usr/bin/python3
""" DB Storage """
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import Column, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


class DBStorage:
    """The database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """ Creates engine """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects from the database session."""
        objects = []

        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                except KeyError:
                    pass
            if issubclass(cls, Base):
                objects = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                objects.extend(self.__session.query(subclass).all())
        obj_dict = {}
        for obj in objects:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            try:
                if obj.__class__.__name__ == 'State':
                    del obj._sa_instance_state
                    obj_dict[key] = obj
                else:
                    obj_dict[key] = obj
            except Exception:
                pass
        return obj_dict
        """if cls is not None:
            query = self.__session.query(cls).all()
            for obj in query:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects"""

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commits the session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj from session """
        self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the session."""
        self.__session.close()
