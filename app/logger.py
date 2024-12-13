import logging
import os


def setup_logger():
    log_file_path = 'log/app.log'
    log_dir = os.path.dirname(log_file_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        filename=log_file_path,
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.DEBUG
    )
    logger = logging.getLogger()

    logger.info("Logger baslatildi")
    return logger
