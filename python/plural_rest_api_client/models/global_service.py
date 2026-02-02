from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.global_service_distro import GlobalServiceDistro
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.cascade import Cascade
  from ..models.service_template import ServiceTemplate
  from ..models.tag import Tag





T = TypeVar("T", bound="GlobalService")



@_attrs_define
class GlobalService:
    """ A global service that deploys services across clusters matching specified criteria

        Attributes:
            tags (list[Tag] | Unset): Tags used to match target clusters
            cascade (Cascade | Unset): Cascade behavior when the global service is deleted
            distro (GlobalServiceDistro | Unset): Target cluster distribution (e.g., eks, aks, gke, generic)
            id (str | Unset): Unique identifier for the global service
            inserted_at (datetime.datetime | Unset):
            interval (str | Unset): Polling interval for syncing the global service (e.g., "5m", "1h")
            mgmt (bool | Unset): If true, the global service will target the management cluster
            name (str | Unset): Name of the global service
            project_id (str | Unset): ID of the project this global service belongs to
            provider_id (str | Unset): ID of the cluster provider to filter target clusters
            reparent (bool | Unset): If true, allows reparenting of existing services owned by this global service
            service_id (str | Unset): ID of the source service to clone (mutually exclusive with template)
            template (ServiceTemplate | Unset): A service template that defines how services are created from a global
                service
            updated_at (datetime.datetime | Unset):
     """

    tags: list[Tag] | Unset = UNSET
    cascade: Cascade | Unset = UNSET
    distro: GlobalServiceDistro | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    interval: str | Unset = UNSET
    mgmt: bool | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    provider_id: str | Unset = UNSET
    reparent: bool | Unset = UNSET
    service_id: str | Unset = UNSET
    template: ServiceTemplate | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cascade import Cascade
        from ..models.service_template import ServiceTemplate
        from ..models.tag import Tag
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


        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        interval = self.interval

        mgmt = self.mgmt

        name = self.name

        project_id = self.project_id

        provider_id = self.provider_id

        reparent = self.reparent

        service_id = self.service_id

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tags is not UNSET:
            field_dict["tags"] = tags
        if cascade is not UNSET:
            field_dict["cascade"] = cascade
        if distro is not UNSET:
            field_dict["distro"] = distro
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if interval is not UNSET:
            field_dict["interval"] = interval
        if mgmt is not UNSET:
            field_dict["mgmt"] = mgmt
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if reparent is not UNSET:
            field_dict["reparent"] = reparent
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if template is not UNSET:
            field_dict["template"] = template
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cascade import Cascade
        from ..models.service_template import ServiceTemplate
        from ..models.tag import Tag
        d = dict(src_dict)
        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)



                tags.append(tags_item)


        _cascade = d.pop("cascade", UNSET)
        cascade: Cascade | Unset
        if isinstance(_cascade,  Unset):
            cascade = UNSET
        else:
            cascade = Cascade.from_dict(_cascade)




        _distro = d.pop("distro", UNSET)
        distro: GlobalServiceDistro | Unset
        if isinstance(_distro,  Unset):
            distro = UNSET
        else:
            distro = GlobalServiceDistro(_distro)




        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        interval = d.pop("interval", UNSET)

        mgmt = d.pop("mgmt", UNSET)

        name = d.pop("name", UNSET)

        project_id = d.pop("project_id", UNSET)

        provider_id = d.pop("provider_id", UNSET)

        reparent = d.pop("reparent", UNSET)

        service_id = d.pop("service_id", UNSET)

        _template = d.pop("template", UNSET)
        template: ServiceTemplate | Unset
        if isinstance(_template,  Unset):
            template = UNSET
        else:
            template = ServiceTemplate.from_dict(_template)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        global_service = cls(
            tags=tags,
            cascade=cascade,
            distro=distro,
            id=id,
            inserted_at=inserted_at,
            interval=interval,
            mgmt=mgmt,
            name=name,
            project_id=project_id,
            provider_id=provider_id,
            reparent=reparent,
            service_id=service_id,
            template=template,
            updated_at=updated_at,
        )


        global_service.additional_properties = d
        return global_service

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
