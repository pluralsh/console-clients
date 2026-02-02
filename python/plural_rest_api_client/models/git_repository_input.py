from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GitRepositoryInput")



@_attrs_define
class GitRepositoryInput:
    """ Input for creating or updating a git repository

        Attributes:
            url (str): The url of the git repository, can be either an https or ssh url
            connection_id (str | Unset): The id of the scm connection to use for authentication
            passphrase (str | Unset): A passphrase to decrypt the given private key
            password (str | Unset): The http password for http authenticated repos
            private_key (str | Unset): An ssh private key to use with this repo if an ssh url was given
            username (str | Unset): The http username for authenticated http repos, defaults to apiKey for github
     """

    url: str
    connection_id: str | Unset = UNSET
    passphrase: str | Unset = UNSET
    password: str | Unset = UNSET
    private_key: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        connection_id = self.connection_id

        passphrase = self.passphrase

        password = self.password

        private_key = self.private_key

        username = self.username


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "url": url,
        })
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase
        if password is not UNSET:
            field_dict["password"] = password
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        connection_id = d.pop("connection_id", UNSET)

        passphrase = d.pop("passphrase", UNSET)

        password = d.pop("password", UNSET)

        private_key = d.pop("private_key", UNSET)

        username = d.pop("username", UNSET)

        git_repository_input = cls(
            url=url,
            connection_id=connection_id,
            passphrase=passphrase,
            password=password,
            private_key=private_key,
            username=username,
        )


        git_repository_input.additional_properties = d
        return git_repository_input

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
