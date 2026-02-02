from enum import Enum


class HelmRepositoryHealth(str, Enum):
    FAILED = "failed"
    PULLABLE = "pullable"

    def __str__(self) -> str:
        return str(self.value)
