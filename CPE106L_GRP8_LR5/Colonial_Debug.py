import sqlite3 as sql3
colonial = sql3.connect("Colonial.db")
cursor = colonial.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("ALL TABLES IN DATABASE: \n \n")
for table in tables:
    print(table[0])

    query = f"SELECT * FROM TRIP"
    cursor.execute(query)

    data = cursor.fetchall()
    for row in data:
        print(row)
    print("\n")