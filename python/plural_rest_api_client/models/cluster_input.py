from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_input_metadata import ClusterInputMetadata
    from ..models.tag_input import TagInput


T = TypeVar("T", bound="ClusterInput")


@_attrs_define
class ClusterInput:
    """Input for creating or updating a cluster

    Attributes:
        tags (list[TagInput] | Unset): Key/value tags to filter and organize clusters
        handle (str | Unset): A short, unique human readable name used to identify this cluster
        metadata (ClusterInputMetadata | Unset): Arbitrary JSON metadata to store user-specific state
        name (str | Unset): Human readable name for the cluster
        project_id (str | Unset): ID of the project this cluster belongs to
    """

    tags: list[TagInput] | Unset = UNSET
    handle: str | Unset = UNSET
    metadata: ClusterInputMetadata | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        handle = self.handle

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if handle is not UNSET:
            field_dict["handle"] = handle
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_input_metadata import ClusterInputMetadata
        from ..models.tag_input import TagInput

        d = dict(src_dict)
        _tags = d.pop("tags", UNSET)
        tags: list[TagInput] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = TagInput.from_dict(tags_item_data)

                tags.append(tags_item)

        handle = d.pop("handle", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ClusterInputMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ClusterInputMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        project_id = d.pop("project_id", UNSET)

        cluster_input = cls(
            tags=tags,
            handle=handle,
            metadata=metadata,
            name=name,
            project_id=project_id,
        )

        cluster_input.additional_properties = d
        return cluster_input

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
