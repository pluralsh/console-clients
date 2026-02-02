from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.console_open_api_user_roles import ConsoleOpenAPIUserRoles





T = TypeVar("T", bound="User")



@_attrs_define
class User:
    """ A registed user

        Attributes:
            email (str):
            id (str):
            inserted_at (datetime.datetime):
            roles (ConsoleOpenAPIUserRoles | Unset): The roles of the user
            service_account (bool | Unset):
            updated_at (datetime.datetime | Unset):
     """

    email: str
    id: str
    inserted_at: datetime.datetime
    roles: ConsoleOpenAPIUserRoles | Unset = UNSET
    service_account: bool | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.console_open_api_user_roles import ConsoleOpenAPIUserRoles
        email = self.email

        id = self.id

        inserted_at = self.inserted_at.isoformat()

        roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles.to_dict()

        service_account = self.service_account

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "email": email,
            "id": id,
            "inserted_at": inserted_at,
        })
        if roles is not UNSET:
            field_dict["roles"] = roles
        if service_account is not UNSET:
            field_dict["service_account"] = service_account
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.console_open_api_user_roles import ConsoleOpenAPIUserRoles
        d = dict(src_dict)
        email = d.pop("email")

        id = d.pop("id")

        inserted_at = isoparse(d.pop("inserted_at"))




        _roles = d.pop("roles", UNSET)
        roles: ConsoleOpenAPIUserRoles | Unset
        if isinstance(_roles,  Unset):
            roles = UNSET
        else:
            roles = ConsoleOpenAPIUserRoles.from_dict(_roles)




        service_account = d.pop("service_account", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        user = cls(
            email=email,
            id=id,
            inserted_at=inserted_at,
            roles=roles,
            service_account=service_account,
            updated_at=updated_at,
        )


        user.additional_properties = d
        return user

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
