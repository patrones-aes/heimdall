from fastapi import APIRouter, Body
from fastapi_router_controller import Controller

from subscription.subscription_service import SubscriptionService

router = APIRouter(prefix='/subscriptions', tags=['Subscriptions'])
controller = Controller(router)

@controller.resource()
class SubscriptionController:
    def __init__(self):
        self.service = SubscriptionService()

    @controller.route.get('/')
    async def get_all_subscriptions(self):
        print("test 2")
        return self.service.get_all_subscriptions()

    @controller.route.post('/')
    async def create_subscription(self, body = Body()):
        return self.service.create_subscription(body)
