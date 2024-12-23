from datetime import datetime, timedelta, timezone
from config.config import SECRET_KEY, ALGORITHM
from api.deps import bcrypt_context
from schemas import serialize_user
from config.db import User

from jose import jwt

def authenticate_user(email: str, password: str):
    user = User.find_one({'email': email})
    if not user:
        return False
    if not bcrypt_context.verify(password, user["password"]):
        return False
    return user


def create_access_token(username: str, user_id: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)