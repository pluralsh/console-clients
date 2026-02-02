from enum import Enum


class ClusterDistro(str, Enum):
    AKS = "aks"
    EKS = "eks"
    GENERIC = "generic"
    GKE = "gke"
    K3S = "k3s"
    OPENSHIFT = "openshift"
    RKE = "rke"

    def __str__(self) -> str:
        return str(self.value)
