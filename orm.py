from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper, sessionmaker


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# =====新建表
# 创建实例，并连接test库
# engine = create_engine('postgresql://postgres:123@localhost/postgres',echo=True)
# echo=True 显示信息
# Base = declarative_base()  # 生成orm基类
#
# class User(Base):
#     __tablename__ = 'user'  # 表名
#     __schemaname__ = 'public'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#     password = Column(String(64))
#
# Base.metadata.create_all(engine) #创建表结构 （这里是父类调子类）
#
# #
# =====增加数据行
# # # 创建实例，并连接test库
engine = create_engine('postgresql://postgres:123@localhost/postgres')
#
metadata = MetaData()

user3 = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('password', String(12))
             )
#
#
class User(object):
    def __init__(self, name, id, password):
        self.id = id
        self.name = name
        self.password = password


# the table metadata is created separately with the Table construct, then associated with the User class via the mapper() function
mapper(User, user3)
#
# # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)  # 实例和engine绑定
Session = Session_class()  # 生成session实例，相当于游标
#
user_obj = User(id=28, name="fgf", password="123456")  # 生成你要创建的数据对象
print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None

Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
print(user_obj.name, user_obj.id)  # 此时也依然还没创建

Session.commit()  # 现此才统一提交，创建数据
print(user_obj.name, user_obj.id)  # 此时也依然还没创建