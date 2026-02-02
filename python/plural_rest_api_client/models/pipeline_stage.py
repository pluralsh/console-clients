from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stage_service import StageService


T = TypeVar("T", bound="PipelineStage")


@_attrs_define
class PipelineStage:
    """A stage in the pipeline representing a deployment environment

    Attributes:
        id (str | Unset): Unique identifier for the stage
        inserted_at (datetime.datetime | Unset):
        name (str | Unset): Name of the stage (e.g., dev, staging, production)
        services (list[StageService] | Unset): Services deployed in this stage
        updated_at (datetime.datetime | Unset):
    """

    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    services: list[StageService] | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        name = self.name

        services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if name is not UNSET:
            field_dict["name"] = name
        if services is not UNSET:
            field_dict["services"] = services
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stage_service import StageService

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        name = d.pop("name", UNSET)

        _services = d.pop("services", UNSET)
        services: list[StageService] | Unset = UNSET
        if _services is not UNSET:
            services = []
            for services_item_data in _services:
                services_item = StageService.from_dict(services_item_data)

                services.append(services_item)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        pipeline_stage = cls(
            id=id,
            inserted_at=inserted_at,
            name=name,
            services=services,
            updated_at=updated_at,
        )

        pipeline_stage.additional_properties = d
        return pipeline_stage

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
