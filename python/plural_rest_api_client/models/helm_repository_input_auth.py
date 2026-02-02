from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.helm_repository_input_auth_aws import HelmRepositoryInputAuthAws
  from ..models.helm_repository_input_auth_azure import HelmRepositoryInputAuthAzure
  from ..models.helm_repository_input_auth_basic import HelmRepositoryInputAuthBasic
  from ..models.helm_repository_input_auth_bearer import HelmRepositoryInputAuthBearer
  from ..models.helm_repository_input_auth_gcp import HelmRepositoryInputAuthGcp





T = TypeVar("T", bound="HelmRepositoryInputAuth")



@_attrs_define
class HelmRepositoryInputAuth:
    """ Authentication configuration for the helm repository

        Attributes:
            aws (HelmRepositoryInputAuthAws | Unset): AWS credentials for ECR
            azure (HelmRepositoryInputAuthAzure | Unset): Azure credentials for ACR
            basic (HelmRepositoryInputAuthBasic | Unset): Basic auth credentials
            bearer (HelmRepositoryInputAuthBearer | Unset): Bearer token auth
            gcp (HelmRepositoryInputAuthGcp | Unset): GCP credentials for GCR/Artifact Registry
     """

    aws: HelmRepositoryInputAuthAws | Unset = UNSET
    azure: HelmRepositoryInputAuthAzure | Unset = UNSET
    basic: HelmRepositoryInputAuthBasic | Unset = UNSET
    bearer: HelmRepositoryInputAuthBearer | Unset = UNSET
    gcp: HelmRepositoryInputAuthGcp | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.helm_repository_input_auth_basic import HelmRepositoryInputAuthBasic
        from ..models.helm_repository_input_auth_gcp import HelmRepositoryInputAuthGcp
        from ..models.helm_repository_input_auth_azure import HelmRepositoryInputAuthAzure
        from ..models.helm_repository_input_auth_aws import HelmRepositoryInputAuthAws
        from ..models.helm_repository_input_auth_bearer import HelmRepositoryInputAuthBearer
        aws: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws, Unset):
            aws = self.aws.to_dict()

        azure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure, Unset):
            azure = self.azure.to_dict()

        basic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic, Unset):
            basic = self.basic.to_dict()

        bearer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bearer, Unset):
            bearer = self.bearer.to_dict()

        gcp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp, Unset):
            gcp = self.gcp.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aws is not UNSET:
            field_dict["aws"] = aws
        if azure is not UNSET:
            field_dict["azure"] = azure
        if basic is not UNSET:
            field_dict["basic"] = basic
        if bearer is not UNSET:
            field_dict["bearer"] = bearer
        if gcp is not UNSET:
            field_dict["gcp"] = gcp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.helm_repository_input_auth_aws import HelmRepositoryInputAuthAws
        from ..models.helm_repository_input_auth_azure import HelmRepositoryInputAuthAzure
        from ..models.helm_repository_input_auth_basic import HelmRepositoryInputAuthBasic
        from ..models.helm_repository_input_auth_bearer import HelmRepositoryInputAuthBearer
        from ..models.helm_repository_input_auth_gcp import HelmRepositoryInputAuthGcp
        d = dict(src_dict)
        _aws = d.pop("aws", UNSET)
        aws: HelmRepositoryInputAuthAws | Unset
        if isinstance(_aws,  Unset):
            aws = UNSET
        else:
            aws = HelmRepositoryInputAuthAws.from_dict(_aws)




        _azure = d.pop("azure", UNSET)
        azure: HelmRepositoryInputAuthAzure | Unset
        if isinstance(_azure,  Unset):
            azure = UNSET
        else:
            azure = HelmRepositoryInputAuthAzure.from_dict(_azure)




        _basic = d.pop("basic", UNSET)
        basic: HelmRepositoryInputAuthBasic | Unset
        if isinstance(_basic,  Unset):
            basic = UNSET
        else:
            basic = HelmRepositoryInputAuthBasic.from_dict(_basic)




        _bearer = d.pop("bearer", UNSET)
        bearer: HelmRepositoryInputAuthBearer | Unset
        if isinstance(_bearer,  Unset):
            bearer = UNSET
        else:
            bearer = HelmRepositoryInputAuthBearer.from_dict(_bearer)




        _gcp = d.pop("gcp", UNSET)
        gcp: HelmRepositoryInputAuthGcp | Unset
        if isinstance(_gcp,  Unset):
            gcp = UNSET
        else:
            gcp = HelmRepositoryInputAuthGcp.from_dict(_gcp)




        helm_repository_input_auth = cls(
            aws=aws,
            azure=azure,
            basic=basic,
            bearer=bearer,
            gcp=gcp,
        )


        helm_repository_input_auth.additional_properties = d
        return helm_repository_input_auth

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
