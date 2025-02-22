import configparser
import pandas as pd
import psycopg2
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

def retrieve_transaction(cls):
    from sqlalchemy import create_engine
    import pandas as pd
    config = configparser.ConfigParser()
    config.read('credentials.cfg')
    try:
            #Database connection parameters
            DATABASE_TYPE = 'postgresql'
            DBAPI = 'psycopg2'
            ENDPOINT = config['postgres']['local_HOST'] # e.g., localhost or remote server
            USER = config['postgres']['postgres']
            PASSWORD = config['postgres']['Saibaba.1915']
            PORT = 5433 # Default PostgreSQL port
            DATABASE = config['postgres']['postgres']
             
        
             #Creating the engine
            engine=create_engine(f'{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}')
            #Query to retrieve all transactions
            query = "SELECT * FROM transactions"
            df_postgres = pd.read_sql(query, engine)
            df_postgres.to_csv('transactions_from_db.csv', index=False)
            print(df_postgres.head())
    except Exception as e:
        print(f"Error: {e}")

              
  
   





        
