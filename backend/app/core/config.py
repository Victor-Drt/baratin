import os
from dotenv import load_dotenv

load_dotenv(".env")

SECRET_KEY = os.getenv("SECRET_KEY", "valor_default") 
ALGORITHM = os.getenv("ALGORITHM", "HS256") 
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30) 
