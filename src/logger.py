import logging
import os
from datetime import datetime

# Generate a unique log file name based on the current date and time
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR = os.path.join(os.getcwd(), "logs")

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Complete path to the log file
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(filename)s:%(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# if __name__ == "__main__":
#     logging.info("logging has started")





#to log any execution happens to track them, even the errors will be logged so that we can debug them later on
#above code will create a folder logs in cwd which is src & every file name will be "logs" + LOG_FILE