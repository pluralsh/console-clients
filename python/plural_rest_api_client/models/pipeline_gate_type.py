from enum import Enum

class PipelineGateType(str, Enum):
    APPROVAL = "approval"
    JOB = "job"
    SENTINEL = "sentinel"
    WINDOW = "window"

    def __str__(self) -> str:
        return str(self.value)
