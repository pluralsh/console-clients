from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sentinel_run_status import SentinelRunStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.sentinel_check_result import SentinelCheckResult
  from ..models.sentinel_run_job import SentinelRunJob





T = TypeVar("T", bound="SentinelRun")



@_attrs_define
class SentinelRun:
    """ A single execution of a sentinel's monitoring checks

        Attributes:
            completed_at (datetime.datetime | Unset): Timestamp when the run completed
            id (str | Unset): Unique identifier for the sentinel run
            inserted_at (datetime.datetime | Unset):
            jobs (list[SentinelRunJob] | Unset): Jobs spawned by this sentinel run for integration tests
            results (list[SentinelCheckResult] | Unset): Results of individual checks in this run
            sentinel_id (str | Unset): ID of the sentinel that was executed
            status (SentinelRunStatus | Unset): Current status of the run (pending, success, failed)
            updated_at (datetime.datetime | Unset):
     """

    completed_at: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    jobs: list[SentinelRunJob] | Unset = UNSET
    results: list[SentinelCheckResult] | Unset = UNSET
    sentinel_id: str | Unset = UNSET
    status: SentinelRunStatus | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sentinel_run_job import SentinelRunJob
        from ..models.sentinel_check_result import SentinelCheckResult
        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        jobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.jobs, Unset):
            jobs = []
            for jobs_item_data in self.jobs:
                jobs_item = jobs_item_data.to_dict()
                jobs.append(jobs_item)



        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)



        sentinel_id = self.sentinel_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if results is not UNSET:
            field_dict["results"] = results
        if sentinel_id is not UNSET:
            field_dict["sentinel_id"] = sentinel_id
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sentinel_check_result import SentinelCheckResult
        from ..models.sentinel_run_job import SentinelRunJob
        d = dict(src_dict)
        _completed_at = d.pop("completed_at", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at,  Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)




        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        _jobs = d.pop("jobs", UNSET)
        jobs: list[SentinelRunJob] | Unset = UNSET
        if _jobs is not UNSET:
            jobs = []
            for jobs_item_data in _jobs:
                jobs_item = SentinelRunJob.from_dict(jobs_item_data)



                jobs.append(jobs_item)


        _results = d.pop("results", UNSET)
        results: list[SentinelCheckResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = SentinelCheckResult.from_dict(results_item_data)



                results.append(results_item)


        sentinel_id = d.pop("sentinel_id", UNSET)

        _status = d.pop("status", UNSET)
        status: SentinelRunStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = SentinelRunStatus(_status)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        sentinel_run = cls(
            completed_at=completed_at,
            id=id,
            inserted_at=inserted_at,
            jobs=jobs,
            results=results,
            sentinel_id=sentinel_id,
            status=status,
            updated_at=updated_at,
        )


        sentinel_run.additional_properties = d
        return sentinel_run

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
