from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.console_open_api_access_token_scope import (
        ConsoleOpenAPIAccessTokenScope,
    )


T = TypeVar("T", bound="AccessToken")


@_attrs_define
class AccessToken:
    """An access token

    Attributes:
        id (str):
        inserted_at (datetime.datetime):
        token (str):
        expires_at (datetime.datetime | Unset):
        last_used_at (datetime.datetime | Unset):
        scopes (list[ConsoleOpenAPIAccessTokenScope] | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: str
    inserted_at: datetime.datetime
    token: str
    expires_at: datetime.datetime | Unset = UNSET
    last_used_at: datetime.datetime | Unset = UNSET
    scopes: list[ConsoleOpenAPIAccessTokenScope] | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        inserted_at = self.inserted_at.isoformat()

        token = self.token

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        last_used_at: str | Unset = UNSET
        if not isinstance(self.last_used_at, Unset):
            last_used_at = self.last_used_at.isoformat()

        scopes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.to_dict()
                scopes.append(scopes_item)

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "inserted_at": inserted_at,
                "token": token,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.console_open_api_access_token_scope import (
            ConsoleOpenAPIAccessTokenScope,
        )

        d = dict(src_dict)
        id = d.pop("id")

        inserted_at = isoparse(d.pop("inserted_at"))

        token = d.pop("token")

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        _last_used_at = d.pop("last_used_at", UNSET)
        last_used_at: datetime.datetime | Unset
        if isinstance(_last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = isoparse(_last_used_at)

        _scopes = d.pop("scopes", UNSET)
        scopes: list[ConsoleOpenAPIAccessTokenScope] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = ConsoleOpenAPIAccessTokenScope.from_dict(scopes_item_data)

                scopes.append(scopes_item)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        access_token = cls(
            id=id,
            inserted_at=inserted_at,
            token=token,
            expires_at=expires_at,
            last_used_at=last_used_at,
            scopes=scopes,
            updated_at=updated_at,
        )

        access_token.additional_properties = d
        return access_token

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
