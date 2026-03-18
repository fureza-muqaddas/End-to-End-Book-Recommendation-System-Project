from src.ds_project.logger import logging
from src.ds_project.exception import CustomException
import sys  
from src.ds_project.components.data_ingestion import DataIngestion


if __name__ == "__main__":
    logging.info("The execution of the main function has started.")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data Ingestion completed. Train data path: {train_data_path}, Test data path: {test_data_path}")

    except Exception as e:
        logging.error("An error occurred in the main function.")
        raise CustomException(e, sys)