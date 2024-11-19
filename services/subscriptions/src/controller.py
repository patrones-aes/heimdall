from typing import List, Dict, Any
from fastapi import APIRouter, Body
from fastapi_router_controller import Controller

from service import SubscriptionService

router = APIRouter(prefix='/subscriptions', tags=['Subscriptions'])
controller = Controller(router)

@controller.resource()
class SubscriptionController:
    def __init__(self) -> None:
        self.service = SubscriptionService()

    @controller.route.get('/')
    async def get_all_subscriptions(self) -> List[Dict[str, Any]]:
        return self.service.get_all_subscriptions()

    @controller.route.get('/{hash_key}')
    async def get_subscription_by_id(self, hash_key: str) -> Dict[str, Any]:
        return self.service.get_subscription_by_id(hash_key)

    @controller.route.post('/')
    async def create_subscriptions(self, body = Body()) -> Dict[str, Any]:
        return self.service.create_subscription(body)
