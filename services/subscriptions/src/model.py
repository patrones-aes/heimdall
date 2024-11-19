import uuid

from modi.core.base_model import BaseModel
from pynamodb.attributes import UnicodeAttribute

class Subscription(BaseModel):
    """
    Subscription Model
    """
    class Meta(BaseModel.Meta):
        table_name = 'subscriptions'

    id = UnicodeAttribute(
        hash_key=True,
        attr_name='id',
        default_for_new=str(uuid.uuid4())
    )
    squad_id = UnicodeAttribute(
        attr_name='squad_id',
        null=False
    )
    user_id = UnicodeAttribute(
        attr_name='user_id',
        null=False
    )
