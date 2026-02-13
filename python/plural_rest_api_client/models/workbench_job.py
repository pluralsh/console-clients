from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.workbench_job_status import WorkbenchJobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workbench_job_result import WorkbenchJobResult


T = TypeVar("T", bound="WorkbenchJob")


@_attrs_define
class WorkbenchJob:
    """A single run of a workbench

    Attributes:
        completed_at (datetime.datetime | Unset): When the run completed
        error (str | Unset): Error message when the job failed
        id (str | Unset): Unique identifier for the job
        inserted_at (datetime.datetime | Unset):
        prompt (str | Unset): The prompt for this run
        result (WorkbenchJobResult | Unset): The result of a workbench job run (working theory, conclusion, todos)
        started_at (datetime.datetime | Unset): When the run started
        status (WorkbenchJobStatus | Unset): Current status (pending, running, successful, failed, cancelled)
        updated_at (datetime.datetime | Unset):
        user_id (str | Unset): ID of the user who created this run
        workbench_id (str | Unset): ID of the workbench this job belongs to
    """

    completed_at: datetime.datetime | Unset = UNSET
    error: str | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    prompt: str | Unset = UNSET
    result: WorkbenchJobResult | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    status: WorkbenchJobStatus | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    user_id: str | Unset = UNSET
    workbench_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        error = self.error

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        prompt = self.prompt

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        workbench_id = self.workbench_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if result is not UNSET:
            field_dict["result"] = result
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if workbench_id is not UNSET:
            field_dict["workbench_id"] = workbench_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workbench_job_result import WorkbenchJobResult

        d = dict(src_dict)
        _completed_at = d.pop("completed_at", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        error = d.pop("error", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        prompt = d.pop("prompt", UNSET)

        _result = d.pop("result", UNSET)
        result: WorkbenchJobResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = WorkbenchJobResult.from_dict(_result)

        _started_at = d.pop("started_at", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _status = d.pop("status", UNSET)
        status: WorkbenchJobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WorkbenchJobStatus(_status)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_id = d.pop("user_id", UNSET)

        workbench_id = d.pop("workbench_id", UNSET)

        workbench_job = cls(
            completed_at=completed_at,
            error=error,
            id=id,
            inserted_at=inserted_at,
            prompt=prompt,
            result=result,
            started_at=started_at,
            status=status,
            updated_at=updated_at,
            user_id=user_id,
            workbench_id=workbench_id,
        )

        workbench_job.additional_properties = d
        return workbench_job

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
