from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RendererHelmInput")


@_attrs_define
class RendererHelmInput:
    """Helm-specific configuration input for a renderer

    Attributes:
        ignore_hooks (bool | Unset): Whether to ignore Helm hooks when rendering
        release (str | Unset): Helm release name to use when rendering
        values (str | Unset): Helm values file content to use when rendering
        values_files (list[str] | Unset): List of relative paths to values files
    """

    ignore_hooks: bool | Unset = UNSET
    release: str | Unset = UNSET
    values: str | Unset = UNSET
    values_files: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ignore_hooks = self.ignore_hooks

        release = self.release

        values = self.values

        values_files: list[str] | Unset = UNSET
        if not isinstance(self.values_files, Unset):
            values_files = self.values_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ignore_hooks is not UNSET:
            field_dict["ignore_hooks"] = ignore_hooks
        if release is not UNSET:
            field_dict["release"] = release
        if values is not UNSET:
            field_dict["values"] = values
        if values_files is not UNSET:
            field_dict["values_files"] = values_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ignore_hooks = d.pop("ignore_hooks", UNSET)

        release = d.pop("release", UNSET)

        values = d.pop("values", UNSET)

        values_files = cast(list[str], d.pop("values_files", UNSET))

        renderer_helm_input = cls(
            ignore_hooks=ignore_hooks,
            release=release,
            values=values,
            values_files=values_files,
        )

        renderer_helm_input.additional_properties = d
        return renderer_helm_input

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
