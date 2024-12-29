from sqlalchemy import create_engine,text
import datetime
import os
db_conn_string = os.environ['DB_CONN_STRING']
db_conn_string ='mysql+pymysql://admin:tnt-projects#24@cars.cjw4gio06s5f.us-east-1.rds.amazonaws.com:3306/cars'
engine=create_engine(db_conn_string,connect_args={"ssl":                                       {"ssl_ca": "/etc/ssl/cert.pem"}}, echo=True)

def load_inventory():
  result_dicts = []
  with engine.connect() as conn:
    result = conn.execute(text("select * from cars"))
  
    for row in result.all():
      result_dicts.append(row._asdict())
  return result_dicts
#print( result_dicts)