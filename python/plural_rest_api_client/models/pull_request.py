from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pull_request_status import PullRequestStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PullRequest")



@_attrs_define
class PullRequest:
    """ A pull request reference tracked by the platform for deployment workflows

        Attributes:
            title (str | Unset): Title of the pull request
            body (str | Unset): Body/description of the pull request
            cluster_id (str | Unset): ID of the cluster this pull request is associated with, if any
            creator (str | Unset): Username of the pull request creator in the source control provider
            id (str | Unset): Unique identifier for the pull request record
            inserted_at (datetime.datetime | Unset):
            labels (list[str] | Unset): Labels applied to the pull request
            ref (str | Unset): Git ref (branch name) for the pull request
            service_id (str | Unset): ID of the service this pull request is associated with, if any
            sha (str | Unset): Git SHA of the pull request head
            stack_id (str | Unset): ID of the stack this pull request is associated with, if any
            status (PullRequestStatus | Unset): Current status of the pull request (open, merged, closed)
            updated_at (datetime.datetime | Unset):
            url (str | Unset): URL of the pull request in the source control provider
     """

    title: str | Unset = UNSET
    body: str | Unset = UNSET
    cluster_id: str | Unset = UNSET
    creator: str | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    labels: list[str] | Unset = UNSET
    ref: str | Unset = UNSET
    service_id: str | Unset = UNSET
    sha: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    status: PullRequestStatus | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        body = self.body

        cluster_id = self.cluster_id

        creator = self.creator

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels



        ref = self.ref

        service_id = self.service_id

        sha = self.sha

        stack_id = self.stack_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if creator is not UNSET:
            field_dict["creator"] = creator
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if labels is not UNSET:
            field_dict["labels"] = labels
        if ref is not UNSET:
            field_dict["ref"] = ref
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if sha is not UNSET:
            field_dict["sha"] = sha
        if stack_id is not UNSET:
            field_dict["stack_id"] = stack_id
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        cluster_id = d.pop("cluster_id", UNSET)

        creator = d.pop("creator", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        labels = cast(list[str], d.pop("labels", UNSET))


        ref = d.pop("ref", UNSET)

        service_id = d.pop("service_id", UNSET)

        sha = d.pop("sha", UNSET)

        stack_id = d.pop("stack_id", UNSET)

        _status = d.pop("status", UNSET)
        status: PullRequestStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = PullRequestStatus(_status)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        url = d.pop("url", UNSET)

        pull_request = cls(
            title=title,
            body=body,
            cluster_id=cluster_id,
            creator=creator,
            id=id,
            inserted_at=inserted_at,
            labels=labels,
            ref=ref,
            service_id=service_id,
            sha=sha,
            stack_id=stack_id,
            status=status,
            updated_at=updated_at,
            url=url,
        )


        pull_request.additional_properties = d
        return pull_request

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
