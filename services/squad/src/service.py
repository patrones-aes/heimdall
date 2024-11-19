from repository import SquadRepository
from model import Squad

class SquadService():
    def get_all_squads(self):
        # Edit if you have to add logic
        repository = SquadRepository(Squad)
        return [item.attribute_values for item in repository.get_all()]

    def create_squad(self, body):
        # Edit if you have to add logic
        repository = SquadRepository(Squad)
        return repository.save(Squad(**body)).attribute_values
