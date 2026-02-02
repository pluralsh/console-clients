from enum import Enum


class PipelineGateState(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    PENDING = "pending"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
