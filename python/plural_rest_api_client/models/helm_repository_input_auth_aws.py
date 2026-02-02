from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="HelmRepositoryInputAuthAws")



@_attrs_define
class HelmRepositoryInputAuthAws:
    """ AWS credentials for ECR

        Attributes:
            access_key (str | Unset): AWS access key ID
            assume_role_arn (str | Unset): ARN of the role to assume
            secret_access_key (str | Unset): AWS secret access key
     """

    access_key: str | Unset = UNSET
    assume_role_arn: str | Unset = UNSET
    secret_access_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_key = self.access_key

        assume_role_arn = self.assume_role_arn

        secret_access_key = self.secret_access_key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_key is not UNSET:
            field_dict["access_key"] = access_key
        if assume_role_arn is not UNSET:
            field_dict["assume_role_arn"] = assume_role_arn
        if secret_access_key is not UNSET:
            field_dict["secret_access_key"] = secret_access_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key = d.pop("access_key", UNSET)

        assume_role_arn = d.pop("assume_role_arn", UNSET)

        secret_access_key = d.pop("secret_access_key", UNSET)

        helm_repository_input_auth_aws = cls(
            access_key=access_key,
            assume_role_arn=assume_role_arn,
            secret_access_key=secret_access_key,
        )


        helm_repository_input_auth_aws.additional_properties = d
        return helm_repository_input_auth_aws

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
