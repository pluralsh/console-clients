from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterUpgradeInput")


@_attrs_define
class ClusterUpgradeInput:
    """Input for creating a cluster upgrade workflow

    Attributes:
        prompt (str | Unset): Optional prompt to guide the upgrade workflow
        runtime_id (str | Unset): Optional agent runtime ID to execute the upgrade
    """

    prompt: str | Unset = UNSET
    runtime_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt

        runtime_id = self.runtime_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if runtime_id is not UNSET:
            field_dict["runtime_id"] = runtime_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prompt = d.pop("prompt", UNSET)

        runtime_id = d.pop("runtime_id", UNSET)

        cluster_upgrade_input = cls(
            prompt=prompt,
            runtime_id=runtime_id,
        )

        cluster_upgrade_input.additional_properties = d
        return cluster_upgrade_input

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
