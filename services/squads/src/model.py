import uuid

from modi.core.base_model import BaseModel
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

class Squad(BaseModel):
    """
    Squad Model
    """
    class Meta(BaseModel.Meta):
        table_name = 'squads'

    id = UnicodeAttribute(
        hash_key=True,
        attr_name='id',
        default_for_new=str(uuid.uuid4())
    )
    name = UnicodeAttribute(
        attr_name='name',
        null=False
    )
    details = UnicodeAttribute(
        attr_name='details',
        null=False
    )
    price = NumberAttribute(
        attr_name='price',
        null=False
    )
