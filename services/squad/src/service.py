from typing import List, Dict, Any
from repository import SquadRepository
from model import Squad

class SquadService():
    def __init__(self):
        self.repository = SquadRepository(Squad)

    def get_all_squads(self) -> List[Dict[str, Any]]:
        return [item.attribute_values for item in self.repository.get_all()]

    def get_squad_by_id(self, hash_key: str) -> Dict[str, Any]:
        return self.repository.get_by_hash_key(hash_key).attribute_values

    def create_squad(self, body) -> Dict[str, Any]:
        return self.repository.save(Squad(**body)).attribute_values
