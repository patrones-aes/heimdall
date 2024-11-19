import uuid
import os

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Subscription(Model):
    class Meta:
        table_name = 'subscriptions'
        host = (
            os.getenv('BICIRED_DB_HOST')
            if os.getenv('ENVIRONMENT') == 'local'
            else None
        )

    id = UnicodeAttribute(
        hash_key=True,
        default_for_new=str(uuid.uuid4())
    )
    name = UnicodeAttribute(null=False)
