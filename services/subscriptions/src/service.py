from typing import List, Dict, Any
from repository import SubscriptionRepository
from model import Subscription

class SubscriptionService():
    def __init__(self):
        self.repository = SubscriptionRepository(Subscription)

    def get_all_subscriptions(self) -> List[Dict[str, Any]]:
        return [item.attribute_values for item in self.repository.get_all()]

    def get_subscription_by_id(self, hash_key: str) -> Dict[str, Any]:
        return self.repository.get_by_hash_key(hash_key).attribute_values

    def create_subscription(self, body) -> Dict[str, Any]:
        return self.repository.save(Subscription(**body)).attribute_values
