from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.global_service_input_distro import GlobalServiceInputDistro
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cascade_input import CascadeInput
  from ..models.service_template_input import ServiceTemplateInput
  from ..models.tag_input import TagInput





T = TypeVar("T", bound="GlobalServiceInput")



@_attrs_define
class GlobalServiceInput:
    """ Input for creating or updating a global service

        Attributes:
            name (str): Name for the global service
            tags (list[TagInput] | Unset): Tags used to match target clusters
            cascade (CascadeInput | Unset): Input for cascade behavior when the global service is deleted
            distro (GlobalServiceInputDistro | Unset): Target cluster distribution
            interval (str | Unset): Polling interval for syncing (e.g., "5m", "1h")
            mgmt (bool | Unset): If true, target the management cluster
            project_id (str | Unset): ID of the project this global service belongs to
            provider_id (str | Unset): ID of the cluster provider to filter target clusters
            reparent (bool | Unset): If true, allows reparenting of existing services
            template (ServiceTemplateInput | Unset): Input for a service template configuration
     """

    name: str
    tags: list[TagInput] | Unset = UNSET
    cascade: CascadeInput | Unset = UNSET
    distro: GlobalServiceInputDistro | Unset = UNSET
    interval: str | Unset = UNSET
    mgmt: bool | Unset = UNSET
    project_id: str | Unset = UNSET
    provider_id: str | Unset = UNSET
    reparent: bool | Unset = UNSET
    template: ServiceTemplateInput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tag_input import TagInput
        from ..models.service_template_input import ServiceTemplateInput
        from ..models.cascade_input import CascadeInput
        name = self.name

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)



        cascade: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cascade, Unset):
            cascade = self.cascade.to_dict()

        distro: str | Unset = UNSET
        if not isinstance(self.distro, Unset):
            distro = self.distro.value


        interval = self.interval

        mgmt = self.mgmt

        project_id = self.project_id

        provider_id = self.provider_id

        reparent = self.reparent

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if tags is not UNSET:
            field_dict["tags"] = tags
        if cascade is not UNSET:
            field_dict["cascade"] = cascade
        if distro is not UNSET:
            field_dict["distro"] = distro
        if interval is not UNSET:
            field_dict["interval"] = interval
        if mgmt is not UNSET:
            field_dict["mgmt"] = mgmt
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if reparent is not UNSET:
            field_dict["reparent"] = reparent
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cascade_input import CascadeInput
        from ..models.service_template_input import ServiceTemplateInput
        from ..models.tag_input import TagInput
        d = dict(src_dict)
        name = d.pop("name")

        _tags = d.pop("tags", UNSET)
        tags: list[TagInput] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = TagInput.from_dict(tags_item_data)



                tags.append(tags_item)


        _cascade = d.pop("cascade", UNSET)
        cascade: CascadeInput | Unset
        if isinstance(_cascade,  Unset):
            cascade = UNSET
        else:
            cascade = CascadeInput.from_dict(_cascade)




        _distro = d.pop("distro", UNSET)
        distro: GlobalServiceInputDistro | Unset
        if isinstance(_distro,  Unset):
            distro = UNSET
        else:
            distro = GlobalServiceInputDistro(_distro)




        interval = d.pop("interval", UNSET)

        mgmt = d.pop("mgmt", UNSET)

        project_id = d.pop("project_id", UNSET)

        provider_id = d.pop("provider_id", UNSET)

        reparent = d.pop("reparent", UNSET)

        _template = d.pop("template", UNSET)
        template: ServiceTemplateInput | Unset
        if isinstance(_template,  Unset):
            template = UNSET
        else:
            template = ServiceTemplateInput.from_dict(_template)




        global_service_input = cls(
            name=name,
            tags=tags,
            cascade=cascade,
            distro=distro,
            interval=interval,
            mgmt=mgmt,
            project_id=project_id,
            provider_id=provider_id,
            reparent=reparent,
            template=template,
        )


        global_service_input.additional_properties = d
        return global_service_input

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
