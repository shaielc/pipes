from abc import abstractmethod
from tpipes.data import Data
from typing import Any, Optional, Sequence, TypeVar, Dict, Sequence, Callable
from tpipes.stage import Stage

T = TypeVar("T")


class Router(Stage[T,T]):
    def __init__(self, router_func: Callable[[Data[T]], int], routes: Optional[Sequence[Stage[T, Any]]] = None, ) -> None:
        if routes is None:
            routes = tuple()
        
        self.routes: Dict[int, Stage[T, Any]] = {}
        self.func = router_func
        for i, route in enumerate(routes):
            self.connect(stage=route, i=i)

    def connect(self, stage: Stage[T, Any], i: int=0) -> None:
        self.routes[i] = stage
    
    def route(self, data: Data[T]) -> Stage[T, Any]:
        return self.routes[self.func(data)]

    def step(self, data: Data[T]) -> tuple[Data[T], Stage[T, Any]]:
        target = self.route(data)
        return data, target