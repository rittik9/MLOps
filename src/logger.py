#any execution that happens should be able to log all those infomation,execution in some files so that we will be able to track if there is some error 
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #path of the logs file which will get created
os.makedirs(logs_path,exist_ok=True) #even if the file exists keep appending in the file

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

#to override functionality basic config
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)

# if __name__=="__main__":
#     logging.info("Logging has started")
    
