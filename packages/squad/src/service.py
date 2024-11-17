from src.repository import SquadRepository

from shared.core.base_service import BaseService
from shared.core.database.connection import DatabaseConnection


class SquadService(BaseService):
    def __init__(self, database: DatabaseConnection):
        self.repository = SquadRepository(database)

    def get_all_squads(self):
        # Edit if you have to add logic
        return self.repository.get_all()

    def create_squad(self, body):
        # Edit if you have to add logic
        return self.repository.create(body)
