from enum import Enum


class ClusterUpgradeStepType(str, Enum):
    ADDON = "addon"
    CLOUD_ADDON = "cloud_addon"
    INFRASTRUCTURE = "infrastructure"

    def __str__(self) -> str:
        return str(self.value)
