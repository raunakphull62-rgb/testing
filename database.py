python
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

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()