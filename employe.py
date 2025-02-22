import configparser
import pandas as pd
import psycopg2
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

def retrieve_member(sb):
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
    except Exception as e:
              
      print('Connecting to the PostgreSQL database...')
#Creating the engine
engine=create_engine(f'postgresql+psycopg2://{'postgres'}:{'Saibaba.1915'}@{'localhost'}:{5433}/{'postgres'}')
print('Connection established')
    
   #query to retrieve the data

query = "SELECT * FROM employe;"

df_postgres = pd.read_sql(query, engine)
df_postgres.to_csv('employe_from_db.csv', index=False)
print(df_postgres.head())






        
