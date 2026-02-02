from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_pull_request_input_context import CreatePullRequestInputContext


T = TypeVar("T", bound="CreatePullRequestInput")


@_attrs_define
class CreatePullRequestInput:
    """Input for creating a pull request using a PR automation

    Attributes:
        context (CreatePullRequestInputContext): Context variables to pass to the PR automation templates
        branch (str | Unset): Branch name for the pull request (overrides default)
        identifier (str | Unset): Repository identifier (overrides default)
    """

    context: CreatePullRequestInputContext
    branch: str | Unset = UNSET
    identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context = self.context.to_dict()

        branch = self.branch

        identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "context": context,
            }
        )
        if branch is not UNSET:
            field_dict["branch"] = branch
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_pull_request_input_context import (
            CreatePullRequestInputContext,
        )

        d = dict(src_dict)
        context = CreatePullRequestInputContext.from_dict(d.pop("context"))

        branch = d.pop("branch", UNSET)

        identifier = d.pop("identifier", UNSET)

        create_pull_request_input = cls(
            context=context,
            branch=branch,
            identifier=identifier,
        )

        create_pull_request_input.additional_properties = d
        return create_pull_request_input

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
