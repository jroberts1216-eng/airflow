import psycopg2
from api_request import mock_fetch_data

def connect_to_db():
    print("Connecting to the Postgres SQL database . . .")
    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,  # Common default port for PostgreSQL is 5432, not 5000
            dbname="db",
            user="db_user",
            password="db_password"
        )
        print("Connection successful.")
        return conn
    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
        raise

def create_table(conn):
    print("Creating table if not exists . . .")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_descriptions TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
        """)
        conn.commit()
        print("Table was created.")
    except psycopg2.Error as e:
        print(f"Failed to create table: {e}")
        raise

def insert_records(conn, data):
    print("Inserting weather data into the database . . .")
    try:
        weather = data['current']
        location = data['location']
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (
                city,
                temperature,
                weather_descriptions,
                wind_speed,
                time,
                utc_offset
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        conn.commit()
        print("Data successfully inserted")
    except psycopg2.Error as e:
        print(f"Error inserting data into the database: {e}")
        raise

# Main execution
def main():
    try:
        #data = mock_fetch_data()
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occured during execution {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")