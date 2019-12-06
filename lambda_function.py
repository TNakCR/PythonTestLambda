import boto3
import pymysql
import pandas as pd
from sqlalchemy import create_engine

def lambda_handler(event, context):
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    client = boto3.client('s3')
    path = 's3://chromeriver-navigator-int-c4-dev/100SalesRecords.csv'
    df = pd.read_csv(path)
    print (df[:100])

    engine = create_engine('mysql+pymysql://Test_User:Test_Pasword@c4-dev-navigatordb-0.cemtanyak0jn.us-west-2.rds.amazonaws.com/chrome_navigator')

    with engine.connect() as conn, conn.begin():
    #df.to_sql('sales102',conn, if_exists='append', index=False)
    return {
        'statusCode': 200,
    }
