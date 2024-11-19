import json

from typing import Dict, Any
from modi.redis.connection_manager import get_redis_connection

from repository import SquadRepository
from model import Squad


def start_events_listening() -> None:
    while True:
        message = get_redis_connection().brpop('subscription_created')
        handle_subscription_creation(json.loads(message[1].decode('UTF-8')))


def handle_subscription_creation(event: Dict[str, Any]) -> None:
    repository = SquadRepository(Squad)
    item = repository.get_by_hash_key(event.get('squad_id'))
    get_redis_connection().lpush('squad_validated', json.dumps(
        {
            'subscription_id': event.get('subscription_id'),
            'squad_id': event.get('squad_id'),
            'is_valid': bool(item)
        }
    ))
