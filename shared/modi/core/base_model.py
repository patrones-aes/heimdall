from pynamodb.models import Model
from modi.config.settings import settings

class BaseModel(Model):
    """
    Base Model
    """
    class Meta:
        host = settings.DYNAMODB_URL
        aws_access_key_id = settings.AWS_ACCESS_KEY_ID
        aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY
        region = settings.AWS_DEFAULT_REGION
