from src.repositories.db_connection import SupabaseConnection
import pandas as pd

class Clientes:

    def __init__(self):
        self.db_con = SupabaseConnection()

    def get_client(self,table,dni_client):
        data = self.db_con.get(table)
        df = pd.DataFrame(data)
        resultado = df[df["cedula"]==dni_client]

        return resultado.to_dict()
    
    def add_client(self,json):
        print("------",json)
        return self.db_con.insert("clientes",json)