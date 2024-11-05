
from typing import Any, Generator, Optional, TypeVar
from tpipes.data import Data
from tpipes.stage import Stage

T = TypeVar("T")

def run_pipeline(stage: Stage[T, Any], input_data: Data[T]) -> Generator[Data[Any], Any, None]:
    next_stage: Optional[Stage[Any, Any]] = stage
    while next_stage is not None:
        data, next_stage = next_stage.step(input_data)
        yield data

