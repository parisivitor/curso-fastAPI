from typing import List

from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
  """
  Configuraçoes gerais usadas na aplicação
  """
  API_V1_STR: str = '/api/v1'
  DB_URL: str = "postgresql+asyncpg://postgres:123123@localhost:5432/faculdade"
  DBBaseModel = declarative_base()

  class Config:
    case_sensitive = True


settings = Settings()
