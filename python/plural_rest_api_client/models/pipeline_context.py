from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_context_context import PipelineContextContext


T = TypeVar("T", bound="PipelineContext")


@_attrs_define
class PipelineContext:
    """A context containing data for pipeline promotions and PR automations

    Attributes:
        context (PipelineContextContext | Unset): Arbitrary key-value data map passed through the pipeline
        id (str | Unset): Unique identifier for the context
        inserted_at (datetime.datetime | Unset):
        pipeline_id (str | Unset): ID of the pipeline this context belongs to
        updated_at (datetime.datetime | Unset):
    """

    context: PipelineContextContext | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    pipeline_id: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        pipeline_id = self.pipeline_id

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["context"] = context
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if pipeline_id is not UNSET:
            field_dict["pipeline_id"] = pipeline_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_context_context import PipelineContextContext

        d = dict(src_dict)
        _context = d.pop("context", UNSET)
        context: PipelineContextContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = PipelineContextContext.from_dict(_context)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        pipeline_id = d.pop("pipeline_id", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        pipeline_context = cls(
            context=context,
            id=id,
            inserted_at=inserted_at,
            pipeline_id=pipeline_id,
            updated_at=updated_at,
        )

        pipeline_context.additional_properties = d
        return pipeline_context

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
