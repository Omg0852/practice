# USING SQL CONNECTION

from sqlalchemy import text,create_engine,String,Integer,PrimaryKeyConstraint,Table,Column,MetaData
from sqlalchemy.orm import Session

engine1 = create_engine("sqlite:///db1.db",echo=True)

conn = engine1.connect()
conn.execute(text("CREATE TABLE IF NOT EXISTS employee (id int primary_key,name str,age int)"))


conn.execute(text(f"INSERT INTO employee (id,name,age) VALUES (1,'OM GAIKWAD',23),(2,'NEHA SHARMA',23),(3,'VIJAY RAJPUT',23)"))
conn.commit()

#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# USING SQL SESSIONS TO USE SQL

session = Session(engine1)

session.execute(text("CREATE TABLE IF NOT EXISTS employee (id int primary_key,name str,age int)"))

session.execute(text(f"INSERT INTO employee (id,name,age) VALUES (9,'OM GAIKWAD',23),(8,'NEHA SHARMA',23),(36,'VIJAY RAJPUT',23),(48,'ASTHA',26)"))
session.commit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# USING ORM SETUP


engine2 = create_engine("sqlite:///practice_ORM.db",echo=True)

session = Session(engine2)


#  use of MATADATE : its keeps track of schema including tables,rows ,column and constarins

meta = MetaData()

# creating a table as an object

people = Table(
    "peoples", # name of the table
    meta,  # MetaData object to store the schema of this table
    Column("id", Integer,primary_key=True,autoincrement=True), # creating a Column using a column Object
    Column("name", String,nullable=False),
    Column("age", Integer,nullable=False)

)

# TO STORE THE SCHEMA AND CREATE THE TABELE
meta.create_all(engine2)
