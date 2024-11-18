from shared.core.database.connection import DatabaseConnection
from shared.core.base_model import BaseModel

def get_database(model: BaseModel) -> DatabaseConnection:
    return DatabaseConnection(model)
