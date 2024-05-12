from settings import Settings
from pymongo import MongoClient
#import logging
#import sys

settings=Settings()	

#logging.basicConfig(filename=settings.log_filename)
#logging.basicConfig()
#logger=logging.getLogger('pymongo')
#logger.setLevel(logging.DEBUG)

#stream_handler = logging.StreamHandler(sys.stdout)
#log_formatter = logging.Formatter("%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s")
#stream_handler.setFormatter(log_formatter)
#logger.addHandler(stream_handler)

#host = settings.domain+":"+str(settings.port)

#client_db = MongoClient(host=settings.db_domain,port=settings.db_port)
#client_db = MongoClient()
client = MongoClient(host=settings.db_host)
client_db = client[settings.db_name]
#print(client.host)