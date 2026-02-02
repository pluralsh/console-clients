from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sentinel_check_type import SentinelCheckType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SentinelCheck")


@_attrs_define
class SentinelCheck:
    """A specific monitoring check within a sentinel

    Attributes:
        id (str | Unset): Unique identifier for the check
        name (str | Unset): Name of this check
        rule_file (str | Unset): Path to the rule file for this check within the repository
        type_ (SentinelCheckType | Unset): Type of check (log, kubernetes, integration_test)
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    rule_file: str | Unset = UNSET
    type_: SentinelCheckType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        rule_file = self.rule_file

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if rule_file is not UNSET:
            field_dict["rule_file"] = rule_file
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rule_file = d.pop("rule_file", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SentinelCheckType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SentinelCheckType(_type_)

        sentinel_check = cls(
            id=id,
            name=name,
            rule_file=rule_file,
            type_=type_,
        )

        sentinel_check.additional_properties = d
        return sentinel_check

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
