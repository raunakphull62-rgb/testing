markdown
# FastAPI Backend

This is a FastAPI backend for a simple e-commerce application. It includes routes for user authentication, product management, and order management.

## Installation

To install the dependencies, run the following command:
bash
pip install -r requirements.txt


## Running the Application

To run the application, use the following command:
bash
uvicorn main:app --host 0.0.0.0 --port 8000


## API Documentation

The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).

## Environment Variables

The following environment variables are required:
* `SUPABASE_URL`: The URL of the Supabase instance.
* `SUPABASE_ANON_KEY`: The anonymous key of the Supabase instance.
* `SUPABASE_SERVICE_KEY`: The service key of the Supabase instance.
* `DB_PASSWORD`: The password of the PostgreSQL database.
* `DB_HOST`: The host of the PostgreSQL database.