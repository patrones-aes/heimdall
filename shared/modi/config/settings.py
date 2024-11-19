import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings
    """
    DYNAMODB_URL: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_DEFAULT_REGION: str = 'us-east-1'

    REDIS_HOST: str
    REDIS_PORT: str


settings = Settings(
    # DynamoDB Connection Settings
    DYNAMODB_URL=os.getenv('DYNAMODB_URL'),
    AWS_ACCESS_KEY_ID=os.getenv('AWS_ACCESS_KEY_ID'),
    AWS_SECRET_ACCESS_KEY=os.getenv('AWS_SECRET_ACCESS_KEY'),
    AWS_DEFAULT_REGION=os.getenv('AWS_DEFAULT_REGION'),

    # Redis Connection Settings
    REDIS_HOST=os.getenv('REDIS_HOST'),
    REDIS_PORT=os.getenv('REDIS_PORT')
)
