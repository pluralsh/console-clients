from enum import Enum


class AgentRunInputMode(str, Enum):
    ANALYZE = "analyze"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
