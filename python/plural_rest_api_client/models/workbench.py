from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Workbench")


@_attrs_define
class Workbench:
    """A workbench for running AI jobs with configurable tools and prompts

    Attributes:
        agent_runtime_id (str | Unset): ID of the agent runtime for this workbench
        description (str | Unset): Description of the workbench
        id (str | Unset): Unique identifier for the workbench
        inserted_at (datetime.datetime | Unset):
        name (str | Unset): Human-readable name of the workbench
        project_id (str | Unset): ID of the project this workbench belongs to
        repository_id (str | Unset): ID of the git repository for this workbench
        system_prompt (str | Unset): The system prompt for the workbench
        updated_at (datetime.datetime | Unset):
    """

    agent_runtime_id: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    repository_id: str | Unset = UNSET
    system_prompt: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_runtime_id = self.agent_runtime_id

        description = self.description

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        name = self.name

        project_id = self.project_id

        repository_id = self.repository_id

        system_prompt = self.system_prompt

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_runtime_id is not UNSET:
            field_dict["agent_runtime_id"] = agent_runtime_id
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_runtime_id = d.pop("agent_runtime_id", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        name = d.pop("name", UNSET)

        project_id = d.pop("project_id", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        system_prompt = d.pop("system_prompt", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        workbench = cls(
            agent_runtime_id=agent_runtime_id,
            description=description,
            id=id,
            inserted_at=inserted_at,
            name=name,
            project_id=project_id,
            repository_id=repository_id,
            system_prompt=system_prompt,
            updated_at=updated_at,
        )

        workbench.additional_properties = d
        return workbench

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
