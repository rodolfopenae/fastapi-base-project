import uuid
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class PostgresDatabase():
    def __init__(self):
        self.engine = create_engine(self.set_url())
        self.Base = declarative_base()
        self.Session = sessionmaker(self.engine)
        self.session = self.Session()
    
    def __set_env(self):
        load_dotenv()
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        host = os.getenv('HOST')
        port = os.getenv('PORT')
        dbname = os.getenv('DBNAME')
        return username, password, host, port, dbname
        
    def set_url(self):
        username, password, host, port, dbname = self.__set_env()
        return f'postgresql://{username}:{password}@{host}:{port}/{dbname}'
    
    def run_sql(self, statements):
        username, password, host, port, dbname = self.__set_env()
        conn = psycopg2.connect(
                dbname=dbname,
                user=username,
                password=password,
                host=host,
                port=port,
                )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        for statement in statements:
            cursor.execute(statement)
            cursor.close()
            conn.close()
    

postgres_database = PostgresDatabase()
Base = postgres_database.Base
engine = postgres_database.engine
session = postgres_database.session
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
