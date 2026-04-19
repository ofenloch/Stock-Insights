import os
import configparser
import psycopg2


# Get the path to config.ini relative to this script
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read(config_path)

# use PGADMIN-SOFTWARE for simplicity 
# Run the Schema.sql as it is firstly in ur database(using Query Tool) -> then use the same database for DB_CONFIGURATION
PG_HOST = config.get('database', 'host')
PG_PORT = config.getint('database', 'port')
PG_DB   = config.get('database', 'dbname')
PG_USER = config.get('database', 'user')
PG_PASS = config.get('database', 'password')

def create_connection():
    conn = psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        dbname=PG_DB,
        user=PG_USER,
        password=PG_PASS
    )
    return conn
