from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.git import Git
  from ..models.helm_spec_input import HelmSpecInput
  from ..models.kustomize_input import KustomizeInput





T = TypeVar("T", bound="ServiceTemplateInput")



@_attrs_define
class ServiceTemplateInput:
    """ Input for a service template configuration

        Attributes:
            name (str): Name of the service to be created from this template
            namespace (str): Kubernetes namespace for the service
            contexts (list[str] | Unset): List of service context names to include
            git (Git | Unset): Git reference configuration
            helm (HelmSpecInput | Unset): Helm chart configuration input
            kustomize (KustomizeInput | Unset): Kustomize configuration input
            protect (bool | Unset): If true, prevent accidental deletion or modification
            repository_id (str | Unset): ID of the git repository backing this template
            templated (bool | Unset): If true, enable variable interpolation in service configuration
     """

    name: str
    namespace: str
    contexts: list[str] | Unset = UNSET
    git: Git | Unset = UNSET
    helm: HelmSpecInput | Unset = UNSET
    kustomize: KustomizeInput | Unset = UNSET
    protect: bool | Unset = UNSET
    repository_id: str | Unset = UNSET
    templated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.git import Git
        from ..models.kustomize_input import KustomizeInput
        from ..models.helm_spec_input import HelmSpecInput
        name = self.name

        namespace = self.namespace

        contexts: list[str] | Unset = UNSET
        if not isinstance(self.contexts, Unset):
            contexts = self.contexts



        git: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git, Unset):
            git = self.git.to_dict()

        helm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helm, Unset):
            helm = self.helm.to_dict()

        kustomize: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kustomize, Unset):
            kustomize = self.kustomize.to_dict()

        protect = self.protect

        repository_id = self.repository_id

        templated = self.templated


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "namespace": namespace,
        })
        if contexts is not UNSET:
            field_dict["contexts"] = contexts
        if git is not UNSET:
            field_dict["git"] = git
        if helm is not UNSET:
            field_dict["helm"] = helm
        if kustomize is not UNSET:
            field_dict["kustomize"] = kustomize
        if protect is not UNSET:
            field_dict["protect"] = protect
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if templated is not UNSET:
            field_dict["templated"] = templated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git import Git
        from ..models.helm_spec_input import HelmSpecInput
        from ..models.kustomize_input import KustomizeInput
        d = dict(src_dict)
        name = d.pop("name")

        namespace = d.pop("namespace")

        contexts = cast(list[str], d.pop("contexts", UNSET))


        _git = d.pop("git", UNSET)
        git: Git | Unset
        if isinstance(_git,  Unset):
            git = UNSET
        else:
            git = Git.from_dict(_git)




        _helm = d.pop("helm", UNSET)
        helm: HelmSpecInput | Unset
        if isinstance(_helm,  Unset):
            helm = UNSET
        else:
            helm = HelmSpecInput.from_dict(_helm)




        _kustomize = d.pop("kustomize", UNSET)
        kustomize: KustomizeInput | Unset
        if isinstance(_kustomize,  Unset):
            kustomize = UNSET
        else:
            kustomize = KustomizeInput.from_dict(_kustomize)




        protect = d.pop("protect", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        templated = d.pop("templated", UNSET)

        service_template_input = cls(
            name=name,
            namespace=namespace,
            contexts=contexts,
            git=git,
            helm=helm,
            kustomize=kustomize,
            protect=protect,
            repository_id=repository_id,
            templated=templated,
        )


        service_template_input.additional_properties = d
        return service_template_input

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
