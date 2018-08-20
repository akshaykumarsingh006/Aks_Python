import pyodbc
conn = pyodbc.connect("driver={SQL Server Native Client 11.0};"
                      "server=MC0ZYWFC\SQLEXPRESS;"
                      "database=master;"
                      "trusted_connection=Yes")
cursor = conn.cursor()
z=cursor.execute("""EXEC sp_readerrorlog 0, 1, 'error' """).fetchall()
for items in z:
    if ('Error' in str(items)) and 'Error: 18456' not in str(items):
        print(items)
    elif('error' in str(items)):
        print(items)
    elif ('fail' in str(items)):
        print(items)
    elif('stop' in str(items)):
        print(items)
conn.close()
