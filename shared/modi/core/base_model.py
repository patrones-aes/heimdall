from datetime import datetime, timezone
from pynamodb.models import Model
from pynamodb.attributes import UTCDateTimeAttribute
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

    created_at = UTCDateTimeAttribute(
    attr_name = 'created_at',
    default_for_new=lambda: datetime.now(timezone.utc),
    null=False
    )
    updated_at = UTCDateTimeAttribute(
        attr_name = 'updated_at',
        default_for_new=lambda: datetime.now(timezone.utc),
        null=False
    )
