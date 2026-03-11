from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    MYSQL_USER:str =""
    MYSQL_PASSWORD:str =""
    MYSQL_HOST:str =""
    MYSQL_PORT: int =3306
    MYSQL_DATABASE: str =""

    model_config = SettingsConfigDict(env_file="../.env",extra="ignore")

settings = Settings()

Connection_URL = URL.create(
    drivername="mysql+pymysql",
    username=settings.MYSQL_USER,
    password=settings.MYSQL_PASSWORD,
    host=settings.MYSQL_HOST,
    port=int(settings.MYSQL_PORT),
    database=settings.MYSQL_DATABASE,
)

# Connection
engine = create_engine(Connection_URL)

# Session
SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind = engine)

# Base
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
