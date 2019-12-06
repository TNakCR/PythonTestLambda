import boto3
import pymysql
import pandas as pd
from sqlalchemy import create_engine


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

client = boto3.client('s3')
path = 's3://danielbermans3bucket/100SalesRecords.csv'
df = pd.read_csv(path)
print (df[:100])

#engine = create_engine('mysql://scott:tiger@localhost:3306/dandb')
#engine = create_engine('mysql+pymysql://scott:tiger@localhost/dandb')
engine = create_engine('mysql+pymysql://root@localhost/dandb')

# engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')


with engine.connect() as conn, conn.begin():
df.to_sql('sales102',conn, if_exists='append', index=False)
# print(df.head())
