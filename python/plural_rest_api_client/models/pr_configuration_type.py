from enum import Enum

class PrConfigurationType(str, Enum):
    BOOL = "bool"
    BUCKET = "bucket"
    CLUSTER = "cluster"
    DOMAIN = "domain"
    ENUM = "enum"
    FILE = "file"
    FLOW = "flow"
    FUNCTION = "function"
    GROUP = "group"
    INT = "int"
    JSON = "json"
    PASSWORD = "password"
    PROJECT = "project"
    STRING = "string"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
