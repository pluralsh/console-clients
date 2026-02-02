from enum import Enum


class StackInputType(str, Enum):
    ANSIBLE = "ansible"
    CUSTOM = "custom"
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
