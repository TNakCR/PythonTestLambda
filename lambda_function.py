import boto3
import pymysql
import pandas as pd
import sqlalchemy as db

def lambda_handler(event, context):
  pd.set_option('display.max_rows', 500)
  pd.set_option('display.max_columns', 500)
  pd.set_option('display.width', 1000)

  client = boto3.client('s3')
  path = 's3://chromeriver-navigator-int-c4-dev/100SalesRecords.csv'
  df = pd.read_csv(path)
  print (df[:100])

  engine = db.create_engine('mysql+pymysql://cr_tester:ch2goAvaTWQa@c4-dev-navigatordb-0.cemtanyak0jn.us-west-2.rds.amazonaws.com/chrome_navigator')
  connection = engine.connect()
  metadata = db.MetaData()
  flyway_schema_history = db.Table('flyway_schema_history', metadata, autoload=True, autoload_with=engine)
  # Print the column names
  print(flyway_schema_history.columns.keys())
  # Print full table metadata
  print(repr(metadata.tables['flyway_schema_history']))

  #with engine.connect() as conn, conn.begin():
  #df.to_sql('sales102',conn, if_exists='append', index=False)

  return {
        'statusCode': 200,
  }

