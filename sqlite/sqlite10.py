from sqlite6 import create_connection
import uuid

if __name__ == '__main__':
    database = "sqlitebook.db"

    conn = create_connection(database)
    try:
        c = conn.cursor()
        books = [(uuid.uuid4().hex, 'Python - I', 'John Wang', True, 10.88,3),
                    (uuid.uuid4().hex, 'Python - II', 'Elle Fu', False, 7.55,5),
                    (uuid.uuid4().hex, 'Python - III', 'Alex Liang', False, 12.00,4),
                    ]
        c.executemany('INSERT INTO books VALUES (?,?,?,?,?,?)', books)
        conn.commit()
    except Exception as error:
        print("Error:",error)
    conn.close()
    
    print("Done.")