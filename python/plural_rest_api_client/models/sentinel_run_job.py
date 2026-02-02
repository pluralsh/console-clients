from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sentinel_run_job_format import SentinelRunJobFormat
from ..models.sentinel_run_job_status import SentinelRunJobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SentinelRunJob")


@_attrs_define
class SentinelRunJob:
    """An integration test job spawned by a sentinel run

    Attributes:
        check (str | Unset): Name of the check this job belongs to
        cluster_id (str | Unset): ID of the cluster this job ran on
        completed_at (datetime.datetime | Unset): Timestamp when the job completed
        format_ (SentinelRunJobFormat | Unset): Output format of the job (plaintext, junit)
        id (str | Unset): Unique identifier for the job
        inserted_at (datetime.datetime | Unset):
        output (str | Unset): Output produced by the job
        repository_id (str | Unset): ID of the git repository used for the test
        sentinel_run_id (str | Unset): ID of the sentinel run this job belongs to
        status (SentinelRunJobStatus | Unset): Current status of the job (pending, running, success, failed)
        updated_at (datetime.datetime | Unset):
    """

    check: str | Unset = UNSET
    cluster_id: str | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    format_: SentinelRunJobFormat | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    output: str | Unset = UNSET
    repository_id: str | Unset = UNSET
    sentinel_run_id: str | Unset = UNSET
    status: SentinelRunJobStatus | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check = self.check

        cluster_id = self.cluster_id

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        output = self.output

        repository_id = self.repository_id

        sentinel_run_id = self.sentinel_run_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check is not UNSET:
            field_dict["check"] = check
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if format_ is not UNSET:
            field_dict["format"] = format_
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if output is not UNSET:
            field_dict["output"] = output
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if sentinel_run_id is not UNSET:
            field_dict["sentinel_run_id"] = sentinel_run_id
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        check = d.pop("check", UNSET)

        cluster_id = d.pop("cluster_id", UNSET)

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _format_ = d.pop("format", UNSET)
        format_: SentinelRunJobFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = SentinelRunJobFormat(_format_)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        output = d.pop("output", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        sentinel_run_id = d.pop("sentinel_run_id", UNSET)

        _status = d.pop("status", UNSET)
        status: SentinelRunJobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SentinelRunJobStatus(_status)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        sentinel_run_job = cls(
            check=check,
            cluster_id=cluster_id,
            completed_at=completed_at,
            format_=format_,
            id=id,
            inserted_at=inserted_at,
            output=output,
            repository_id=repository_id,
            sentinel_run_id=sentinel_run_id,
            status=status,
            updated_at=updated_at,
        )

        sentinel_run_job.additional_properties = d
        return sentinel_run_job

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
