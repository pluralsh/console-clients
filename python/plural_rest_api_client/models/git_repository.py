from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.git_repository_auth_method import GitRepositoryAuthMethod
from ..models.git_repository_health import GitRepositoryHealth
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="GitRepository")



@_attrs_define
class GitRepository:
    """ A git repository

        Attributes:
            auth_method (GitRepositoryAuthMethod | Unset):
            error (str | Unset): The error message for the git repository's last pull attempt
            health (GitRepositoryHealth | Unset):
            https_path (str | Unset): The https url for this git repo if you need to customize it
            id (str | Unset):
            inserted_at (datetime.datetime | Unset):
            pulled_at (datetime.datetime | Unset): The last successful git pull timestamp
            updated_at (datetime.datetime | Unset):
            url (str | Unset): The url of the git repository, can be either an https or ssh url
            url_format (str | Unset): A format string to get the http url for a subfolder in a git repo
     """

    auth_method: GitRepositoryAuthMethod | Unset = UNSET
    error: str | Unset = UNSET
    health: GitRepositoryHealth | Unset = UNSET
    https_path: str | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    pulled_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    url: str | Unset = UNSET
    url_format: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        auth_method: str | Unset = UNSET
        if not isinstance(self.auth_method, Unset):
            auth_method = self.auth_method.value


        error = self.error

        health: str | Unset = UNSET
        if not isinstance(self.health, Unset):
            health = self.health.value


        https_path = self.https_path

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        pulled_at: str | Unset = UNSET
        if not isinstance(self.pulled_at, Unset):
            pulled_at = self.pulled_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        url = self.url

        url_format = self.url_format


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if auth_method is not UNSET:
            field_dict["auth_method"] = auth_method
        if error is not UNSET:
            field_dict["error"] = error
        if health is not UNSET:
            field_dict["health"] = health
        if https_path is not UNSET:
            field_dict["https_path"] = https_path
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if pulled_at is not UNSET:
            field_dict["pulled_at"] = pulled_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if url_format is not UNSET:
            field_dict["url_format"] = url_format

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _auth_method = d.pop("auth_method", UNSET)
        auth_method: GitRepositoryAuthMethod | Unset
        if isinstance(_auth_method,  Unset):
            auth_method = UNSET
        else:
            auth_method = GitRepositoryAuthMethod(_auth_method)




        error = d.pop("error", UNSET)

        _health = d.pop("health", UNSET)
        health: GitRepositoryHealth | Unset
        if isinstance(_health,  Unset):
            health = UNSET
        else:
            health = GitRepositoryHealth(_health)




        https_path = d.pop("https_path", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        _pulled_at = d.pop("pulled_at", UNSET)
        pulled_at: datetime.datetime | Unset
        if isinstance(_pulled_at,  Unset):
            pulled_at = UNSET
        else:
            pulled_at = isoparse(_pulled_at)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        url = d.pop("url", UNSET)

        url_format = d.pop("url_format", UNSET)

        git_repository = cls(
            auth_method=auth_method,
            error=error,
            health=health,
            https_path=https_path,
            id=id,
            inserted_at=inserted_at,
            pulled_at=pulled_at,
            updated_at=updated_at,
            url=url,
            url_format=url_format,
        )


        git_repository.additional_properties = d
        return git_repository

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
