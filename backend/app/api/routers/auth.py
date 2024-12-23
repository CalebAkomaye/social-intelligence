from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from api.deps import bcrypt_context
from models import  Token, UserCreate
from utils import create_access_token, authenticate_user
from schemas import serialize_user
from fastapi.security import OAuth2PasswordRequestForm
from config.db import User
from bson import ObjectId

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def create_user(user_credentials: UserCreate):
    user_data = user_credentials.dict()
    username = user_data['username']
    email = user_data['email']
    password = bcrypt_context.hash(user_data['password'])
    
    # if user already registered
    existing_user = User.find_one({'email': email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered"
        )
    
    # Create the new user
    user = {
        "_id": ObjectId(),
        "username": username,
        "email": email,
        "password": password
    }
    # user = serialize_user(existing_user)
    User.insert_one(user)
    
    return {"message": "User created successfully", "user": serialize_user(user)}

@router.post('/login', response_model=Token)
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], email: str):
    user = authenticate_user(email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Error validating user",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    token = create_access_token(user["email"], str(user["_id"]), timedelta(minutes=20))

    
    return {"access_token": token, "token_type": "Bearer"}