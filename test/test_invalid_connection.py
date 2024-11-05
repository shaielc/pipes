from tpipes.data import Data
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
    
def test_invalid_pipeline() -> None:
    stage1: SimpleStage1 = SimpleStage1()
    stage2: SimpleStage2 = SimpleStage2()
    # Next line should be marked as an error by mypy:
    stage2.connect(stage1)


if __name__ == "__main__":
    test_invalid_pipeline()