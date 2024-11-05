from dataclasses import dataclass
from typing import Dict, Generic, TypeVar, Any

T = TypeVar("T")

@dataclass
class Data(Generic[T]):
    content: T
    metadata: Dict[str, Any]
    error: bool = False # Content should be an error if set to true
    

