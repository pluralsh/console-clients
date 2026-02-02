from enum import Enum


class GitRepositoryAuthMethod(str, Enum):
    BASIC = "basic"
    SSH = "ssh"

    def __str__(self) -> str:
        return str(self.value)
