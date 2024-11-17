from typing import Dict, Any

class BaseModel:
    """
    Base Model
    """
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
