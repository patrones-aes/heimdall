from src.repository import SquadRepository

class SquadService():
    def __init__(self):
        self.repository = SquadRepository()

    def get_all_squads(self):
        # Edit if you have to add logic
        return self.repository.get_all()

    def create_squad(self, body):
        # Edit if you have to add logic
        return self.repository.create(body)
