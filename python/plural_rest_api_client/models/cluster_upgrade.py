from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cluster_upgrade_status import ClusterUpgradeStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_runtime import AgentRuntime
    from ..models.cluster_upgrade_step import ClusterUpgradeStep
    from ..models.user import User


T = TypeVar("T", bound="ClusterUpgrade")


@_attrs_define
class ClusterUpgrade:
    """An agentic workflow for upgrading a cluster

    Attributes:
        cluster_id (str | Unset): ID of the cluster being upgraded
        id (str | Unset): Unique identifier for the cluster upgrade
        inserted_at (datetime.datetime | Unset):
        prompt (str | Unset): Prompt used to generate the upgrade workflow
        runtime (AgentRuntime | Unset): An agent runtime configured on a cluster for executing AI coding agents
        runtime_id (str | Unset): ID of the agent runtime executing the upgrade
        status (ClusterUpgradeStatus | Unset): Status of the upgrade (pending, in_progress, completed, failed)
        steps (list[ClusterUpgradeStep] | Unset): Steps that make up this upgrade workflow
        updated_at (datetime.datetime | Unset):
        user (User | Unset): A registed user
        user_id (str | Unset): ID of the user who initiated the upgrade
        version (str | Unset): Target Kubernetes version for this upgrade
    """

    cluster_id: str | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    prompt: str | Unset = UNSET
    runtime: AgentRuntime | Unset = UNSET
    runtime_id: str | Unset = UNSET
    status: ClusterUpgradeStatus | Unset = UNSET
    steps: list[ClusterUpgradeStep] | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    user: User | Unset = UNSET
    user_id: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_id = self.cluster_id

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        prompt = self.prompt

        runtime: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runtime, Unset):
            runtime = self.runtime.to_dict()

        runtime_id = self.runtime_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_id = self.user_id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if runtime_id is not UNSET:
            field_dict["runtime_id"] = runtime_id
        if status is not UNSET:
            field_dict["status"] = status
        if steps is not UNSET:
            field_dict["steps"] = steps
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user is not UNSET:
            field_dict["user"] = user
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_runtime import AgentRuntime
        from ..models.cluster_upgrade_step import ClusterUpgradeStep
        from ..models.user import User

        d = dict(src_dict)
        cluster_id = d.pop("cluster_id", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        prompt = d.pop("prompt", UNSET)

        _runtime = d.pop("runtime", UNSET)
        runtime: AgentRuntime | Unset
        if isinstance(_runtime, Unset):
            runtime = UNSET
        else:
            runtime = AgentRuntime.from_dict(_runtime)

        runtime_id = d.pop("runtime_id", UNSET)

        _status = d.pop("status", UNSET)
        status: ClusterUpgradeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ClusterUpgradeStatus(_status)

        _steps = d.pop("steps", UNSET)
        steps: list[ClusterUpgradeStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = ClusterUpgradeStep.from_dict(steps_item_data)

                steps.append(steps_item)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        user_id = d.pop("user_id", UNSET)

        version = d.pop("version", UNSET)

        cluster_upgrade = cls(
            cluster_id=cluster_id,
            id=id,
            inserted_at=inserted_at,
            prompt=prompt,
            runtime=runtime,
            runtime_id=runtime_id,
            status=status,
            steps=steps,
            updated_at=updated_at,
            user=user,
            user_id=user_id,
            version=version,
        )

        cluster_upgrade.additional_properties = d
        return cluster_upgrade

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
