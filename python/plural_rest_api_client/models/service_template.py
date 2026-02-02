from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.git import Git
  from ..models.helm_spec import HelmSpec
  from ..models.kustomize import Kustomize





T = TypeVar("T", bound="ServiceTemplate")



@_attrs_define
class ServiceTemplate:
    """ A service template that defines how services are created from a global service

        Attributes:
            contexts (list[str] | Unset): List of service context names to include
            git (Git | Unset): Git reference configuration
            helm (HelmSpec | Unset): Helm chart configuration for a service
            id (str | Unset): Unique identifier for the service template
            inserted_at (datetime.datetime | Unset):
            kustomize (Kustomize | Unset): Kustomize configuration for a service
            name (str | Unset): Name of the service to be created from this template
            namespace (str | Unset): Kubernetes namespace for the service
            protect (bool | Unset): If true, prevents accidental deletion or modification of created services
            repository_id (str | Unset): ID of the git repository backing this template
            templated (bool | Unset): If true, the service configuration supports variable interpolation
            updated_at (datetime.datetime | Unset):
     """

    contexts: list[str] | Unset = UNSET
    git: Git | Unset = UNSET
    helm: HelmSpec | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    kustomize: Kustomize | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    protect: bool | Unset = UNSET
    repository_id: str | Unset = UNSET
    templated: bool | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.git import Git
        from ..models.helm_spec import HelmSpec
        from ..models.kustomize import Kustomize
        contexts: list[str] | Unset = UNSET
        if not isinstance(self.contexts, Unset):
            contexts = self.contexts



        git: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git, Unset):
            git = self.git.to_dict()

        helm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helm, Unset):
            helm = self.helm.to_dict()

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        kustomize: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kustomize, Unset):
            kustomize = self.kustomize.to_dict()

        name = self.name

        namespace = self.namespace

        protect = self.protect

        repository_id = self.repository_id

        templated = self.templated

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if contexts is not UNSET:
            field_dict["contexts"] = contexts
        if git is not UNSET:
            field_dict["git"] = git
        if helm is not UNSET:
            field_dict["helm"] = helm
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if kustomize is not UNSET:
            field_dict["kustomize"] = kustomize
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if protect is not UNSET:
            field_dict["protect"] = protect
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if templated is not UNSET:
            field_dict["templated"] = templated
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git import Git
        from ..models.helm_spec import HelmSpec
        from ..models.kustomize import Kustomize
        d = dict(src_dict)
        contexts = cast(list[str], d.pop("contexts", UNSET))


        _git = d.pop("git", UNSET)
        git: Git | Unset
        if isinstance(_git,  Unset):
            git = UNSET
        else:
            git = Git.from_dict(_git)




        _helm = d.pop("helm", UNSET)
        helm: HelmSpec | Unset
        if isinstance(_helm,  Unset):
            helm = UNSET
        else:
            helm = HelmSpec.from_dict(_helm)




        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        _kustomize = d.pop("kustomize", UNSET)
        kustomize: Kustomize | Unset
        if isinstance(_kustomize,  Unset):
            kustomize = UNSET
        else:
            kustomize = Kustomize.from_dict(_kustomize)




        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        protect = d.pop("protect", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        templated = d.pop("templated", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        service_template = cls(
            contexts=contexts,
            git=git,
            helm=helm,
            id=id,
            inserted_at=inserted_at,
            kustomize=kustomize,
            name=name,
            namespace=namespace,
            protect=protect,
            repository_id=repository_id,
            templated=templated,
            updated_at=updated_at,
        )


        service_template.additional_properties = d
        return service_template

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
