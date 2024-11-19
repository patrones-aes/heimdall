import json

from typing import Dict, Any
from modi.redis.connection_manager import get_redis_connection

from repository import SubscriptionRepository
from model import Subscription


def start_events_listening() -> None:
    while True:
        message = get_redis_connection().brpop('squad_validated')
        handle_squad_validation(json.loads(message[1].decode('UTF-8')))


def handle_squad_validation(event: Dict[str, Any]) -> None:
    repository = SubscriptionRepository(Subscription)
    item = repository.get_by_hash_key(event.get('subscription_id'))
    item.update(actions=[
        Subscription.status.set(
            'ACTIVE' if event.get('is_valid') else 'INACTIVE')
    ])
