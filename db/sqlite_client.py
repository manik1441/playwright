import sqlite3
import pandas as pd
from config.utils.logger import get_logger

class SQLiteClient:
    def __init__(self, db_path):
        self.db_path = db_path
        self.logger = get_logger("DB_Client")

    def execute_query(self, query):
        self.logger.info(f"Executing query: {query}")
        with sqlite3.connect(self.db_path) as conn:
            # Pandas simplifies reading SQL into a DataFrame
            df = pd.read_sql_query(query, conn)
        return df