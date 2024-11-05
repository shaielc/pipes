from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Generator, Generic, Optional, Tuple, TypeVar
from tpipes.data import Data

T = TypeVar("T")
M = TypeVar("M")

class Stage(Generic[T,M]):
    def __init__(self, target: Optional[Stage[M, Any]]=None) -> None:
        self.target = target

    def connect(self, stage: Stage[M, Any]) -> None:
        self.target = stage
    
    @abstractmethod
    def step(self, input_data: Data[T]) -> Tuple[Data[M], Optional[Stage[M, Any]]]:
        pass


class ProcessingStage(Stage[T,M]):
    @abstractmethod
    def process(self, data: Data[T]) -> Data[M]:
        pass
    
    def step(self, input_data: Data[T]) -> Tuple[Data[M], Optional[Stage[M, Any]]]:
        current: Data[M] = self.process(input_data) 
        return current, self.target
        