from enum import Enum

class ListClustersCompliance(str, Enum):
    COMPLIANT = "compliant"
    LATEST = "latest"
    OUTDATED = "outdated"

    def __str__(self) -> str:
        return str(self.value)
