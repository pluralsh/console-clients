from enum import Enum


class HelmRepositoryInputProvider(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    BASIC = "basic"
    BEARER = "bearer"
    GCP = "gcp"

    def __str__(self) -> str:
        return str(self.value)
