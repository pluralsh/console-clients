from enum import Enum


class ListSentinelsStatus(str, Enum):
    FAILED = "failed"
    PENDING = "pending"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
