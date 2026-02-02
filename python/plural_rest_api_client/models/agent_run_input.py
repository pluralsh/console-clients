from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_run_input_mode import AgentRunInputMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentRunInput")


@_attrs_define
class AgentRunInput:
    """Input for creating a new agent run to execute an AI coding agent

    Attributes:
        mode (AgentRunInputMode): Mode of the agent run (analyze for read-only, write for modifications)
        prompt (str): The prompt to give to the agent describing the task to perform
        repository (str): The git repository URL the agent will work on (https or ssh format)
        runtime_id (str): The runtime ID to execute the agent run on
        flow_id (str | Unset): Optional flow ID to associate this agent run with
        shared (bool | Unset): Whether to share this agent run publicly
    """

    mode: AgentRunInputMode
    prompt: str
    repository: str
    runtime_id: str
    flow_id: str | Unset = UNSET
    shared: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        prompt = self.prompt

        repository = self.repository

        runtime_id = self.runtime_id

        flow_id = self.flow_id

        shared = self.shared

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "prompt": prompt,
                "repository": repository,
                "runtime_id": runtime_id,
            }
        )
        if flow_id is not UNSET:
            field_dict["flow_id"] = flow_id
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = AgentRunInputMode(d.pop("mode"))

        prompt = d.pop("prompt")

        repository = d.pop("repository")

        runtime_id = d.pop("runtime_id")

        flow_id = d.pop("flow_id", UNSET)

        shared = d.pop("shared", UNSET)

        agent_run_input = cls(
            mode=mode,
            prompt=prompt,
            repository=repository,
            runtime_id=runtime_id,
            flow_id=flow_id,
            shared=shared,
        )

        agent_run_input.additional_properties = d
        return agent_run_input

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
