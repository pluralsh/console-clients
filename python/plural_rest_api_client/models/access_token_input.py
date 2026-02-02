from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.console_open_api_access_token_scope import ConsoleOpenAPIAccessTokenScope





T = TypeVar("T", bound="AccessTokenInput")



@_attrs_define
class AccessTokenInput:
    """ Input for creating a service account access token

        Attributes:
            expiry (str | Unset): Token TTL, e.g. 1h, 1d, 1w
            scopes (list[ConsoleOpenAPIAccessTokenScope] | Unset):
     """

    expiry: str | Unset = UNSET
    scopes: list[ConsoleOpenAPIAccessTokenScope] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.console_open_api_access_token_scope import ConsoleOpenAPIAccessTokenScope
        expiry = self.expiry

        scopes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.to_dict()
                scopes.append(scopes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if expiry is not UNSET:
            field_dict["expiry"] = expiry
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.console_open_api_access_token_scope import ConsoleOpenAPIAccessTokenScope
        d = dict(src_dict)
        expiry = d.pop("expiry", UNSET)

        _scopes = d.pop("scopes", UNSET)
        scopes: list[ConsoleOpenAPIAccessTokenScope] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = ConsoleOpenAPIAccessTokenScope.from_dict(scopes_item_data)



                scopes.append(scopes_item)


        access_token_input = cls(
            expiry=expiry,
            scopes=scopes,
        )


        access_token_input.additional_properties = d
        return access_token_input

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
