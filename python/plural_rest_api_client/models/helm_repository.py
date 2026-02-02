from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.helm_repository_health import HelmRepositoryHealth
from ..models.helm_repository_provider import HelmRepositoryProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="HelmRepository")


@_attrs_define
class HelmRepository:
    """A helm repository

    Attributes:
        error (str | Unset): The error message for the helm repository's last pull attempt
        health (HelmRepositoryHealth | Unset):
        id (str | Unset):
        inserted_at (datetime.datetime | Unset):
        provider (HelmRepositoryProvider | Unset):
        pulled_at (datetime.datetime | Unset): The last successful pull timestamp
        updated_at (datetime.datetime | Unset):
        url (str | Unset): The url of the helm repository
    """

    error: str | Unset = UNSET
    health: HelmRepositoryHealth | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    provider: HelmRepositoryProvider | Unset = UNSET
    pulled_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        health: str | Unset = UNSET
        if not isinstance(self.health, Unset):
            health = self.health.value

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        pulled_at: str | Unset = UNSET
        if not isinstance(self.pulled_at, Unset):
            pulled_at = self.pulled_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if health is not UNSET:
            field_dict["health"] = health
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if provider is not UNSET:
            field_dict["provider"] = provider
        if pulled_at is not UNSET:
            field_dict["pulled_at"] = pulled_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error", UNSET)

        _health = d.pop("health", UNSET)
        health: HelmRepositoryHealth | Unset
        if isinstance(_health, Unset):
            health = UNSET
        else:
            health = HelmRepositoryHealth(_health)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        _provider = d.pop("provider", UNSET)
        provider: HelmRepositoryProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = HelmRepositoryProvider(_provider)

        _pulled_at = d.pop("pulled_at", UNSET)
        pulled_at: datetime.datetime | Unset
        if isinstance(_pulled_at, Unset):
            pulled_at = UNSET
        else:
            pulled_at = isoparse(_pulled_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        url = d.pop("url", UNSET)

        helm_repository = cls(
            error=error,
            health=health,
            id=id,
            inserted_at=inserted_at,
            provider=provider,
            pulled_at=pulled_at,
            updated_at=updated_at,
            url=url,
        )

        helm_repository.additional_properties = d
        return helm_repository

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
