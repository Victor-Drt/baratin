from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from .config import SECRET_KEY, ALGORITHM
import jwt

password_hash = PasswordHash.recommended()


def hash_password(password):
    return password_hash.hash(password)


def verify_password(plain_password, password):
    return password_hash.verify(plain_password, password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
