#from settings import Settings
from pymongo import MongoClient
#import logging
#import sys

#settings=Settings()	

#logging.basicConfig(filename=settings.log_filename)
#logging.basicConfig()
#logger=logging.getLogger('pymongo')
#logger.setLevel(logging.DEBUG)

#stream_handler = logging.StreamHandler(sys.stdout)
#log_formatter = logging.Formatter("%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s")
#stream_handler.setFormatter(log_formatter)
#logger.addHandler(stream_handler)


client_db = MongoClient()