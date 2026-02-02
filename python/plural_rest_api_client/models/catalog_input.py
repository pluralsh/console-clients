from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CatalogInput")



@_attrs_define
class CatalogInput:
    """ Input for creating or updating a catalog

        Attributes:
            author (str): Author or maintainer of the catalog
            name (str): Name for the catalog
            category (str | Unset): Category for organizing the catalog
            dark_icon (str | Unset): URL or reference to the catalog's icon for dark mode
            description (str | Unset): Description of the catalog's purpose
            icon (str | Unset): URL or reference to the catalog's icon for light mode
            project_id (str | Unset): ID of the project this catalog belongs to
     """

    author: str
    name: str
    category: str | Unset = UNSET
    dark_icon: str | Unset = UNSET
    description: str | Unset = UNSET
    icon: str | Unset = UNSET
    project_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        author = self.author

        name = self.name

        category = self.category

        dark_icon = self.dark_icon

        description = self.description

        icon = self.icon

        project_id = self.project_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "author": author,
            "name": name,
        })
        if category is not UNSET:
            field_dict["category"] = category
        if dark_icon is not UNSET:
            field_dict["dark_icon"] = dark_icon
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author = d.pop("author")

        name = d.pop("name")

        category = d.pop("category", UNSET)

        dark_icon = d.pop("dark_icon", UNSET)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        project_id = d.pop("project_id", UNSET)

        catalog_input = cls(
            author=author,
            name=name,
            category=category,
            dark_icon=dark_icon,
            description=description,
            icon=icon,
            project_id=project_id,
        )


        catalog_input.additional_properties = d
        return catalog_input

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
