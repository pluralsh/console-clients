from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cluster_distro import ClusterDistro
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.cluster_metadata import ClusterMetadata
  from ..models.tag import Tag





T = TypeVar("T", bound="Cluster")



@_attrs_define
class Cluster:
    """ A Kubernetes cluster that can be deployed to and managed through the platform

        Attributes:
            tags (list[Tag] | Unset): Key/value tags to filter and organize clusters
            availability_zones (list[str] | Unset): The availability zones this cluster is running in
            cpu_total (float | Unset): The total CPU capacity of the cluster in cores
            cpu_util (float | Unset): The current CPU utilization of the cluster as a percentage
            current_version (str | Unset): Current Kubernetes version as reported by the deployment operator
            deleted_at (datetime.datetime | Unset): Timestamp when this cluster was scheduled for deletion
            distro (ClusterDistro | Unset): The distribution of kubernetes this cluster is running (generic, eks, aks, gke,
                rke, k3s, openshift)
            handle (str | Unset): A short, unique human readable name used to identify this cluster
            id (str | Unset): Unique identifier for the cluster
            inserted_at (datetime.datetime | Unset):
            installed (bool | Unset): Whether the deploy operator has been registered for this cluster
            kubelet_version (str | Unset): The lowest discovered kubelet version for all nodes in the cluster
            memory_total (float | Unset): The total memory capacity of the cluster in bytes
            memory_util (float | Unset): The current memory utilization of the cluster as a percentage
            metadata (ClusterMetadata | Unset): Arbitrary JSON metadata to store user-specific state of this cluster
            name (str | Unset): Human readable name of this cluster, will also translate to cloud k8s name
            namespace_count (int | Unset): The number of namespaces in this cluster
            node_count (int | Unset): The number of nodes in this cluster
            openshift_version (str | Unset): The version of OpenShift this cluster is running, if applicable
            pinged_at (datetime.datetime | Unset): Timestamp of the last ping from the deploy operator
            pod_count (int | Unset): The number of pods in this cluster
            project_id (str | Unset): ID of the project this cluster belongs to
            protect (bool | Unset): If true, this cluster cannot be deleted
            self_ (bool | Unset): Whether this is the management cluster itself
            updated_at (datetime.datetime | Unset):
            version (str | Unset): Desired Kubernetes version for the cluster
            virtual (bool | Unset): Whether this is a virtual cluster
     """

    tags: list[Tag] | Unset = UNSET
    availability_zones: list[str] | Unset = UNSET
    cpu_total: float | Unset = UNSET
    cpu_util: float | Unset = UNSET
    current_version: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    distro: ClusterDistro | Unset = UNSET
    handle: str | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    installed: bool | Unset = UNSET
    kubelet_version: str | Unset = UNSET
    memory_total: float | Unset = UNSET
    memory_util: float | Unset = UNSET
    metadata: ClusterMetadata | Unset = UNSET
    name: str | Unset = UNSET
    namespace_count: int | Unset = UNSET
    node_count: int | Unset = UNSET
    openshift_version: str | Unset = UNSET
    pinged_at: datetime.datetime | Unset = UNSET
    pod_count: int | Unset = UNSET
    project_id: str | Unset = UNSET
    protect: bool | Unset = UNSET
    self_: bool | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    version: str | Unset = UNSET
    virtual: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cluster_metadata import ClusterMetadata
        from ..models.tag import Tag
        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)



        availability_zones: list[str] | Unset = UNSET
        if not isinstance(self.availability_zones, Unset):
            availability_zones = self.availability_zones



        cpu_total = self.cpu_total

        cpu_util = self.cpu_util

        current_version = self.current_version

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        distro: str | Unset = UNSET
        if not isinstance(self.distro, Unset):
            distro = self.distro.value


        handle = self.handle

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        installed = self.installed

        kubelet_version = self.kubelet_version

        memory_total = self.memory_total

        memory_util = self.memory_util

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        namespace_count = self.namespace_count

        node_count = self.node_count

        openshift_version = self.openshift_version

        pinged_at: str | Unset = UNSET
        if not isinstance(self.pinged_at, Unset):
            pinged_at = self.pinged_at.isoformat()

        pod_count = self.pod_count

        project_id = self.project_id

        protect = self.protect

        self_ = self.self_

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        version = self.version

        virtual = self.virtual


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tags is not UNSET:
            field_dict["tags"] = tags
        if availability_zones is not UNSET:
            field_dict["availability_zones"] = availability_zones
        if cpu_total is not UNSET:
            field_dict["cpu_total"] = cpu_total
        if cpu_util is not UNSET:
            field_dict["cpu_util"] = cpu_util
        if current_version is not UNSET:
            field_dict["current_version"] = current_version
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if distro is not UNSET:
            field_dict["distro"] = distro
        if handle is not UNSET:
            field_dict["handle"] = handle
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if installed is not UNSET:
            field_dict["installed"] = installed
        if kubelet_version is not UNSET:
            field_dict["kubelet_version"] = kubelet_version
        if memory_total is not UNSET:
            field_dict["memory_total"] = memory_total
        if memory_util is not UNSET:
            field_dict["memory_util"] = memory_util
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if namespace_count is not UNSET:
            field_dict["namespace_count"] = namespace_count
        if node_count is not UNSET:
            field_dict["node_count"] = node_count
        if openshift_version is not UNSET:
            field_dict["openshift_version"] = openshift_version
        if pinged_at is not UNSET:
            field_dict["pinged_at"] = pinged_at
        if pod_count is not UNSET:
            field_dict["pod_count"] = pod_count
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if protect is not UNSET:
            field_dict["protect"] = protect
        if self_ is not UNSET:
            field_dict["self"] = self_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version
        if virtual is not UNSET:
            field_dict["virtual"] = virtual

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_metadata import ClusterMetadata
        from ..models.tag import Tag
        d = dict(src_dict)
        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)



                tags.append(tags_item)


        availability_zones = cast(list[str], d.pop("availability_zones", UNSET))


        cpu_total = d.pop("cpu_total", UNSET)

        cpu_util = d.pop("cpu_util", UNSET)

        current_version = d.pop("current_version", UNSET)

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at,  Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)




        _distro = d.pop("distro", UNSET)
        distro: ClusterDistro | Unset
        if isinstance(_distro,  Unset):
            distro = UNSET
        else:
            distro = ClusterDistro(_distro)




        handle = d.pop("handle", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        installed = d.pop("installed", UNSET)

        kubelet_version = d.pop("kubelet_version", UNSET)

        memory_total = d.pop("memory_total", UNSET)

        memory_util = d.pop("memory_util", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ClusterMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = ClusterMetadata.from_dict(_metadata)




        name = d.pop("name", UNSET)

        namespace_count = d.pop("namespace_count", UNSET)

        node_count = d.pop("node_count", UNSET)

        openshift_version = d.pop("openshift_version", UNSET)

        _pinged_at = d.pop("pinged_at", UNSET)
        pinged_at: datetime.datetime | Unset
        if isinstance(_pinged_at,  Unset):
            pinged_at = UNSET
        else:
            pinged_at = isoparse(_pinged_at)




        pod_count = d.pop("pod_count", UNSET)

        project_id = d.pop("project_id", UNSET)

        protect = d.pop("protect", UNSET)

        self_ = d.pop("self", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        version = d.pop("version", UNSET)

        virtual = d.pop("virtual", UNSET)

        cluster = cls(
            tags=tags,
            availability_zones=availability_zones,
            cpu_total=cpu_total,
            cpu_util=cpu_util,
            current_version=current_version,
            deleted_at=deleted_at,
            distro=distro,
            handle=handle,
            id=id,
            inserted_at=inserted_at,
            installed=installed,
            kubelet_version=kubelet_version,
            memory_total=memory_total,
            memory_util=memory_util,
            metadata=metadata,
            name=name,
            namespace_count=namespace_count,
            node_count=node_count,
            openshift_version=openshift_version,
            pinged_at=pinged_at,
            pod_count=pod_count,
            project_id=project_id,
            protect=protect,
            self_=self_,
            updated_at=updated_at,
            version=version,
            virtual=virtual,
        )


        cluster.additional_properties = d
        return cluster

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
