from enum import Enum

class AgentRunLanguage(str, Enum):
    CPP = "cpp"
    CSHARP = "csharp"
    GO = "go"
    JAVA = "java"
    JAVASCRIPT = "javascript"
    PHP = "php"
    PYTHON = "python"
    RUBY = "ruby"
    TERRAFORM = "terraform"

    def __str__(self) -> str:
        return str(self.value)
