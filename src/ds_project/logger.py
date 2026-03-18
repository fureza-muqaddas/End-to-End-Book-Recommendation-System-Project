import logging 
import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # Log file will be created in the current working directory with the name format "YYYY-MM-DD.log"
os.makedirs(log_path, exist_ok=True) # Ensure the directory exists

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE) # Full path to the log file

logging.basicConfig(
    filename=LOG_FILE_PATH,     
    level=logging.INFO,
    format='%(lineno)d - %(name)s - %(levelname)s - %(message)s'
)