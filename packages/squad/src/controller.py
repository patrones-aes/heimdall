from fastapi import APIRouter, Body, Depends
from fastapi_router_controller import Controller
from modi.core.database.connection import DatabaseConnection
from modi.deps import get_database

from service import SquadService
from model import Squad

router = APIRouter(prefix='/squads', tags=['Squads'])
controller = Controller(router)

@controller.resource()
class SquadController:
    def __init__(self,
                 database: DatabaseConnection = Depends(get_database(Squad))) -> None:
        self.service = SquadService(database)

    @controller.route.get('/')
    async def get_all_squads(self):
        return self.service.get_all_squads()

    @controller.route.post('/')
    async def create_squads(self, body = Body()):
        return self.service.create_squad(body)
