import pyodbc
import smtplib
sender = 'akshaykumarsingh006@gmail.com'
recipient = 'akshaykumarsingh006@gmail.com'
password = 'Sksjyots@123'

smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp_server.login(sender, password)
conn = pyodbc.connect("driver={SQL Server Native client 11.0};"
                      "server=DESKTOP-4I4HRRA;"
                      "database=master;"
                      "trusted_connection=yes")
cursor = conn.cursor()
z = cursor.execute('select name as Db_name, state_desc as State from sys.databases').fetchall()
message = (str(z)).strip('  ')
smtp_server.sendmail(sender, recipient, message)
conn.close()
