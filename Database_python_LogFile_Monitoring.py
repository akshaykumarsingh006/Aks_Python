import pyodbc
conn = pyodbc.connect("driver={SQL Server Native client 11.0};"
                      "server=MC0ZYWFC\SQLEXPRESS;"
                      "database=master;"
                      "trusted_connection=yes")
cursor = conn.cursor()
z = cursor.execute("dbcc sqlperf('logspace')").fetchall()
for a,b,c,d in z:
    if c>20:
        print('SendEmail.!The log_space used_percentage is {} for {} DB'.format(c,a))

conn.close()