python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, users, products, orders
from app.utils.database import engine
from app.utils.auth_utils import get_current_user
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from supabase import create_client, Client
import os

# Create a Supabase client
supabase_url = os.environ["SUPABASE_URL"]
supabase_anon_key = os.environ["SUPABASE_ANON_KEY"]
supabase_service_key = os.environ["SUPABASE_SERVICE_KEY"]
supabase: Client = create_client(supabase_url, supabase_anon_key)

# Create a database engine
db_password = os.environ["DB_PASSWORD"]
db_host = os.environ["DB_HOST"]
engine = create_engine(f"postgresql://postgres:{db_password}@{db_host}:5432/postgres")

# Create a FastAPI app
app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)

# Define a route for protected data
@app.get("/protected")
async def protected(current_user: dict = Depends(get_current_user)):
    # Return protected data
    return {"message": "Hello, protected world!"}