from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HelmRepositoryInputAuthAzure")


@_attrs_define
class HelmRepositoryInputAuthAzure:
    """Azure credentials for ACR

    Attributes:
        client_id (str | Unset): Azure client ID
        client_secret (str | Unset): Azure client secret
        subscription_id (str | Unset): Azure subscription ID
        tenant_id (str | Unset): Azure tenant ID
    """

    client_id: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    subscription_id: str | Unset = UNSET
    tenant_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        subscription_id = self.subscription_id

        tenant_id = self.tenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        subscription_id = d.pop("subscription_id", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        helm_repository_input_auth_azure = cls(
            client_id=client_id,
            client_secret=client_secret,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
        )

        helm_repository_input_auth_azure.additional_properties = d
        return helm_repository_input_auth_azure

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
