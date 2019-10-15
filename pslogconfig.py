import logging
from logging.handlers import RotatingFileHandler

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
fmt = logging.Formatter(fmt_str)  # what to log?

rfh = RotatingFileHandler('access.log', maxBytes=32, backupCount=5)  # where to log?
rfh.setFormatter(fmt)  # set formatter to the handler

sh = logging.StreamHandler()   # to log into  console
sh.setFormatter(fmt)

logger = logging.getLogger('amadeus')  # custom logger object
logger.setLevel(logging.DEBUG)
logger.addHandler(rfh)  # adding handler to logger
logger.addHandler(sh)
