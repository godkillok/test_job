import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence
from sqlalchemy.schema import CreateTable
import datetime
engine = create_engine('postgresql://postgres:123456@localhost/pipeline')
Session = sessionmaker(bind=engine)

metadata = MetaData()
users = Table('user_tbl', metadata, schema = 'public', autoload=True, autoload_with=engine)


users_table=Table('user_tbl', metadata, schema = 'public', autoload=True, autoload_with=engine)

connection = engine.connect()
result=[]

for i in range(5):
     print(i, end=',')

for i in range(5):
     data = {}
     print('name'+str(i), end=',')
     data['name']='name'+str(i)
     data['sign'] = 100* i
     result.append(data)
stmt = users_table.insert().\
values(result)

connection.execute(stmt,data)


