

from tpipes.data import Data
from tpipes.pipeline import run_pipeline
from tpipes.router import Router
from tpipes.stage import ProcessingStage, Stage



class SimpleStage1(ProcessingStage[str, str]):
    def process(self, data: Data[str]) -> Data[str]:
        data.content += "a"
        return data


class SimpleStage2(ProcessingStage[str, int]):
    def process(self, data: Data[str]) -> Data[int]:
        return Data(
            content=len(data.content),
            metadata=data.metadata
        )


def test_simple_pipeline() -> None:
    stages = (
        SimpleStage1(),
        SimpleStage2(),
    )

    router: Router[str] = Router(lambda data: 0 if len(data.content) < 10 else 1)
    router.connect(stages[0])
    router.connect(stages[1])
    input_data =Data[str]("", {}, False)
    run_pipeline(router, input_data)


if __name__ == "__main__":
    test_simple_pipeline()
    
