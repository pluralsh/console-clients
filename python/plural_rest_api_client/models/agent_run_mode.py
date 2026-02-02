from enum import Enum

class AgentRunMode(str, Enum):
    ANALYZE = "analyze"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
