from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Cascade")


@_attrs_define
class Cascade:
    """Cascade behavior when the global service is deleted

    Attributes:
        delete (bool | Unset): If true, cascade delete all services owned by this global service
        detach (bool | Unset): If true, immediately detach services from the database without draining
    """

    delete: bool | Unset = UNSET
    detach: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete = self.delete

        detach = self.detach

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete is not UNSET:
            field_dict["delete"] = delete
        if detach is not UNSET:
            field_dict["detach"] = detach

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete = d.pop("delete", UNSET)

        detach = d.pop("detach", UNSET)

        cascade = cls(
            delete=delete,
            detach=detach,
        )

        cascade.additional_properties = d
        return cascade

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
