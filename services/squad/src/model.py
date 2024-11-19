import uuid

from modi.core.base_model import BaseModel
from pynamodb.attributes import UnicodeAttribute

class Squad(BaseModel):
    """
    Squad Model
    """
    class Meta(BaseModel.Meta):
        table_name = 'squads'

    id = UnicodeAttribute(
        attr_name='id',
        hash_key=True,
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
