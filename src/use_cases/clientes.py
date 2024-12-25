from src.repositories.db_connection import SupabaseConnection

class Clientes:

    def __init__(self):
        self.db_con = SupabaseConnection()

    def get_client(self,table):
        return self.db_con.get(table)