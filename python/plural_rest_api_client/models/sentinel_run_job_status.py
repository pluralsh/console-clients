from enum import Enum

class SentinelRunJobStatus(str, Enum):
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
