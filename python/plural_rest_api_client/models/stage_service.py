from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.promotion_criteria import PromotionCriteria





T = TypeVar("T", bound="StageService")



@_attrs_define
class StageService:
    """ A service deployment within a pipeline stage

        Attributes:
            criteria (PromotionCriteria | Unset): Criteria for promoting a service to the next stage
            id (str | Unset): Unique identifier for the stage service
            inserted_at (datetime.datetime | Unset):
            service_id (str | Unset): ID of the deployed service
            updated_at (datetime.datetime | Unset):
     """

    criteria: PromotionCriteria | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    service_id: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_criteria import PromotionCriteria
        criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        service_id = self.service_id

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_criteria import PromotionCriteria
        d = dict(src_dict)
        _criteria = d.pop("criteria", UNSET)
        criteria: PromotionCriteria | Unset
        if isinstance(_criteria,  Unset):
            criteria = UNSET
        else:
            criteria = PromotionCriteria.from_dict(_criteria)




        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        service_id = d.pop("service_id", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        stage_service = cls(
            criteria=criteria,
            id=id,
            inserted_at=inserted_at,
            service_id=service_id,
            updated_at=updated_at,
        )


        stage_service.additional_properties = d
        return stage_service

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
