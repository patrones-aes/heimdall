from src.model import Squad
from shared.lib.base_repository import BaseRepository

class SquadRepository:
    def __init__(self):
        if not Squad.exists():
            Squad.create_table(
                read_capacity_units=1,
                write_capacity_units=1,
                wait=True
            )

    def get_all(self):
        return list(Squad.scan())

    def create(self, body):
        new_subscription = Squad(**body)
        new_subscription.save()
        return new_subscription.get_attributes()
