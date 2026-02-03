from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.agent_runtime_type import AgentRuntimeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentRuntime")


@_attrs_define
class AgentRuntime:
    """An agent runtime configured on a cluster for executing AI coding agents

    Attributes:
        ai_proxy (bool | Unset): Whether this runtime uses the built-in Plural AI proxy for LLM requests
        allowed_repositories (list[str] | Unset): The git repositories allowed to be used with this runtime
        cluster_id (str | Unset): ID of the cluster this runtime is deployed on
        default (bool | Unset): Whether this is the default runtime for coding agents
        id (str | Unset): Unique identifier for the agent runtime
        inserted_at (datetime.datetime | Unset):
        name (str | Unset): Human-readable name of this runtime
        type_ (AgentRuntimeType | Unset): Type of agent runtime (claude, opencode, gemini, custom)
        updated_at (datetime.datetime | Unset):
    """

    ai_proxy: bool | Unset = UNSET
    allowed_repositories: list[str] | Unset = UNSET
    cluster_id: str | Unset = UNSET
    default: bool | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    type_: AgentRuntimeType | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ai_proxy = self.ai_proxy

        allowed_repositories: list[str] | Unset = UNSET
        if not isinstance(self.allowed_repositories, Unset):
            allowed_repositories = self.allowed_repositories

        cluster_id = self.cluster_id

        default = self.default

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ai_proxy is not UNSET:
            field_dict["ai_proxy"] = ai_proxy
        if allowed_repositories is not UNSET:
            field_dict["allowed_repositories"] = allowed_repositories
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if default is not UNSET:
            field_dict["default"] = default
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ai_proxy = d.pop("ai_proxy", UNSET)

        allowed_repositories = cast(list[str], d.pop("allowed_repositories", UNSET))

        cluster_id = d.pop("cluster_id", UNSET)

        default = d.pop("default", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AgentRuntimeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AgentRuntimeType(_type_)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        agent_runtime = cls(
            ai_proxy=ai_proxy,
            allowed_repositories=allowed_repositories,
            cluster_id=cluster_id,
            default=default,
            id=id,
            inserted_at=inserted_at,
            name=name,
            type_=type_,
            updated_at=updated_at,
        )

        agent_runtime.additional_properties = d
        return agent_runtime

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
