from modi.core.base_model import BaseModel

class Squad(BaseModel):
    """
    Squad Model
    """
    table_name = 'squads'
    key_schema = [{"AttributeName": "id", "KeyType": "HASH"}]
    attribute_definitions = [{"AttributeName": "id", "AttributeType": "S"}]
    provisioned_throughput = {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
