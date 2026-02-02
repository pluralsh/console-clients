from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.service_renderer_input_type import ServiceRendererInputType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.renderer_helm_input import RendererHelmInput





T = TypeVar("T", bound="ServiceRendererInput")



@_attrs_define
class ServiceRendererInput:
    """ Input for a custom renderer configuration

        Attributes:
            path (str): Path within the repository where this renderer applies
            type_ (ServiceRendererInputType): Type of renderer (auto, raw, helm, kustomize)
            helm (RendererHelmInput | Unset): Helm-specific configuration input for a renderer
     """

    path: str
    type_: ServiceRendererInputType
    helm: RendererHelmInput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.renderer_helm_input import RendererHelmInput
        path = self.path

        type_ = self.type_.value

        helm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helm, Unset):
            helm = self.helm.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "path": path,
            "type": type_,
        })
        if helm is not UNSET:
            field_dict["helm"] = helm

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.renderer_helm_input import RendererHelmInput
        d = dict(src_dict)
        path = d.pop("path")

        type_ = ServiceRendererInputType(d.pop("type"))




        _helm = d.pop("helm", UNSET)
        helm: RendererHelmInput | Unset
        if isinstance(_helm,  Unset):
            helm = UNSET
        else:
            helm = RendererHelmInput.from_dict(_helm)




        service_renderer_input = cls(
            path=path,
            type_=type_,
            helm=helm,
        )


        service_renderer_input.additional_properties = d
        return service_renderer_input

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
