from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GithubAppInput")



@_attrs_define
class GithubAppInput:
    """ Github App authentication configuration

        Attributes:
            app_id (str): The GitHub App ID
            installation_id (str): The GitHub App installation ID
            private_key (str): The private key for the GitHub App
     """

    app_id: str
    installation_id: str
    private_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        installation_id = self.installation_id

        private_key = self.private_key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "app_id": app_id,
            "installation_id": installation_id,
            "private_key": private_key,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("app_id")

        installation_id = d.pop("installation_id")

        private_key = d.pop("private_key")

        github_app_input = cls(
            app_id=app_id,
            installation_id=installation_id,
            private_key=private_key,
        )


        github_app_input.additional_properties = d
        return github_app_input

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
