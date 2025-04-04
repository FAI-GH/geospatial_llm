import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        print("✅ Connected to the database successfully!")
        return conn
    except Exception as e:
        print("❌ Connection failed:", e)
        return None

if __name__ == "__main__":
    connect()
