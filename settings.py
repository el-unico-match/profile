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
	
    model_config = SettingsConfigDict(env_file=".env")	