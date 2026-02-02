from enum import Enum


class ScmConnectionType(str, Enum):
    AZURE_DEVOPS = "azure_devops"
    BITBUCKET = "bitbucket"
    BITBUCKET_DATACENTER = "bitbucket_datacenter"
    GITHUB = "github"
    GITLAB = "gitlab"

    def __str__(self) -> str:
        return str(self.value)
