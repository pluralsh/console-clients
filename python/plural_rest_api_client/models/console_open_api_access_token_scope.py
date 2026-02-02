from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsoleOpenAPIAccessTokenScope")


@_attrs_define
class ConsoleOpenAPIAccessTokenScope:
    """A scope entry for an access token

    Attributes:
        api (str | Unset): A single API name
        apis (list[str] | Unset): API name
        identifier (str | Unset): Identifier for scoped access
        ids (list[str] | Unset): Scoped resource ids
    """

    api: str | Unset = UNSET
    apis: list[str] | Unset = UNSET
    identifier: str | Unset = UNSET
    ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api = self.api

        apis: list[str] | Unset = UNSET
        if not isinstance(self.apis, Unset):
            apis = self.apis

        identifier = self.identifier

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api is not UNSET:
            field_dict["api"] = api
        if apis is not UNSET:
            field_dict["apis"] = apis
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api = d.pop("api", UNSET)

        apis = cast(list[str], d.pop("apis", UNSET))

        identifier = d.pop("identifier", UNSET)

        ids = cast(list[str], d.pop("ids", UNSET))

        console_open_api_access_token_scope = cls(
            api=api,
            apis=apis,
            identifier=identifier,
            ids=ids,
        )

        console_open_api_access_token_scope.additional_properties = d
        return console_open_api_access_token_scope

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
