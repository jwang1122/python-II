from sqlite6 import create_connection

def main():
    database = "sqlitebook.db"
    
    sql_create_books_table = """ CREATE TABLE IF NOT EXISTS books (
                                        _id text PRIMARY KEY,
                                        title text NOT NULL,
                                        author text,
                                        read boolean,
                                        price real,
                                        rating integer
                                    ); """

    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_books_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
    print("Done.")