from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pipeline_context_input_context import PipelineContextInputContext


T = TypeVar("T", bound="PipelineContextInput")


@_attrs_define
class PipelineContextInput:
    """Input for creating a new pipeline context to trigger a pipeline run

    Attributes:
        context (PipelineContextInputContext): Arbitrary key-value data map to pass through the pipeline for PR
            automations
    """

    context: PipelineContextInputContext
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context = self.context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "context": context,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_context_input_context import PipelineContextInputContext

        d = dict(src_dict)
        context = PipelineContextInputContext.from_dict(d.pop("context"))

        pipeline_context_input = cls(
            context=context,
        )

        pipeline_context_input.additional_properties = d
        return pipeline_context_input

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
