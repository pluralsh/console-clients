from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pr_configuration import PrConfiguration


T = TypeVar("T", bound="PrAutomation")


@_attrs_define
class PrAutomation:
    """A PR automation template for creating infrastructure or application pull requests

    Attributes:
        title (str | Unset): Title template for generated pull requests
        addon (str | Unset): Name of the addon this PR automation is associated with, if any
        branch (str | Unset): Default branch name for generated pull requests
        catalog_id (str | Unset): ID of the catalog this PR automation belongs to
        cluster_id (str | Unset): ID of the cluster this PR automation is associated with, if any
        configuration (list[PrConfiguration] | Unset): Configuration fields for the PR automation
        connection_id (str | Unset): ID of the SCM connection used for creating pull requests
        dark_icon (str | Unset): URL or reference to the PR automation's icon for dark mode
        documentation (str | Unset): Documentation describing the PR automation's purpose and usage
        icon (str | Unset): URL or reference to the PR automation's icon for light mode
        id (str | Unset): Unique identifier for the PR automation
        identifier (str | Unset): Repository identifier (e.g., owner/repo) for the PR automation
        inserted_at (datetime.datetime | Unset):
        message (str | Unset): Message/body template for generated pull requests
        name (str | Unset): Name of the PR automation
        project_id (str | Unset): ID of the project this PR automation belongs to
        service_id (str | Unset): ID of the service this PR automation is associated with, if any
        updated_at (datetime.datetime | Unset):
    """

    title: str | Unset = UNSET
    addon: str | Unset = UNSET
    branch: str | Unset = UNSET
    catalog_id: str | Unset = UNSET
    cluster_id: str | Unset = UNSET
    configuration: list[PrConfiguration] | Unset = UNSET
    connection_id: str | Unset = UNSET
    dark_icon: str | Unset = UNSET
    documentation: str | Unset = UNSET
    icon: str | Unset = UNSET
    id: str | Unset = UNSET
    identifier: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    message: str | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    service_id: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        addon = self.addon

        branch = self.branch

        catalog_id = self.catalog_id

        cluster_id = self.cluster_id

        configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = []
            for configuration_item_data in self.configuration:
                configuration_item = configuration_item_data.to_dict()
                configuration.append(configuration_item)

        connection_id = self.connection_id

        dark_icon = self.dark_icon

        documentation = self.documentation

        icon = self.icon

        id = self.id

        identifier = self.identifier

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        message = self.message

        name = self.name

        project_id = self.project_id

        service_id = self.service_id

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if addon is not UNSET:
            field_dict["addon"] = addon
        if branch is not UNSET:
            field_dict["branch"] = branch
        if catalog_id is not UNSET:
            field_dict["catalog_id"] = catalog_id
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if dark_icon is not UNSET:
            field_dict["dark_icon"] = dark_icon
        if documentation is not UNSET:
            field_dict["documentation"] = documentation
        if icon is not UNSET:
            field_dict["icon"] = icon
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pr_configuration import PrConfiguration

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        addon = d.pop("addon", UNSET)

        branch = d.pop("branch", UNSET)

        catalog_id = d.pop("catalog_id", UNSET)

        cluster_id = d.pop("cluster_id", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: list[PrConfiguration] | Unset = UNSET
        if _configuration is not UNSET:
            configuration = []
            for configuration_item_data in _configuration:
                configuration_item = PrConfiguration.from_dict(configuration_item_data)

                configuration.append(configuration_item)

        connection_id = d.pop("connection_id", UNSET)

        dark_icon = d.pop("dark_icon", UNSET)

        documentation = d.pop("documentation", UNSET)

        icon = d.pop("icon", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        project_id = d.pop("project_id", UNSET)

        service_id = d.pop("service_id", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        pr_automation = cls(
            title=title,
            addon=addon,
            branch=branch,
            catalog_id=catalog_id,
            cluster_id=cluster_id,
            configuration=configuration,
            connection_id=connection_id,
            dark_icon=dark_icon,
            documentation=documentation,
            icon=icon,
            id=id,
            identifier=identifier,
            inserted_at=inserted_at,
            message=message,
            name=name,
            project_id=project_id,
            service_id=service_id,
            updated_at=updated_at,
        )

        pr_automation.additional_properties = d
        return pr_automation

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
