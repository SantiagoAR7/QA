import os
from supabase import create_client


class SupabaseConnection:
    """Class for connection to supabase database"""


    def __init__(self):
        """ init module"""
        # SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
        # SUPABASE_KEY: str = os.environ.get("SUPABASE_KEY")
        SUPABASE_URL = "https://xqmafvkfnczqconrupfb.supabase.co"
        SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhxbWFmdmtmbmN6cWNvbnJ1cGZiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzUxNDM4OTQsImV4cCI6MjA1MDcxOTg5NH0.Rtl-QSshb3XUNoHLOeLq-RO45E9L19I19GTRphpl0rk"
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    def get(self, table:str):
        """ Get data from table"""
        return self.supabase.table(table).select("*").execute().data
    
    def insert(self, table:str, json:dict):
        """ Insert data"""
        return (self.supabase.table(table).insert(json).execute())
    