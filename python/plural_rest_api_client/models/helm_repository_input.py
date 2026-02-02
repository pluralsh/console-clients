from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.helm_repository_input_provider import HelmRepositoryInputProvider
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.helm_repository_input_auth import HelmRepositoryInputAuth





T = TypeVar("T", bound="HelmRepositoryInput")



@_attrs_define
class HelmRepositoryInput:
    """ Input for upserting a helm repository

        Attributes:
            auth (HelmRepositoryInputAuth | Unset): Authentication configuration for the helm repository
            provider (HelmRepositoryInputProvider | Unset):
            url (str | Unset): The url of the helm repository
     """

    auth: HelmRepositoryInputAuth | Unset = UNSET
    provider: HelmRepositoryInputProvider | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.helm_repository_input_auth import HelmRepositoryInputAuth
        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value


        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if auth is not UNSET:
            field_dict["auth"] = auth
        if provider is not UNSET:
            field_dict["provider"] = provider
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.helm_repository_input_auth import HelmRepositoryInputAuth
        d = dict(src_dict)
        _auth = d.pop("auth", UNSET)
        auth: HelmRepositoryInputAuth | Unset
        if isinstance(_auth,  Unset):
            auth = UNSET
        else:
            auth = HelmRepositoryInputAuth.from_dict(_auth)




        _provider = d.pop("provider", UNSET)
        provider: HelmRepositoryInputProvider | Unset
        if isinstance(_provider,  Unset):
            provider = UNSET
        else:
            provider = HelmRepositoryInputProvider(_provider)




        url = d.pop("url", UNSET)

        helm_repository_input = cls(
            auth=auth,
            provider=provider,
            url=url,
        )


        helm_repository_input.additional_properties = d
        return helm_repository_input

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
