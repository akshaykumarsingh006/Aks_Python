import pyodbc
conn = pyodbc.connect("driver={SQL Server Native client 11.0};"
                      "server=MC0ZYWFC\SQLEXPRESS;"
                      "database=master;"
                      "trusted_connection=yes")
cursor = conn.cursor()
z = cursor.execute("""
Set NOCOUNT ON
DECLARE @GetInstances TABLE
( Value nvarchar(100),
 InstanceNames nvarchar(100),
 Data nvarchar(100))
Insert into @GetInstances
EXECUTE xp_regread
@rootkey = 'HKEY_LOCAL_MACHINE',
@key = 'SOFTWARE\Microsoft\Microsoft SQL Server',
@value_name = 'InstalledInstances'
Select InstanceNames from @GetInstances""").fetchall()

print('SQL Instance names are: \n ')
for items in z:
    print(' '.join(items))

conn.close()