import os
import configparser
from tkinter.filedialog import test
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


ADMIN_HOST=config.get('dbadmin', 'host')
ADMIN_PORT=config.getint('dbadmin', 'port')
ADMIN_DB=config.get('dbadmin', 'dbname')
ADMIN_USER=config.get('dbadmin', 'user')
ADMIN_PASS=config.get('dbadmin', 'password')

def create_connection() -> psycopg2.extensions.connection:
    conn = psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        dbname=PG_DB,
        user=PG_USER,
        password=PG_PASS
    )
    return conn

def create_admin_connection() -> psycopg2.extensions.connection:
    conn = psycopg2.connect(
        host=ADMIN_HOST,
        port=ADMIN_PORT,
        dbname=ADMIN_DB,
        user=ADMIN_USER,
        password=ADMIN_PASS
    )
    return conn

def set_up_database():
    """
        This function creates the user and the database for Stock-Insights
        if they don't exist.
        
        It uses the admin connection to execute the necessary SQL commands.
    """
    
    admin_conn = create_admin_connection()
    admin_conn.autocommit = True

    with admin_conn.cursor() as admin_cursor:
        # Mimick the CREATE USER IF NOT EXISTS
        # see https://stackoverflow.com/a/55954480
        psql_script_1 = f"""
            DO $$
            BEGIN
                CREATE ROLE {PG_USER} WITH LOGIN PASSWORD '{PG_PASS}';
            EXCEPTION WHEN duplicate_object THEN
                RAISE NOTICE '%, skipping', SQLERRM USING ERRCODE = SQLSTATE;
            END
            $$;
        """
        admin_cursor.execute(psql_script_1)
        admin_conn.commit()
        print(f"User {PG_USER} created (or already existed)")

        # The concept from above can't be used with CREATE DATABASE because "CREATE DATABASE cannot run inside a transaction block"
        try:
            admin_cursor.execute(f"CREATE DATABASE {PG_DB} OWNER {PG_USER};")
            print(f"Database {PG_DB} created, owner is {PG_USER}")
        except psycopg2.errors.DuplicateDatabase:
            print(f"Database {PG_DB} already exists, skipping creation.")

        admin_conn.commit() 

    admin_conn.close()
    print("Database and user created successfully!")
    