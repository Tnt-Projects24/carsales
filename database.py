from sqlalchemy import create_engine,text
import datetime
import os
db_conn_string = os.environ['DB_CONN_STRING']
#db_conn_string ='mysql+pymysql://admin:tnt-projects#24@cars.cjw4gio06s5f.us-east-1.rds.amazonaws.com:3306/cars'
engine=create_engine(db_conn_string,connect_args={"ssl":                                       {"ssl_ca": "/etc/ssl/cert.pem"}}, echo=True)

#### This is to show the car inventort information for inventory.html
def load_inventory():
  result_dicts = []
  with engine.connect() as conn:
      result = conn.execute(text("select * from cars"))
  
      for row in result.all():
          result_dicts.append(row._asdict())
  return result_dicts
#print( result_dicts)


## This is to add the cars into the cars table.
def add_cars():
  # get the cars details from the form
  # crete a sql statement to save it to the database.
  insert_stmt = "insert into cars (name, year, price) values (:name, :year, :price)"
  with engine.connect() as conn:
    result = conn.execute(text(insert_stmt, name="test", year=2023, price=1000"))
  