from shared.core.database.connection import DatabaseConnection

class BaseService:
    """
    Base Service
    """
    def __init__(self, connection: DatabaseConnection):
        self.connection = connection
