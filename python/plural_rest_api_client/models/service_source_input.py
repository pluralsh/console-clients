from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git import Git


T = TypeVar("T", bound="ServiceSourceInput")


@_attrs_define
class ServiceSourceInput:
    """Input for an additional source repository

    Attributes:
        git (Git | Unset): Git reference configuration
        path (str | Unset): Subdirectory path where this source will live in the final tarball
        repository_id (str | Unset): ID of the git repository to source from
    """

    git: Git | Unset = UNSET
    path: str | Unset = UNSET
    repository_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        git: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git, Unset):
            git = self.git.to_dict()

        path = self.path

        repository_id = self.repository_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if git is not UNSET:
            field_dict["git"] = git
        if path is not UNSET:
            field_dict["path"] = path
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git import Git

        d = dict(src_dict)
        _git = d.pop("git", UNSET)
        git: Git | Unset
        if isinstance(_git, Unset):
            git = UNSET
        else:
            git = Git.from_dict(_git)

        path = d.pop("path", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        service_source_input = cls(
            git=git,
            path=path,
            repository_id=repository_id,
        )

        service_source_input.additional_properties = d
        return service_source_input

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
