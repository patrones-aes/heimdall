from modi.core.base_service import BaseService

from repository import SquadRepository
from model import Squad

class SquadService(BaseService):
    def get_all_squads(self):
        # Edit if you have to add logic
        repository = SquadRepository(Squad, self.connection)
        return repository.get_all()

    def create_squad(self, body):
        # Edit if you have to add logic
        repository = SquadRepository(Squad, self.connection)
        return repository.save(Squad(**body))
