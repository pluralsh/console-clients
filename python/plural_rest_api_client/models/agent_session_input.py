from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_session_input_type import AgentSessionInputType
from ..types import UNSET, Unset






T = TypeVar("T", bound="AgentSessionInput")



@_attrs_define
class AgentSessionInput:
    """ Input for creating a new agent session to execute autonomous infrastructure tasks

        Attributes:
            prompt (str): The prompt describing the task for the agent to perform
            cluster_id (str | Unset): ID of the cluster to use for this session
            connection_id (str | Unset): ID of the cloud connection to use for this session
            done (bool | Unset): Whether to immediately mark this session as done
            plan_confirmed (bool | Unset): Whether the provisioning plan is pre-confirmed
            type_ (AgentSessionInputType | Unset): Type of agent session (terraform, kubernetes)
     """

    prompt: str
    cluster_id: str | Unset = UNSET
    connection_id: str | Unset = UNSET
    done: bool | Unset = UNSET
    plan_confirmed: bool | Unset = UNSET
    type_: AgentSessionInputType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt

        cluster_id = self.cluster_id

        connection_id = self.connection_id

        done = self.done

        plan_confirmed = self.plan_confirmed

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "prompt": prompt,
        })
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if done is not UNSET:
            field_dict["done"] = done
        if plan_confirmed is not UNSET:
            field_dict["plan_confirmed"] = plan_confirmed
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prompt = d.pop("prompt")

        cluster_id = d.pop("cluster_id", UNSET)

        connection_id = d.pop("connection_id", UNSET)

        done = d.pop("done", UNSET)

        plan_confirmed = d.pop("plan_confirmed", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AgentSessionInputType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = AgentSessionInputType(_type_)




        agent_session_input = cls(
            prompt=prompt,
            cluster_id=cluster_id,
            connection_id=connection_id,
            done=done,
            plan_confirmed=plan_confirmed,
            type_=type_,
        )


        agent_session_input.additional_properties = d
        return agent_session_input

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
