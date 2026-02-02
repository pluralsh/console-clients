from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sentinel_check_result_status import SentinelCheckResultStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="SentinelCheckResult")



@_attrs_define
class SentinelCheckResult:
    """ The result of a single check within a sentinel run

        Attributes:
            failed_count (int | Unset): Number of failed jobs
            job_count (int | Unset): Total number of jobs spawned for this check
            name (str | Unset): Name of the check that was executed
            reason (str | Unset): Reason for failure if the check failed
            status (SentinelCheckResultStatus | Unset): Status of this check (pending, success, failed)
            successful_count (int | Unset): Number of successful jobs
     """

    failed_count: int | Unset = UNSET
    job_count: int | Unset = UNSET
    name: str | Unset = UNSET
    reason: str | Unset = UNSET
    status: SentinelCheckResultStatus | Unset = UNSET
    successful_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        failed_count = self.failed_count

        job_count = self.job_count

        name = self.name

        reason = self.reason

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        successful_count = self.successful_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if failed_count is not UNSET:
            field_dict["failed_count"] = failed_count
        if job_count is not UNSET:
            field_dict["job_count"] = job_count
        if name is not UNSET:
            field_dict["name"] = name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if status is not UNSET:
            field_dict["status"] = status
        if successful_count is not UNSET:
            field_dict["successful_count"] = successful_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed_count = d.pop("failed_count", UNSET)

        job_count = d.pop("job_count", UNSET)

        name = d.pop("name", UNSET)

        reason = d.pop("reason", UNSET)

        _status = d.pop("status", UNSET)
        status: SentinelCheckResultStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = SentinelCheckResultStatus(_status)




        successful_count = d.pop("successful_count", UNSET)

        sentinel_check_result = cls(
            failed_count=failed_count,
            job_count=job_count,
            name=name,
            reason=reason,
            status=status,
            successful_count=successful_count,
        )


        sentinel_check_result.additional_properties = d
        return sentinel_check_result

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
