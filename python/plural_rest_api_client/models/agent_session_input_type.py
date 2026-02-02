from enum import Enum

class AgentSessionInputType(str, Enum):
    KUBERNETES = "kubernetes"
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
