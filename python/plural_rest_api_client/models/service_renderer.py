from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_renderer_type import ServiceRendererType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.renderer_helm import RendererHelm


T = TypeVar("T", bound="ServiceRenderer")


@_attrs_define
class ServiceRenderer:
    """A custom renderer for processing service manifests at a specific path

    Attributes:
        helm (RendererHelm | Unset): Helm-specific configuration for a renderer
        path (str | Unset): Path within the repository where this renderer applies
        type_ (ServiceRendererType | Unset): Type of renderer (auto, raw, helm, kustomize)
    """

    helm: RendererHelm | Unset = UNSET
    path: str | Unset = UNSET
    type_: ServiceRendererType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        helm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helm, Unset):
            helm = self.helm.to_dict()

        path = self.path

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if helm is not UNSET:
            field_dict["helm"] = helm
        if path is not UNSET:
            field_dict["path"] = path
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.renderer_helm import RendererHelm

        d = dict(src_dict)
        _helm = d.pop("helm", UNSET)
        helm: RendererHelm | Unset
        if isinstance(_helm, Unset):
            helm = UNSET
        else:
            helm = RendererHelm.from_dict(_helm)

        path = d.pop("path", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ServiceRendererType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ServiceRendererType(_type_)

        service_renderer = cls(
            helm=helm,
            path=path,
            type_=type_,
        )

        service_renderer.additional_properties = d
        return service_renderer

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
