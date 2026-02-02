from enum import Enum


class ServiceRendererType(str, Enum):
    AUTO = "auto"
    HELM = "helm"
    KUSTOMIZE = "kustomize"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)
