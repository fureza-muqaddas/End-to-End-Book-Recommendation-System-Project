import os 
import sys
from src.ds_project.exception import CustomException
from src.ds_project.logger import logging
import pandas as pd 
from src.ds_project.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')
    train_data_path: str = os.path.join('artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('artifacts', 'test_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method starts.")
        try:
            df = read_sql_data()
            logging.info("Dataset read as pandas dataframe.")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data is saved.")

           
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
           
            logging.info("Data Ingestion method completed.")

            return (self.ingestion_config.train_data_path, 
                    self.ingestion_config.test_data_path)
        
        except Exception as e:
            logging.error("Error occurred in Data Ingestion method.")
            raise CustomException(e, sys)

