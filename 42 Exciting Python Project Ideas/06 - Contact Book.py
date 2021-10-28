import sqlite3
from sqlite3.dbapi2 import Error, connect

def create_connection(db_file):
    # Create a database connection to a SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Database found with version ", sqlite3.version)    
    except Error as e:
        print(e)
    finally:
        return conn

def create_table(conn, create_table_sql):
    """
        Create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "test.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects(
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text);"""

    sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks(
                                id integer PRIMARY KEY,
                                name text NOT NU LL,
                                priority integer,
                                status_id integer NOT NULL,
                                project_id integer NOT NULL,
                                begin_date text NOT NULL,
                                end_date text NOT NULL,
                                FOREIGN KEY (project_id) REFERENCES projects (id)
                            );"""

    conn = create_connection(database)

    
    sql_get_table = "SELECT * FROM projects"
    mycursor = conn.cursor()
    mycursor.execute(sql_get_table)
    myresult = mycursor.fetchall()

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! Cannot create the database connection.")
if __name__ == '__main__':
    main()