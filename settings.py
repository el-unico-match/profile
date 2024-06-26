from typing import List
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    disable_db:bool=False
	
    log_filename:str='profile.log'
    NOTSET:int=0
    DEBUG:int=10
    INFO:int=20
    WARNING:int=30
    ERROR:int=40
    CRITICAL:int=50	
    logging_level:int=DEBUG
	
    DOCKER_DOMAIN:str='profile_mongo'
    LOCAL_DOMAIN:str='localhost'
    db_domain:str = LOCAL_DOMAIN
    db_port:int = 5000
    db_host:str=db_domain+":"+str(db_port)
    local_db_name:str='local'
    remote_db_name:str='remote'	
    db_name:str=local_db_name
	
    apikey_value:str=''
    apikey_status:str=''
    apikey_activate_endpoint:str=''
    apikey_whitelist:List[str]=[]
    isIngoingSecurityCheckEnabled:bool=False
    isOutgoingSecurityCheckEnabled:bool=False

    isRunningTests:bool=False

    model_config = SettingsConfigDict(env_file=("dev.env",".env"))	
    
settings=Settings()