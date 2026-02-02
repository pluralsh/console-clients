from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.stack_status import StackStatus
from ..models.stack_type import StackType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.git import Git
  from ..models.tag import Tag





T = TypeVar("T", bound="Stack")



@_attrs_define
class Stack:
    """ An infrastructure stack

        Attributes:
            tags (list[Tag] | Unset):
            approval (bool | Unset):
            cluster_id (str | Unset):
            deleted_at (datetime.datetime | Unset):
            git (Git | Unset): Git reference configuration
            id (str | Unset):
            inserted_at (datetime.datetime | Unset):
            interval (str | Unset):
            manage_state (bool | Unset):
            name (str | Unset):
            paused (bool | Unset):
            project_id (str | Unset):
            repository_id (str | Unset):
            status (StackStatus | Unset):
            type_ (StackType | Unset):
            updated_at (datetime.datetime | Unset):
            workdir (str | Unset):
     """

    tags: list[Tag] | Unset = UNSET
    approval: bool | Unset = UNSET
    cluster_id: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    git: Git | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    interval: str | Unset = UNSET
    manage_state: bool | Unset = UNSET
    name: str | Unset = UNSET
    paused: bool | Unset = UNSET
    project_id: str | Unset = UNSET
    repository_id: str | Unset = UNSET
    status: StackStatus | Unset = UNSET
    type_: StackType | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    workdir: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.git import Git
        from ..models.tag import Tag
        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)



        approval = self.approval

        cluster_id = self.cluster_id

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        git: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git, Unset):
            git = self.git.to_dict()

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        interval = self.interval

        manage_state = self.manage_state

        name = self.name

        paused = self.paused

        project_id = self.project_id

        repository_id = self.repository_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        workdir = self.workdir


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tags is not UNSET:
            field_dict["tags"] = tags
        if approval is not UNSET:
            field_dict["approval"] = approval
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if git is not UNSET:
            field_dict["git"] = git
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
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
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
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

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at,  Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)




        _git = d.pop("git", UNSET)
        git: Git | Unset
        if isinstance(_git,  Unset):
            git = UNSET
        else:
            git = Git.from_dict(_git)




        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        interval = d.pop("interval", UNSET)

        manage_state = d.pop("manage_state", UNSET)

        name = d.pop("name", UNSET)

        paused = d.pop("paused", UNSET)

        project_id = d.pop("project_id", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        _status = d.pop("status", UNSET)
        status: StackStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = StackStatus(_status)




        _type_ = d.pop("type", UNSET)
        type_: StackType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = StackType(_type_)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        workdir = d.pop("workdir", UNSET)

        stack = cls(
            tags=tags,
            approval=approval,
            cluster_id=cluster_id,
            deleted_at=deleted_at,
            git=git,
            id=id,
            inserted_at=inserted_at,
            interval=interval,
            manage_state=manage_state,
            name=name,
            paused=paused,
            project_id=project_id,
            repository_id=repository_id,
            status=status,
            type_=type_,
            updated_at=updated_at,
            workdir=workdir,
        )


        stack.additional_properties = d
        return stack

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
