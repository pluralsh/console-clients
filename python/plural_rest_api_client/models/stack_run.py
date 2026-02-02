from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.stack_run_status import StackRunStatus
from ..models.stack_run_type import StackRunType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git import Git


T = TypeVar("T", bound="StackRun")


@_attrs_define
class StackRun:
    """A stack run instance

    Attributes:
        approval (bool | Unset):
        approved_at (datetime.datetime | Unset):
        cancellation_reason (str | Unset):
        cluster_id (str | Unset):
        destroy (bool | Unset):
        dry_run (bool | Unset):
        git (Git | Unset): Git reference configuration
        id (str | Unset):
        inserted_at (datetime.datetime | Unset):
        manage_state (bool | Unset):
        message (str | Unset):
        repository_id (str | Unset):
        stack_id (str | Unset):
        status (StackRunStatus | Unset):
        type_ (StackRunType | Unset):
        updated_at (datetime.datetime | Unset):
        workdir (str | Unset):
    """

    approval: bool | Unset = UNSET
    approved_at: datetime.datetime | Unset = UNSET
    cancellation_reason: str | Unset = UNSET
    cluster_id: str | Unset = UNSET
    destroy: bool | Unset = UNSET
    dry_run: bool | Unset = UNSET
    git: Git | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    manage_state: bool | Unset = UNSET
    message: str | Unset = UNSET
    repository_id: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    status: StackRunStatus | Unset = UNSET
    type_: StackRunType | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    workdir: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval = self.approval

        approved_at: str | Unset = UNSET
        if not isinstance(self.approved_at, Unset):
            approved_at = self.approved_at.isoformat()

        cancellation_reason = self.cancellation_reason

        cluster_id = self.cluster_id

        destroy = self.destroy

        dry_run = self.dry_run

        git: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git, Unset):
            git = self.git.to_dict()

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        manage_state = self.manage_state

        message = self.message

        repository_id = self.repository_id

        stack_id = self.stack_id

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
        field_dict.update({})
        if approval is not UNSET:
            field_dict["approval"] = approval
        if approved_at is not UNSET:
            field_dict["approved_at"] = approved_at
        if cancellation_reason is not UNSET:
            field_dict["cancellation_reason"] = cancellation_reason
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if destroy is not UNSET:
            field_dict["destroy"] = destroy
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if git is not UNSET:
            field_dict["git"] = git
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if manage_state is not UNSET:
            field_dict["manage_state"] = manage_state
        if message is not UNSET:
            field_dict["message"] = message
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if stack_id is not UNSET:
            field_dict["stack_id"] = stack_id
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

        d = dict(src_dict)
        approval = d.pop("approval", UNSET)

        _approved_at = d.pop("approved_at", UNSET)
        approved_at: datetime.datetime | Unset
        if isinstance(_approved_at, Unset):
            approved_at = UNSET
        else:
            approved_at = isoparse(_approved_at)

        cancellation_reason = d.pop("cancellation_reason", UNSET)

        cluster_id = d.pop("cluster_id", UNSET)

        destroy = d.pop("destroy", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        _git = d.pop("git", UNSET)
        git: Git | Unset
        if isinstance(_git, Unset):
            git = UNSET
        else:
            git = Git.from_dict(_git)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        manage_state = d.pop("manage_state", UNSET)

        message = d.pop("message", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        stack_id = d.pop("stack_id", UNSET)

        _status = d.pop("status", UNSET)
        status: StackRunStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StackRunStatus(_status)

        _type_ = d.pop("type", UNSET)
        type_: StackRunType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = StackRunType(_type_)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        workdir = d.pop("workdir", UNSET)

        stack_run = cls(
            approval=approval,
            approved_at=approved_at,
            cancellation_reason=cancellation_reason,
            cluster_id=cluster_id,
            destroy=destroy,
            dry_run=dry_run,
            git=git,
            id=id,
            inserted_at=inserted_at,
            manage_state=manage_state,
            message=message,
            repository_id=repository_id,
            stack_id=stack_id,
            status=status,
            type_=type_,
            updated_at=updated_at,
            workdir=workdir,
        )

        stack_run.additional_properties = d
        return stack_run

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
