import redis

from modi.config.settings import settings


class RedisQueueManager:
    """
    Redis connection manager
    """

    def __init__(self) -> None:
        self.connection_pool = redis.ConnectionPool(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT
        )

    def get_connection(self) -> redis.Redis:
        """
        Create a Redis connection from the connection pool.

        Returns:
            redis.Redis: A Redis client connected to the default database (0).
        """
        return redis.StrictRedis(connection_pool=self.connection_pool)


def get_redis_connection() -> redis.Redis:
    """
    Get a Redis connection for queue operations.

    Returns:
        redis.Redis: A Redis client connected to the default database (0).
    """
    connection_manager = RedisQueueManager()
    return connection_manager.get_connection()
