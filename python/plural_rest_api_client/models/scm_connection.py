from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.scm_connection_type import ScmConnectionType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.console_open_apiscm_connection_github_app import ConsoleOpenAPISCMConnectionGithubApp





T = TypeVar("T", bound="ScmConnection")



@_attrs_define
class ScmConnection:
    """ An SCM connection for integrating with source control providers

        Attributes:
            name (str): The name of the SCM connection
            type_ (ScmConnectionType):
            api_url (str | Unset): Base URL for HTTP APIs for self-hosted versions if different from base URL
            base_url (str | Unset): Base URL for self-hosted versions of this provider
            default (bool | Unset): Whether this is the default SCM connection
            github (ConsoleOpenAPISCMConnectionGithubApp | Unset): A Github App connection
            id (str | Unset):
            inserted_at (datetime.datetime | Unset):
            updated_at (datetime.datetime | Unset):
            username (str | Unset): The username for authentication
     """

    name: str
    type_: ScmConnectionType
    api_url: str | Unset = UNSET
    base_url: str | Unset = UNSET
    default: bool | Unset = UNSET
    github: ConsoleOpenAPISCMConnectionGithubApp | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.console_open_apiscm_connection_github_app import ConsoleOpenAPISCMConnectionGithubApp
        name = self.name

        type_ = self.type_.value

        api_url = self.api_url

        base_url = self.base_url

        default = self.default

        github: dict[str, Any] | Unset = UNSET
        if not isinstance(self.github, Unset):
            github = self.github.to_dict()

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        username = self.username


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "type": type_,
        })
        if api_url is not UNSET:
            field_dict["api_url"] = api_url
        if base_url is not UNSET:
            field_dict["base_url"] = base_url
        if default is not UNSET:
            field_dict["default"] = default
        if github is not UNSET:
            field_dict["github"] = github
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.console_open_apiscm_connection_github_app import ConsoleOpenAPISCMConnectionGithubApp
        d = dict(src_dict)
        name = d.pop("name")

        type_ = ScmConnectionType(d.pop("type"))




        api_url = d.pop("api_url", UNSET)

        base_url = d.pop("base_url", UNSET)

        default = d.pop("default", UNSET)

        _github = d.pop("github", UNSET)
        github: ConsoleOpenAPISCMConnectionGithubApp | Unset
        if isinstance(_github,  Unset):
            github = UNSET
        else:
            github = ConsoleOpenAPISCMConnectionGithubApp.from_dict(_github)




        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        username = d.pop("username", UNSET)

        scm_connection = cls(
            name=name,
            type_=type_,
            api_url=api_url,
            base_url=base_url,
            default=default,
            github=github,
            id=id,
            inserted_at=inserted_at,
            updated_at=updated_at,
            username=username,
        )


        scm_connection.additional_properties = d
        return scm_connection

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
