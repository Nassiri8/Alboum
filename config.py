import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env") 

class Config:
    MYSQL_URL = os.getenv("MYSQL_URL")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

conf = Config()