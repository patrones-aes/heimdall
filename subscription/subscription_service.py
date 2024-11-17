from src.subscription.subscription_repository import SubscriptionRepository
from src.subscription.subscription_list_repository import SubscriptionListRepository

class SubscriptionService():
    def __init__(self):
        # self.repository = SubscriptionRepository()
        self.repository = SubscriptionListRepository()

    def get_all_subscriptions(self):
        # Edit if you have to add logic
        return self.repository.get_all()

    def create_subscription(self, body):
        # Edit if you have to add logic
        try:
            self.repository.create(body)
            return {'status': 'subscribed'}
        except Exception:
            return {'status': 'error'}
