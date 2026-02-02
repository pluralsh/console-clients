from enum import Enum

class SentinelRunJobFormat(str, Enum):
    JUNIT = "junit"
    PLAINTEXT = "plaintext"

    def __str__(self) -> str:
        return str(self.value)
