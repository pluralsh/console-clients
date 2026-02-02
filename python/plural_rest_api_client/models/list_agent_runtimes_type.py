from enum import Enum


class ListAgentRuntimesType(str, Enum):
    CLAUDE = "claude"
    CUSTOM = "custom"
    GEMINI = "gemini"
    OPENCODE = "opencode"

    def __str__(self) -> str:
        return str(self.value)
