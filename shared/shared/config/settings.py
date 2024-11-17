import os

class Settings:
    """
    Settings
    """
    DYNAMODB_HOST: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_DEFAULT_REGION: str = 'us-east-1'

settings = Settings(
    DYNAMODB_HOST=os.getenv('DYNAMODB_HOST'),
    AWS_ACCESS_KEY_ID=os.getenv('AWS_ACCESS_KEY_ID'),
    AWS_SECRET_ACCESS_KEY=os.getenv('AWS_SECRET_ACCESS_KEY'),
    AWS_DEFAULR_REGION=os.getenv('AWS_DEFAULT_REGION'),
)
