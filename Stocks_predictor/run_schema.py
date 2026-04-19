import os
from db_config import create_connection

def run_schema():
    """
    Connects to PostgreSQL and runs the schema.sql script to create tables.
    """
    # Get the path to schema.sql relative to this script
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')

    # Read the SQL file
    try:
        with open(schema_path, 'r') as file:
            sql_script = file.read()
    except FileNotFoundError:
        print(f"Error: schema.sql file not found at {schema_path}")
        return
    except Exception as e:
        print(f"Error reading schema.sql: {e}")
        return

    # Connect to database and execute script
    conn = None
    try:
        conn = create_connection()
        cursor = conn.cursor()

        # Execute the SQL script
        cursor.execute(sql_script)

        # Commit the changes
        conn.commit()

        print("Schema created successfully!")

    except Exception as e:
        print(f"Error executing schema: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    run_schema()