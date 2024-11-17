import uuid
import os

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class Squad(Model):
    class Meta:
        table_name = 'squads'
        host = (
            f'http://{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}'
            if os.getenv('ENVIRONMENT') == 'local'
            else None
        )

    id = UnicodeAttribute(
        hash_key=True,
        default_for_new=str(uuid.uuid4())
    )
    name = UnicodeAttribute(null=False)
