# already comes with a powerful module for logging
from logging_helper import logger


# different logging levels, config options, how to log in different modules, log handles, stack trace
logger.debug('this is a debug message')
logger.info('this is a info message')
logger.warning('this is a warning message')
logger.error('this is an error message')
logger.critical('this is a critical message')

# by default only messages with level warning or above are printed, to change this we need to modify the config
# by default the messages will be logged by the root logger
# below is the way to create the logger for this module

# we can create a helper class to help with the logging config
# refer to the logging_helper.py

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logger.error(e, exc_info=True) # exec_info = True prints the stacktrace

# a large application with lot of logging needs log rotation
from logging.handlers import RotatingFileHandler

rotating_file_handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(rotating_file_handler)

for _ in range(10000):
    logger.error("hello, world")

from logging.handlers import TimedRotatingFileHandler
import time
# timed rotating file handler
# s - seconds, m - minutes, h hours, midnight, w0 Monday, w1 Tuesday, etc.
timed_rotating_file_handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(timed_rotating_file_handler)

for _ in range(6):
    logger.error("hello world!")
    time.sleep(5)

# if there are lot of different modules and microservices architecture
# use json format for logging - use python-json-logger which is opensource
import logging
from pythonjsonlogger import jsonlogger

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

logger.error({"special": "value", "run": 12})
logger.error("classic message", extra={"special": "value", "run": 12})
