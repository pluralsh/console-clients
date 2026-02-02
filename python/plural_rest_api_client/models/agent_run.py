from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_run_language import AgentRunLanguage
from ..models.agent_run_mode import AgentRunMode
from ..models.agent_run_status import AgentRunStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AgentRun")



@_attrs_define
class AgentRun:
    """ An execution of an AI coding agent processing a prompt against a repository

        Attributes:
            branch (str | Unset): The git branch the agent is operating on (uses default branch if not set)
            error (str | Unset): Error message if the agent run failed
            flow_id (str | Unset): ID of the flow this agent run is associated with, if any
            id (str | Unset): Unique identifier for the agent run
            inserted_at (datetime.datetime | Unset):
            language (AgentRunLanguage | Unset): Programming language used in the agent run (javascript, python, java, cpp,
                csharp, go, ruby, php, terraform)
            language_version (str | Unset): Specific version of the programming language to use
            mode (AgentRunMode | Unset): Mode of the agent run (analyze for read-only analysis, write for code
                modifications)
            prompt (str | Unset): The prompt given to the AI agent to process
            repository (str | Unset): The git repository URL the agent is working on
            runtime_id (str | Unset): ID of the runtime executing this agent run
            shared (bool | Unset): Whether this agent run is shared publicly
            status (AgentRunStatus | Unset): Current status of the agent run (pending, running, successful, failed,
                cancelled)
            updated_at (datetime.datetime | Unset):
            user_id (str | Unset): ID of the user who initiated this agent run
     """

    branch: str | Unset = UNSET
    error: str | Unset = UNSET
    flow_id: str | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    language: AgentRunLanguage | Unset = UNSET
    language_version: str | Unset = UNSET
    mode: AgentRunMode | Unset = UNSET
    prompt: str | Unset = UNSET
    repository: str | Unset = UNSET
    runtime_id: str | Unset = UNSET
    shared: bool | Unset = UNSET
    status: AgentRunStatus | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        branch = self.branch

        error = self.error

        flow_id = self.flow_id

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        language: str | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value


        language_version = self.language_version

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value


        prompt = self.prompt

        repository = self.repository

        runtime_id = self.runtime_id

        shared = self.shared

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if branch is not UNSET:
            field_dict["branch"] = branch
        if error is not UNSET:
            field_dict["error"] = error
        if flow_id is not UNSET:
            field_dict["flow_id"] = flow_id
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if language is not UNSET:
            field_dict["language"] = language
        if language_version is not UNSET:
            field_dict["language_version"] = language_version
        if mode is not UNSET:
            field_dict["mode"] = mode
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if repository is not UNSET:
            field_dict["repository"] = repository
        if runtime_id is not UNSET:
            field_dict["runtime_id"] = runtime_id
        if shared is not UNSET:
            field_dict["shared"] = shared
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch = d.pop("branch", UNSET)

        error = d.pop("error", UNSET)

        flow_id = d.pop("flow_id", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        _language = d.pop("language", UNSET)
        language: AgentRunLanguage | Unset
        if isinstance(_language,  Unset):
            language = UNSET
        else:
            language = AgentRunLanguage(_language)




        language_version = d.pop("language_version", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: AgentRunMode | Unset
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = AgentRunMode(_mode)




        prompt = d.pop("prompt", UNSET)

        repository = d.pop("repository", UNSET)

        runtime_id = d.pop("runtime_id", UNSET)

        shared = d.pop("shared", UNSET)

        _status = d.pop("status", UNSET)
        status: AgentRunStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = AgentRunStatus(_status)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        user_id = d.pop("user_id", UNSET)

        agent_run = cls(
            branch=branch,
            error=error,
            flow_id=flow_id,
            id=id,
            inserted_at=inserted_at,
            language=language,
            language_version=language_version,
            mode=mode,
            prompt=prompt,
            repository=repository,
            runtime_id=runtime_id,
            shared=shared,
            status=status,
            updated_at=updated_at,
            user_id=user_id,
        )


        agent_run.additional_properties = d
        return agent_run

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
