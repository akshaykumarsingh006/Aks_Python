from connection import *
conn = connection() ##object creation
conn = conn.connect_to_instance('DESKTOP-4I4HRRA','master')
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
