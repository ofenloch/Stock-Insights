import os
from db_config import create_connection, create_admin_connection
from psycopg2.extensions import connection

def run_sql_script(sql_script_path: str, conn: connection):
    """
    Connects to PostgreSQL and runs the given SQL script.
    """


    # Read the SQL file
    try:
        with open(sql_script_path, 'r') as file:
            sql_script = file.read()
    except FileNotFoundError:
        print(f"Error: SQL script not found at {sql_script_path}")
        return
    except Exception as e:
        print(f"Error reading SQL script: {e}")
        return

    # Connect to database and execute script
    try:
        cursor = conn.cursor()

        # Execute the SQL script
        cursor.execute(sql_script)

        # Commit the changes
        conn.commit()

        print("SQL script executed successfully!")

    except Exception as e:
        print(f"Error executing SQL script: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    
    # Get the path to config.sql relative to this script
    schema_path = os.path.join(os.path.dirname(__file__), 'config.sql')
    # Run the config script (creating user, dbs, and granting permissions) using the admin connection
    run_sql_script(schema_path, create_admin_connection())    
    
    
    
    # Get the path to schema.sql relative to this script
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    # Run the schema script (creating tables) using the regular non-adminconnection
    run_sql_script(schema_path, create_connection())