from enum import Enum


class SentinelCheckType(str, Enum):
    INTEGRATION_TEST = "integration_test"
    KUBERNETES = "kubernetes"
    LOG = "log"

    def __str__(self) -> str:
        return str(self.value)
