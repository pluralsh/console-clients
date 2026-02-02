from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_gate import PipelineGate


T = TypeVar("T", bound="PipelineEdge")


@_attrs_define
class PipelineEdge:
    """An edge connecting two stages with optional promotion gates

    Attributes:
        from_id (str | Unset): ID of the source stage
        gates (list[PipelineGate] | Unset): Gates that must be satisfied for promotion
        id (str | Unset): Unique identifier for the edge
        inserted_at (datetime.datetime | Unset):
        promoted_at (datetime.datetime | Unset): Timestamp when promotion last occurred through this edge
        to_id (str | Unset): ID of the destination stage
        updated_at (datetime.datetime | Unset):
    """

    from_id: str | Unset = UNSET
    gates: list[PipelineGate] | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    promoted_at: datetime.datetime | Unset = UNSET
    to_id: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_id = self.from_id

        gates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gates, Unset):
            gates = []
            for gates_item_data in self.gates:
                gates_item = gates_item_data.to_dict()
                gates.append(gates_item)

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        promoted_at: str | Unset = UNSET
        if not isinstance(self.promoted_at, Unset):
            promoted_at = self.promoted_at.isoformat()

        to_id = self.to_id

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_id is not UNSET:
            field_dict["from_id"] = from_id
        if gates is not UNSET:
            field_dict["gates"] = gates
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if promoted_at is not UNSET:
            field_dict["promoted_at"] = promoted_at
        if to_id is not UNSET:
            field_dict["to_id"] = to_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_gate import PipelineGate

        d = dict(src_dict)
        from_id = d.pop("from_id", UNSET)

        _gates = d.pop("gates", UNSET)
        gates: list[PipelineGate] | Unset = UNSET
        if _gates is not UNSET:
            gates = []
            for gates_item_data in _gates:
                gates_item = PipelineGate.from_dict(gates_item_data)

                gates.append(gates_item)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        _promoted_at = d.pop("promoted_at", UNSET)
        promoted_at: datetime.datetime | Unset
        if isinstance(_promoted_at, Unset):
            promoted_at = UNSET
        else:
            promoted_at = isoparse(_promoted_at)

        to_id = d.pop("to_id", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        pipeline_edge = cls(
            from_id=from_id,
            gates=gates,
            id=id,
            inserted_at=inserted_at,
            promoted_at=promoted_at,
            to_id=to_id,
            updated_at=updated_at,
        )

        pipeline_edge.additional_properties = d
        return pipeline_edge

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
