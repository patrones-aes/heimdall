from typing import Dict, Any, List

class BaseModel:
    """
    Base Model
    """
    table_name: str
    key_schema: List[Dict[str, Any]]
    attribute_definitions: List[Dict[str, Any]]
    provisioned_throughput: Dict[str, int]

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self) -> Dict[str, Any]:
        """
        Transforms a model instance into a dictionary.
        """
        return self.__dict__

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseModel':
        """
        Create a model instance from a dictionary.
        """
        return cls(**data)
    
    @classmethod
    def get_table_metadata(cls) -> Dict[str, Any]:
        """
        Get table metadata for table creation.
        """
        if not hasattr(cls, 'table_name') or not hasattr(cls, 'key_schema') or not hasattr(cls, 'attribute_definitions') or not hasattr(cls, 'provisioned_throughput'):
            raise ValueError("Model must define table metadata attributes: table_name, key_schema, attribute_definitions, provisioned_throughput.")
        
        return {
            "TableName": cls.table_name,
            "KeySchema": cls.key_schema,
            "AttributeDefinitions": cls.attribute_definitions,
            "ProvisionedThroughput": cls.provisioned_throughput,
        }
