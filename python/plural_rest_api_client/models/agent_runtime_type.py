from enum import Enum


class AgentRuntimeType(str, Enum):
    CLAUDE = "claude"
    CUSTOM = "custom"
    GEMINI = "gemini"
    OPENCODE = "opencode"

    def __str__(self) -> str:
        return str(self.value)
