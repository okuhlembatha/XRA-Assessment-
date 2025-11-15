import os
import sys
import psycopg2
from psycopg2 import sql

# Get environment variables
def get_env_variable(var_name, required=True, default=None):
    value = os.environ.get(var_name, default)
    if required and (value is None or value == ""):
        print(f"Error: Missing required environment variable: {var_name}")
        print("Please set DB_HOST, DB_NAME, DB_USER, DB_PASSWORD")
        sys.exit(1)
    return value
    

# Build database config
def get_database_connection():
    return {
        "host": get_env_variable("DB_HOST"),
        "port": get_env_variable("DB_PORT"),
        "database": get_env_variable("DB_NAME"),
        "user": get_env_variable("DB_USER"),
        "password": get_env_variable("DB_PASSWORD")
    }

# Connect to PostgreSQL
def connect_to_database():
    try:
        db_config = get_database_connection()
        connection = psycopg2.connect(**db_config)
        print("Successfully connected")
        return connection
    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
        sys.exit(1)

# Create table if it does not exist
def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
        connection.commit()
        print("Employees table created")
    except psycopg2.Error as e:
        connection.rollback()
        print(f"Failed to create table: {e}")
        sys.exit(1)

# Insert new employee
def insert_employee(connection, name, department):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO employees (name, department) VALUES (%s, %s)",
                (name, department),
            )
        connection.commit()
        print("Employee added.")
    except psycopg2.Error as e:
        connection.rollback()
        print(f"Failed to insert new employee: {e}")

# Print all rows for employees
def print_all_employees(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, department, created_at FROM employees ORDER BY id")
            rows = cursor.fetchall()

            print("\nEmployees:")
            print("-" * 60)
            print(f"{'ID':<5}{'Name':<20}{'Department':<20}{'Created At'}")
            print("-" * 60)

            for row in rows:
                print(f"{row[0]:<5}{row[1]:<20}{row[2]:<20}{row[3]}")
            print("-" * 60)
    except psycopg2.Error as e:
        print(f"Failed to print employees: {e}")

def main():
    connection = connect_to_database()
    create_table(connection)

    name = input("Name: ").strip()
    department = input("Department: ").strip()

    insert_employee(connection, name, department)
    print_all_employees(connection)

    connection.close()

if __name__ == "__main__":
    main()
    
