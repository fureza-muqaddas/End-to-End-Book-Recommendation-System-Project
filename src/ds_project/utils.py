import os 
import sys
from src.ds_project.exception import CustomException
from src.ds_project.logger import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
db = os.getenv("db")
password = os.getenv("password")

def read_sql_data():
    logging.info("Reading data from SQL database.")
    try:
        mybd = pymysql.connect(host=host, user=user, password=password, db=db)
        logging.info("Data read from SQL database successfully.")
        df=pd.read_sql("SELECT * FROM books", con=mybd)
        return df
        
    except Exception as e:
        raise CustomException(e, sys)
    






