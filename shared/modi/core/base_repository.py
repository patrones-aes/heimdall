from typing import Type, Generic, TypeVar, Dict, Any, Optional, List

from modi.core.base_model import BaseModel

ModelType = TypeVar('ModelType', bound=BaseModel)

class BaseRepository(Generic[ModelType]):
    """
    Base Repository
    """

    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    def get_all(self) -> list[ModelType]:
        """
        Get all items from the table.
        """
        return list(self.model.scan())

    def get_by_key(self, key: Dict[str, Any]) -> Optional[ModelType]:
        """
        Get an item by primary key.
        """
        try:
            return self.model.get(**key)
        except self.model.DoesNotExist:
            return None

    def save(self, instance: ModelType) -> ModelType:
        """
        Save a model instance to the table.
        """
        instance.save()
        return instance

    def delete_by_key(self, key: Dict[str, Any]) -> None:
        """
        Delete an item by primary key.
        """
        item = self.get_by_key(key)
        if item:
            item.delete()

    def query(self, key: str, value: Any) -> List[ModelType]:
        """
        Query the table by a key and value.
        """
        return list(self.model.query(value, key_condition=key))
