from typing import List, Dict, Any
from fastapi import APIRouter, Body
from fastapi_router_controller import Controller

from service import SquadService

router = APIRouter(prefix='/squads', tags=['Squads'])
controller = Controller(router)

@controller.resource()
class SquadController:
    def __init__(self) -> None:
        self.service = SquadService()

    @controller.route.get('/')
    async def get_all_squads(self) -> List[Dict[str, Any]]:
        return self.service.get_all_squads()

    @controller.route.post('/')
    async def create_squads(self, body = Body()):
        return self.service.create_squad(body)
