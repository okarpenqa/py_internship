from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
import csv

engine = create_engine('sqlite:///database.db')
metadata_obj = MetaData()

user = Table('cities', metadata_obj,
             Column('id', Integer, primary_key=True),
             Column('name', String(255), nullable=False),
             Column('country_name', String(255), nullable=False)
             )

metadata_obj.create_all(engine)

with open('city_list.csv', mode='r') as file:
    csv_reader = csv.reader(file, delimiter=';')

    for row in csv_reader:
        stmt = user.insert().values(id=row[2], name=row[1], country_name=row[0])
        with engine.connect() as conn:
            result = conn.execute(stmt)
