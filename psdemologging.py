import logging
from termcolor import colored

text = colored('Hello, World!', 'blue', attrs=['reverse', 'blink'])
# print(text)

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt_str)# , filename='error.log')

logging.debug(text)
logging.info('confirmation notes')
logging.warning('warnings message')
logging.error('an error information')
logging.critical('panic errors')

