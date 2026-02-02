from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stack_input_type import StackInputType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git import Git
    from ..models.tag import Tag


T = TypeVar("T", bound="StackInput")


@_attrs_define
class StackInput:
    """An infrastructure stack input

    Attributes:
        tags (list[Tag] | Unset):
        approval (bool | Unset):
        cluster_id (str | Unset):
        git (Git | Unset): Git reference configuration
        interval (str | Unset):
        manage_state (bool | Unset):
        name (str | Unset):
        paused (bool | Unset):
        project_id (str | Unset):
        repository_id (str | Unset):
        type_ (StackInputType | Unset):
        workdir (str | Unset):
    """

    tags: list[Tag] | Unset = UNSET
    approval: bool | Unset = UNSET
    cluster_id: str | Unset = UNSET
    git: Git | Unset = UNSET
    interval: str | Unset = UNSET
    manage_state: bool | Unset = UNSET
    name: str | Unset = UNSET
    paused: bool | Unset = UNSET
    project_id: str | Unset = UNSET
    repository_id: str | Unset = UNSET
    type_: StackInputType | Unset = UNSET
    workdir: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        approval = self.approval

        cluster_id = self.cluster_id

        git: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git, Unset):
            git = self.git.to_dict()

        interval = self.interval

        manage_state = self.manage_state

        name = self.name

        paused = self.paused

        project_id = self.project_id

        repository_id = self.repository_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        workdir = self.workdir

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if approval is not UNSET:
            field_dict["approval"] = approval
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if git is not UNSET:
            field_dict["git"] = git
        if interval is not UNSET:
            field_dict["interval"] = interval
        if manage_state is not UNSET:
            field_dict["manage_state"] = manage_state
        if name is not UNSET:
            field_dict["name"] = name
        if paused is not UNSET:
            field_dict["paused"] = paused
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if workdir is not UNSET:
            field_dict["workdir"] = workdir

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git import Git
        from ..models.tag import Tag

        d = dict(src_dict)
        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        approval = d.pop("approval", UNSET)

        cluster_id = d.pop("cluster_id", UNSET)

        _git = d.pop("git", UNSET)
        git: Git | Unset
        if isinstance(_git, Unset):
            git = UNSET
        else:
            git = Git.from_dict(_git)

        interval = d.pop("interval", UNSET)

        manage_state = d.pop("manage_state", UNSET)

        name = d.pop("name", UNSET)

        paused = d.pop("paused", UNSET)

        project_id = d.pop("project_id", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: StackInputType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = StackInputType(_type_)

        workdir = d.pop("workdir", UNSET)

        stack_input = cls(
            tags=tags,
            approval=approval,
            cluster_id=cluster_id,
            git=git,
            interval=interval,
            manage_state=manage_state,
            name=name,
            paused=paused,
            project_id=project_id,
            repository_id=repository_id,
            type_=type_,
            workdir=workdir,
        )

        stack_input.additional_properties = d
        return stack_input

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
