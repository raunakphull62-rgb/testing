python
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.utils.auth_utils import authenticate_user, get_current_user
from app.utils.database import get_db
from supabase import create_client, Client
import os
import jwt

# Create a Supabase client
supabase_url = os.environ["SUPABASE_URL"]
supabase_anon_key = os.environ["SUPABASE_ANON_KEY"]
supabase_service_key = os.environ["SUPABASE_SERVICE_KEY"]
supabase: Client = create_client(supabase_url, supabase_anon_key)

# Create an OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Create a router
router = APIRouter()

# Define a model for user authentication
class UserAuth(BaseModel):
    email: str
    password: str

# Define a route for user registration
@router.post("/register")
async def register(user: UserAuth):
    # Register a new user
    user_data = {
        "email": user.email,
        "password": user.password,
    }
    user = supabase.auth.sign_up(user_data)
    if user.user:
        return {"message": "User created successfully"}
    else:
        raise HTTPException(status_code=400, detail="User already exists")

# Define a route for user login
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Authenticate the user
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # Generate a JWT token
    token = jwt.encode({"sub": user.id}, "secret_key", algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}

# Define a route for user logout
@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    # Invalidate the JWT token
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "User logged out successfully"}