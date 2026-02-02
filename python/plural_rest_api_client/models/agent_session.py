from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.agent_session_type import AgentSessionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentSession")


@_attrs_define
class AgentSession:
    """An autonomous AI agent session working on infrastructure tasks

    Attributes:
        agent_id (str | Unset): Internal agent identifier
        branch (str | Unset): The git branch this session's pull request is operating on
        cluster_id (str | Unset): ID of the cluster associated with this session
        commit_count (int | Unset): Number of commits made by this agent session
        connection_id (str | Unset): ID of the cloud connection used by this session
        done (bool | Unset): Whether the agent has declared the work for this session complete
        id (str | Unset): Unique identifier for the agent session
        initialized (bool | Unset): Whether the agent session has been initialized
        inserted_at (datetime.datetime | Unset):
        plan_confirmed (bool | Unset): Whether the provisioning plan has been confirmed by the user
        prompt (str | Unset): The prompt given to the agent
        pull_request_id (str | Unset): ID of the pull request created by this session
        service_id (str | Unset): ID of the service associated with this session
        stack_id (str | Unset): ID of the infrastructure stack associated with this session
        thread_id (str | Unset): ID of the chat thread associated with this session
        type_ (AgentSessionType | Unset): Type of agent session (terraform, kubernetes, provisioning, search, manifests,
            chat, research)
        updated_at (datetime.datetime | Unset):
    """

    agent_id: str | Unset = UNSET
    branch: str | Unset = UNSET
    cluster_id: str | Unset = UNSET
    commit_count: int | Unset = UNSET
    connection_id: str | Unset = UNSET
    done: bool | Unset = UNSET
    id: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    plan_confirmed: bool | Unset = UNSET
    prompt: str | Unset = UNSET
    pull_request_id: str | Unset = UNSET
    service_id: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    type_: AgentSessionType | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        branch = self.branch

        cluster_id = self.cluster_id

        commit_count = self.commit_count

        connection_id = self.connection_id

        done = self.done

        id = self.id

        initialized = self.initialized

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        plan_confirmed = self.plan_confirmed

        prompt = self.prompt

        pull_request_id = self.pull_request_id

        service_id = self.service_id

        stack_id = self.stack_id

        thread_id = self.thread_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if branch is not UNSET:
            field_dict["branch"] = branch
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if commit_count is not UNSET:
            field_dict["commit_count"] = commit_count
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if done is not UNSET:
            field_dict["done"] = done
        if id is not UNSET:
            field_dict["id"] = id
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if plan_confirmed is not UNSET:
            field_dict["plan_confirmed"] = plan_confirmed
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if pull_request_id is not UNSET:
            field_dict["pull_request_id"] = pull_request_id
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if stack_id is not UNSET:
            field_dict["stack_id"] = stack_id
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = d.pop("agent_id", UNSET)

        branch = d.pop("branch", UNSET)

        cluster_id = d.pop("cluster_id", UNSET)

        commit_count = d.pop("commit_count", UNSET)

        connection_id = d.pop("connection_id", UNSET)

        done = d.pop("done", UNSET)

        id = d.pop("id", UNSET)

        initialized = d.pop("initialized", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        plan_confirmed = d.pop("plan_confirmed", UNSET)

        prompt = d.pop("prompt", UNSET)

        pull_request_id = d.pop("pull_request_id", UNSET)

        service_id = d.pop("service_id", UNSET)

        stack_id = d.pop("stack_id", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AgentSessionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AgentSessionType(_type_)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        agent_session = cls(
            agent_id=agent_id,
            branch=branch,
            cluster_id=cluster_id,
            commit_count=commit_count,
            connection_id=connection_id,
            done=done,
            id=id,
            initialized=initialized,
            inserted_at=inserted_at,
            plan_confirmed=plan_confirmed,
            prompt=prompt,
            pull_request_id=pull_request_id,
            service_id=service_id,
            stack_id=stack_id,
            thread_id=thread_id,
            type_=type_,
            updated_at=updated_at,
        )

        agent_session.additional_properties = d
        return agent_session

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
