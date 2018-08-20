class connection:

    def connect_to_instance(self,server_name,database_name):
        import pyodbc
        con_object = pyodbc.connect("driver={SQL Server Native Client 11.0};server={%s};database={%s};trusted_connection=Yes" %(server_name, database_name))

        return con_object
