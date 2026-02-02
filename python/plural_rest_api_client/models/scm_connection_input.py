from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.scm_connection_input_type import ScmConnectionInputType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.github_app_input import GithubAppInput





T = TypeVar("T", bound="ScmConnectionInput")



@_attrs_define
class ScmConnectionInput:
    """ Input for creating or updating an SCM connection

        Attributes:
            name (str): The name of the SCM connection
            type_ (ScmConnectionInputType):
            api_url (str | Unset): Base URL for HTTP APIs for self-hosted versions if different from base URL
            base_url (str | Unset): Base URL for Git clones for self-hosted versions
            default (bool | Unset): Whether this is the default SCM connection
            github (GithubAppInput | Unset): Github App authentication configuration
            signing_private_key (str | Unset): A private key used for signing commits
            token (str | Unset): The access token for authentication
            username (str | Unset): The username for authentication
     """

    name: str
    type_: ScmConnectionInputType
    api_url: str | Unset = UNSET
    base_url: str | Unset = UNSET
    default: bool | Unset = UNSET
    github: GithubAppInput | Unset = UNSET
    signing_private_key: str | Unset = UNSET
    token: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.github_app_input import GithubAppInput
        name = self.name

        type_ = self.type_.value

        api_url = self.api_url

        base_url = self.base_url

        default = self.default

        github: dict[str, Any] | Unset = UNSET
        if not isinstance(self.github, Unset):
            github = self.github.to_dict()

        signing_private_key = self.signing_private_key

        token = self.token

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
        if signing_private_key is not UNSET:
            field_dict["signing_private_key"] = signing_private_key
        if token is not UNSET:
            field_dict["token"] = token
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_app_input import GithubAppInput
        d = dict(src_dict)
        name = d.pop("name")

        type_ = ScmConnectionInputType(d.pop("type"))




        api_url = d.pop("api_url", UNSET)

        base_url = d.pop("base_url", UNSET)

        default = d.pop("default", UNSET)

        _github = d.pop("github", UNSET)
        github: GithubAppInput | Unset
        if isinstance(_github,  Unset):
            github = UNSET
        else:
            github = GithubAppInput.from_dict(_github)




        signing_private_key = d.pop("signing_private_key", UNSET)

        token = d.pop("token", UNSET)

        username = d.pop("username", UNSET)

        scm_connection_input = cls(
            name=name,
            type_=type_,
            api_url=api_url,
            base_url=base_url,
            default=default,
            github=github,
            signing_private_key=signing_private_key,
            token=token,
            username=username,
        )


        scm_connection_input.additional_properties = d
        return scm_connection_input

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
