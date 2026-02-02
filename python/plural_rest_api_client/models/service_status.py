from enum import Enum


class ServiceStatus(str, Enum):
    FAILED = "failed"
    HEALTHY = "healthy"
    PAUSED = "paused"
    STALE = "stale"
    SYNCED = "synced"

    def __str__(self) -> str:
        return str(self.value)
