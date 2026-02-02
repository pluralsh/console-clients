from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Kustomize")



@_attrs_define
class Kustomize:
    """ Kustomize configuration for a service

        Attributes:
            enable_helm (bool | Unset): If true, Helm integration is enabled for Kustomize
            path (str | Unset): Path to the kustomization.yaml or kustomize directory relative to the repository root
     """

    enable_helm: bool | Unset = UNSET
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        enable_helm = self.enable_helm

        path = self.path


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if enable_helm is not UNSET:
            field_dict["enable_helm"] = enable_helm
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_helm = d.pop("enable_helm", UNSET)

        path = d.pop("path", UNSET)

        kustomize = cls(
            enable_helm=enable_helm,
            path=path,
        )


        kustomize.additional_properties = d
        return kustomize

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
