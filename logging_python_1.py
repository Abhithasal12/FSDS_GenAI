import logging
import os

# create a logger string
#logger_str is a format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" 

#  %(asctime)s: means current time in your window # %(levelname)s: your logging.INFO # %(module)s: log_file = "logs/running_log.log" (file name) # %(message)s [Actuall massage we print]

log_folder = "logs"                          #### folder name
log_file = "logs/running_log.log"            #### filepath name 

#os.makedirs-for exicut folder/ (log_folder-for name folder) #Note= exist_ok= if folder is exist then do nothing is True
os.makedirs(log_folder, exist_ok=True)

#logging actuall code
logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    #handler for saveing the file in this logging_file (*log_file) that's why we use [FileHandler]
    handlers=[
        logging.FileHandler(log_file)
    ]
)

logger = logging.getLogger("mylog")



def add_number(a,b):
    out = a + b
    logger.info("succesfuly excuted")

    return out

num = add_number(3,4)
print(num)


