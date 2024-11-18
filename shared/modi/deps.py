from modi.core.database.connection import DatabaseConnection
from modi.core.base_model import BaseModel

def get_database(model: BaseModel) -> DatabaseConnection:
    return DatabaseConnection(model)
