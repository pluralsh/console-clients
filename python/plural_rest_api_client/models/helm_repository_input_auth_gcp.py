from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HelmRepositoryInputAuthGcp")


@_attrs_define
class HelmRepositoryInputAuthGcp:
    """GCP credentials for GCR/Artifact Registry

    Attributes:
        application_credentials (str | Unset): GCP service account JSON credentials
    """

    application_credentials: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_credentials = self.application_credentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_credentials is not UNSET:
            field_dict["application_credentials"] = application_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_credentials = d.pop("application_credentials", UNSET)

        helm_repository_input_auth_gcp = cls(
            application_credentials=application_credentials,
        )

        helm_repository_input_auth_gcp.additional_properties = d
        return helm_repository_input_auth_gcp

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
