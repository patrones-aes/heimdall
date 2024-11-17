from core.database.connection import DatabaseConnection

def get_database(table_name: str) -> DatabaseConnection:
    return DatabaseConnection(table_name)
