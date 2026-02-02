from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sentinel_status import SentinelStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.sentinel_check import SentinelCheck





T = TypeVar("T", bound="Sentinel")



@_attrs_define
class Sentinel:
    """ An automated monitoring system that runs checks against your infrastructure

        Attributes:
            checks (list[SentinelCheck] | Unset): List of checks configured for this sentinel
            description (str | Unset): Description of what this sentinel monitors
            id (str | Unset): Unique identifier for the sentinel
            inserted_at (datetime.datetime | Unset):
            last_run_at (datetime.datetime | Unset): Timestamp of when this sentinel was last executed
            name (str | Unset): Human-readable name of this sentinel
            project_id (str | Unset): ID of the project this sentinel belongs to
            repository_id (str | Unset): ID of the git repository for rule files
            status (SentinelStatus | Unset): Status of the sentinel's last run (pending, success, failed)
            updated_at (datetime.datetime | Unset):
     """

    checks: list[SentinelCheck] | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    last_run_at: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    repository_id: str | Unset = UNSET
    status: SentinelStatus | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sentinel_check import SentinelCheck
        checks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.checks, Unset):
            checks = []
            for checks_item_data in self.checks:
                checks_item = checks_item_data.to_dict()
                checks.append(checks_item)



        description = self.description

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        last_run_at: str | Unset = UNSET
        if not isinstance(self.last_run_at, Unset):
            last_run_at = self.last_run_at.isoformat()

        name = self.name

        project_id = self.project_id

        repository_id = self.repository_id

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
        if checks is not UNSET:
            field_dict["checks"] = checks
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if last_run_at is not UNSET:
            field_dict["last_run_at"] = last_run_at
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sentinel_check import SentinelCheck
        d = dict(src_dict)
        _checks = d.pop("checks", UNSET)
        checks: list[SentinelCheck] | Unset = UNSET
        if _checks is not UNSET:
            checks = []
            for checks_item_data in _checks:
                checks_item = SentinelCheck.from_dict(checks_item_data)



                checks.append(checks_item)


        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        _last_run_at = d.pop("last_run_at", UNSET)
        last_run_at: datetime.datetime | Unset
        if isinstance(_last_run_at,  Unset):
            last_run_at = UNSET
        else:
            last_run_at = isoparse(_last_run_at)




        name = d.pop("name", UNSET)

        project_id = d.pop("project_id", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        _status = d.pop("status", UNSET)
        status: SentinelStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = SentinelStatus(_status)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        sentinel = cls(
            checks=checks,
            description=description,
            id=id,
            inserted_at=inserted_at,
            last_run_at=last_run_at,
            name=name,
            project_id=project_id,
            repository_id=repository_id,
            status=status,
            updated_at=updated_at,
        )


        sentinel.additional_properties = d
        return sentinel

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
