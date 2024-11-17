from typing import Type, Generic, TypeVar, Dict, Any, Optional

from core.database.connection import DatabaseConnection
from core.base_model import BaseModel

ModelType = TypeVar('ModelType', bound=BaseModel)

class BaseRepository(Generic[ModelType]):
    """
    Base Repository
    """
    connection: DatabaseConnection

    def __init__(self,
                 model: Type[ModelType],
                 connection: DatabaseConnection) -> None:
        self.model = model
        self.connection = connection

    def get_all(self) -> list[ModelType]:
        """Get all items from the table."""
        response = self.connection.scan_table()
        return [
            self.model.from_dict(item)
            for item in response.get("Items", [])]

    def get_by_key(self, key: Dict[str, Any]) -> Optional[ModelType]:
        """Get an item by primary key."""
        response = self.connection.get_item(key)
        item = response.get("Item")
        if item:
            return self.model.from_dict(item)
        return None

    def save(self, instance: ModelType) -> Dict[str, Any]:
        """Save a model instance to the table."""
        return self.connection.put_item(instance.to_dict())

    def delete_by_key(self, key: Dict[str, Any]) -> Dict[str, Any]:
        """Delete an item by primary key."""
        return self.connection.delete_item(key)
