from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PromotionCriteria")


@_attrs_define
class PromotionCriteria:
    """Criteria for promoting a service to the next stage

    Attributes:
        id (str | Unset): Unique identifier for the promotion criteria
        inserted_at (datetime.datetime | Unset):
        pr_automation_id (str | Unset): ID of the PR automation to trigger on promotion
        repository (str | Unset): Repository to create PRs against for promotion
        updated_at (datetime.datetime | Unset):
    """

    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    pr_automation_id: str | Unset = UNSET
    repository: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        pr_automation_id = self.pr_automation_id

        repository = self.repository

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
        if pr_automation_id is not UNSET:
            field_dict["pr_automation_id"] = pr_automation_id
        if repository is not UNSET:
            field_dict["repository"] = repository
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        pr_automation_id = d.pop("pr_automation_id", UNSET)

        repository = d.pop("repository", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        promotion_criteria = cls(
            id=id,
            inserted_at=inserted_at,
            pr_automation_id=pr_automation_id,
            repository=repository,
            updated_at=updated_at,
        )

        promotion_criteria.additional_properties = d
        return promotion_criteria

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
