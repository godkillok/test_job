import psycopg2
import time
# conn = psycopg2.connect(database='postgres',password＝"123",user='postgres',host='localhost',port=5432)

conn =psycopg2.connect(database="pipeline",  host="localhost", port="5432")#user="postgres", password="123",
pipeline = conn.cursor()

#创立strem
create_str = """
CREATE STREAM namestream2 (name text, namecount bigint,namecount2 bigint);
"""
# pipeline.execute(create_str)
# conn.commit()
# drop_str='''
# DROP STREAM namestream2 CASCADE
# '''
stmt = '''
              SELECT T1.schema, T1.name FROM
              pipeline_streams() T1
               '''
ert=pipeline.execute(stmt)
conn.commit()

#建立正常的CONTINUOUS VIEW
create_cv = """
CREATE CONTINUOUS VIEW namecout7_view AS SELECT name,COUNT(*),sum(namecount) FROM namestream2 GROUP BY name
"""
# pipeline.execute(create_cv)
# conn.commit()


#建立Stream-table JOINs正常的CONTINUOUS VIEW
create_cv = """
CREATE CONTINUOUS VIEW streamjoin AS SELECT namestream.name,COUNT(*) FROM namestream join user_tbl ON namestream.name = user_tbl.name GROUP BY namestream.name
"""
# pipeline.execute(create_cv)
# conn.commit()

#1分钟的时间窗口CONTINUOUS VIEW
create_cv = """
CREATE CONTINUOUS VIEW namecout4 with(sw = '2 minute') AS SELECT name,sum(namecount) FROM namestream GROUP BY name
"""
# pipeline.execute(create_cv)
# conn.commit()

#1分钟的时间窗口CONTINUOUS VIEW
create_cv = """
CREATE CONTINUOUS VIEW namemin2 with(ttl = '1 minute',ttl_column = 'minute') AS SELECT minute(arrival_timestamp),name,COUNT(*) FROM namestream GROUP BY minute,name
"""
# pipeline.execute(create_cv)
# conn.commit()

draw_cv = """
drop continuous view namecout4
"""
# pipeline.execute(draw_cv)
# conn.commit()
rows = []
# # ten minutes windows
'''
select from_unixtime(floor(unix_timestamp(date_time)/600)*600) as begin_time, count(*) 
 from host_performance 
 group by begin_time;  
'''
# select_cv = """
# SELECT * FROM pipeline_views();
# """
# w=pipeline.execute(select_cv)
# c=conn.commit()
for i in range(100):
    data = {}
    print('name' + str(i), end=',')
    data['name'] = 'name' + str(i/2)
    data['namecount'] = 1 * i
    data['namecount2'] = 1 * i
    data['namecount3'] = 1 * i
    rows.append(data)
pipeline.executemany('INSERT INTO namestream2 VALUES (%(name)s,%(namecount)s,%(namecount2)s)', rows)

    # rows = []
# pipeline.execute("INSERT INTO namestream VALUES('apple',52642)")
# pipeline.execute("INSERT INTO namestream VALUES('apple3',5642)")
# pipeline.execute("INSERT INTO namestream VALUES('apple2',5642)")
# # Now write the rows to the stream


#插入一个table
# pipeline.execute('INSERT INTO namestream (name) SELECT name FROM user_tbl')


# Now read the results
# pipeline.execute('SELECT * FROM namecout_view')
# rows = pipeline.fetchall()
# print("＝＝＝normal and er")
# print("\t\n")
# for row in rows:
#     name, count = row
#     print(name, count)
#
# # Now read the results
# pipeline.execute('SELECT * FROM namecout２')
# rows = pipeline.fetchall()
# print("\t\n")
# print("＝＝＝1 minute window")
# for row in rows:
#     name, count = row
#     print(name, count)
#
#
# # Now read the results１
# pipeline.execute('SELECT * FROM namecout２_view')
# rows = pipeline.fetchall()
# print("\t\n")
# print("＝＝normal but later")
# for row in rows:
#     name, count = row
#     print(name, count)
#
#
# # Now read the results１２
# pipeline.execute('SELECT * FROM namemin2')
# rows = pipeline.fetchall()
# print("\t\n")
# print("＝＝ttl = '1 minute', ttl_column = 'minute‘")
# for row in rows:
#     name, minute,count = row
#     print(name, minute,count)
#
# # Now read the results１２
# pipeline.execute('SELECT * FROM streamjoin')
# rows = pipeline.fetchall()
# print("\t\n")
# print("＝＝streamjoin‘")
# for row in rows:
#     name,count = row
#     print(name, minute,count)
# pipeline.execute('DROP CONTINUOUS VIEW continuous_view')
pipeline.close()

