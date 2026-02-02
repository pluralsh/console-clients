from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pipeline_gate_state import PipelineGateState
from ..models.pipeline_gate_type import PipelineGateType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PipelineGate")



@_attrs_define
class PipelineGate:
    """ A gate checkpoint for pipeline promotions

        Attributes:
            id (str | Unset): Unique identifier for the gate
            inserted_at (datetime.datetime | Unset):
            name (str | Unset): Name of the gate
            state (PipelineGateState | Unset): Current state of the gate (pending, open, closed, running)
            type_ (PipelineGateType | Unset): Type of gate (approval, window, job)
            updated_at (datetime.datetime | Unset):
     """

    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    state: PipelineGateState | Unset = UNSET
    type_: PipelineGateType | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        name = self.name

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value


        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        name = d.pop("name", UNSET)

        _state = d.pop("state", UNSET)
        state: PipelineGateState | Unset
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = PipelineGateState(_state)




        _type_ = d.pop("type", UNSET)
        type_: PipelineGateType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = PipelineGateType(_type_)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        pipeline_gate = cls(
            id=id,
            inserted_at=inserted_at,
            name=name,
            state=state,
            type_=type_,
            updated_at=updated_at,
        )


        pipeline_gate.additional_properties = d
        return pipeline_gate

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
