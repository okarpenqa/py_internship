from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///database.db')


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_name = Column(String)


Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

print('=====Updating object by id=====')
city = session.query(City).get(2)
print('Previous name = {}'.format(city.name))
city.name = 'New name'
session.commit()

updated_city = session.query(City).get(2)
print('Updated name = {}'.format(updated_city.name))
