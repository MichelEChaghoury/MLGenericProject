import logging
import os
from datetime import datetime as dt

LOG_FILE: str = f"{dt.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_PATH: str = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(LOGS_PATH, exist_ok=True)


LOG_FILE_PATH: str = os.path.join(LOGS_PATH, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)


if __name__ == '__main__':
    logging.info('Logging has started')
