import logging

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
#                     datefmt='%m/%d/%Y %H:%M:%S')

# logger = logging.getLogger(__name__)

# import logging.config
# logging.config.fileConfig('logging.conf')

# file_conf_logger = logging.getLogger('simpleExample')
# file_conf_logger.debug('this is a debug message')

logger = logging.getLogger(__name__)

# create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log_demo.log')

# level and the format
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


