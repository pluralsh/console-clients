from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cluster_upgrade_step_status import ClusterUpgradeStepStatus
from ..models.cluster_upgrade_step_type import ClusterUpgradeStepType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.agent_run import AgentRun





T = TypeVar("T", bound="ClusterUpgradeStep")



@_attrs_define
class ClusterUpgradeStep:
    """ A step in an agentic cluster upgrade workflow

        Attributes:
            agent_run (AgentRun | Unset): An execution of an AI coding agent processing a prompt against a repository
            agent_run_id (str | Unset): ID of the agent run associated with this step, if any
            error (str | Unset): Error message if the step failed
            id (str | Unset): Unique identifier for the upgrade step
            inserted_at (datetime.datetime | Unset):
            name (str | Unset): Name of the upgrade step
            prompt (str | Unset): Prompt used to generate the upgrade step
            status (ClusterUpgradeStepStatus | Unset): Status of the step (pending, in_progress, completed, failed)
            type_ (ClusterUpgradeStepType | Unset): Type of step (addon, cloud_addon, infrastructure)
            updated_at (datetime.datetime | Unset):
            upgrade_id (str | Unset): ID of the cluster upgrade this step belongs to
     """

    agent_run: AgentRun | Unset = UNSET
    agent_run_id: str | Unset = UNSET
    error: str | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    prompt: str | Unset = UNSET
    status: ClusterUpgradeStepStatus | Unset = UNSET
    type_: ClusterUpgradeStepType | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    upgrade_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_run import AgentRun
        agent_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.agent_run, Unset):
            agent_run = self.agent_run.to_dict()

        agent_run_id = self.agent_run_id

        error = self.error

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        name = self.name

        prompt = self.prompt

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        upgrade_id = self.upgrade_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if agent_run is not UNSET:
            field_dict["agent_run"] = agent_run
        if agent_run_id is not UNSET:
            field_dict["agent_run_id"] = agent_run_id
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if name is not UNSET:
            field_dict["name"] = name
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if upgrade_id is not UNSET:
            field_dict["upgrade_id"] = upgrade_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_run import AgentRun
        d = dict(src_dict)
        _agent_run = d.pop("agent_run", UNSET)
        agent_run: AgentRun | Unset
        if isinstance(_agent_run,  Unset):
            agent_run = UNSET
        else:
            agent_run = AgentRun.from_dict(_agent_run)




        agent_run_id = d.pop("agent_run_id", UNSET)

        error = d.pop("error", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        name = d.pop("name", UNSET)

        prompt = d.pop("prompt", UNSET)

        _status = d.pop("status", UNSET)
        status: ClusterUpgradeStepStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ClusterUpgradeStepStatus(_status)




        _type_ = d.pop("type", UNSET)
        type_: ClusterUpgradeStepType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = ClusterUpgradeStepType(_type_)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        upgrade_id = d.pop("upgrade_id", UNSET)

        cluster_upgrade_step = cls(
            agent_run=agent_run,
            agent_run_id=agent_run_id,
            error=error,
            id=id,
            inserted_at=inserted_at,
            name=name,
            prompt=prompt,
            status=status,
            type_=type_,
            updated_at=updated_at,
            upgrade_id=upgrade_id,
        )


        cluster_upgrade_step.additional_properties = d
        return cluster_upgrade_step

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
