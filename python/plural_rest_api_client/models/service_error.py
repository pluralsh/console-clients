from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceError")


@_attrs_define
class ServiceError:
    """An error reported by the deployment operator during service sync

    Attributes:
        message (str | Unset): Error message describing what went wrong
        source (str | Unset): Source of the error (e.g., component name or sync stage)
        warning (bool | Unset): If true, this is a warning rather than a fatal error
    """

    message: str | Unset = UNSET
    source: str | Unset = UNSET
    warning: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        source = self.source

        warning = self.warning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if source is not UNSET:
            field_dict["source"] = source
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        source = d.pop("source", UNSET)

        warning = d.pop("warning", UNSET)

        service_error = cls(
            message=message,
            source=source,
            warning=warning,
        )

        service_error.additional_properties = d
        return service_error

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
