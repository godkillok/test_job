import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence
from sqlalchemy.schema import CreateTable
import datetime
import json
engine = create_engine('postgresql://postgres:123456@localhost/pipeline')
Session = sessionmaker(bind=engine)

metadata = MetaData()
users = Table('user_tbl', metadata, schema = 'public', autoload=True, autoload_with=engine)

from sqlalchemy import select

s = select(
    [
        users.c.sign,
        users.c.name
    ]
).select_from(
    users
)

g=engine.execute(s)

fag=g.fetchall()

fag.insert(0,fag[1])
print(type(fag[1]))

data=[]

for v in fag:
    d = {}
    for column, value in v.items():
        d[column]=value
    data.append(d)
data.insert(0, data[1])
data[1]['name']='apple'

data1=[]
data2=[]

for v in fag:
    d2 = {}
    d2=dict(v.items())
    d3=json.dumps(d2)
    data1.append(d2)
    data2.append(d3)
data1.insert(0, data1[1])
data1[1]['name'] = 'apple'
print(data1)


