import json

from typing import List, Dict, Any
from modi.redis.connection_manager import get_redis_connection
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
        item = self.repository.save(Subscription(**body)).attribute_values
        get_redis_connection().lpush(
            'subscription_created',
            json.dumps({
                'subscription_id': item.get('id'),
                'squad_id': item.get('squad_id'),
                'user_id': item.get('user_id')
            }))
        return item
