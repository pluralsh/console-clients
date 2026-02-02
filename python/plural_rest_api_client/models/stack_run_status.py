from enum import Enum

class StackRunStatus(str, Enum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    PENDING = "pending"
    PENDING_APPROVAL = "pending_approval"
    QUEUED = "queued"
    RUNNING = "running"
    SUCCESSFUL = "successful"

    def __str__(self) -> str:
        return str(self.value)
