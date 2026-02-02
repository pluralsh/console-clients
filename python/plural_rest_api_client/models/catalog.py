from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Catalog")


@_attrs_define
class Catalog:
    """A catalog of PR automations for self-service deployment workflows

    Attributes:
        author (str | Unset): Author or maintainer of the catalog
        category (str | Unset): Category for organizing catalogs (e.g., infrastructure, applications)
        dark_icon (str | Unset): URL or reference to the catalog's icon for dark mode
        description (str | Unset): Description of the catalog's purpose and contents
        icon (str | Unset): URL or reference to the catalog's icon for light mode
        id (str | Unset): Unique identifier for the catalog
        inserted_at (datetime.datetime | Unset):
        name (str | Unset): Name of the catalog
        project_id (str | Unset): ID of the project this catalog belongs to
        updated_at (datetime.datetime | Unset):
    """

    author: str | Unset = UNSET
    category: str | Unset = UNSET
    dark_icon: str | Unset = UNSET
    description: str | Unset = UNSET
    icon: str | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        category = self.category

        dark_icon = self.dark_icon

        description = self.description

        icon = self.icon

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        name = self.name

        project_id = self.project_id

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if category is not UNSET:
            field_dict["category"] = category
        if dark_icon is not UNSET:
            field_dict["dark_icon"] = dark_icon
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author = d.pop("author", UNSET)

        category = d.pop("category", UNSET)

        dark_icon = d.pop("dark_icon", UNSET)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        name = d.pop("name", UNSET)

        project_id = d.pop("project_id", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        catalog = cls(
            author=author,
            category=category,
            dark_icon=dark_icon,
            description=description,
            icon=icon,
            id=id,
            inserted_at=inserted_at,
            name=name,
            project_id=project_id,
            updated_at=updated_at,
        )

        catalog.additional_properties = d
        return catalog

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
