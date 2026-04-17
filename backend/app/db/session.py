from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import SQLALCHEMY_DATABASE_URL


# Cria a engine do SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria a sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependência para obter a sessão nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}
