from enum import Enum


class AgentSessionType(str, Enum):
    CHAT = "chat"
    KUBERNETES = "kubernetes"
    MANIFESTS = "manifests"
    PROVISIONING = "provisioning"
    RESEARCH = "research"
    SEARCH = "search"
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
