from sqlalchemy import create_engine
from config import conf 

engine = create_engine(f"mysql://{conf.MYSQL_USER}:{conf.MYSQL_PASSWORD}@{conf.MYSQL_URL}/{conf.MYSQL_DATABASE}")