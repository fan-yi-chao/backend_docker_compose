
import os
import time
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    # Retry logic is intentionally simple here to force CI to handle wait
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        database=os.environ.get('DB_NAME', 'testdb'),
        user=os.environ.get('DB_USER', 'user'),
        password=os.environ.get('DB_PASSWORD', 'password')
    )
    return conn

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1;')
        conn.close()
        return "DB Connected!"
    except Exception as e:
        return f"Connection Failed: {e}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
