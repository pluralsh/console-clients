from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.git import Git
    from ..models.helm_spec_input import HelmSpecInput
    from ..models.kustomize_input import KustomizeInput
    from ..models.service_configuration_input import ServiceConfigurationInput
    from ..models.service_renderer_input import ServiceRendererInput
    from ..models.service_source_input import ServiceSourceInput


T = TypeVar("T", bound="ServiceInput")


@_attrs_define
class ServiceInput:
    """Input for creating or updating a service deployment

    Attributes:
        name (str): Desired name for the service
        namespace (str): Target deployment namespace
        configuration (list[ServiceConfigurationInput] | Unset): Configuration values to template into the service
            manifests. You must pass the full list of configuration inputs
        dry_run (bool | Unset): If true, does not actually apply any changes to the cluster
        git (Git | Unset): Git reference configuration
        helm (HelmSpecInput | Unset): Helm chart configuration input
        kustomize (KustomizeInput | Unset): Kustomize configuration input
        protect (bool | Unset): If true, marks the service as protected from accidental changes
        renderers (list[ServiceRendererInput] | Unset): Custom renderers for processing service manifests
        repository_id (str | Unset): ID of the backing repository for this service
        sources (list[ServiceSourceInput] | Unset): Additional source repositories for this service
    """

    name: str
    namespace: str
    configuration: list[ServiceConfigurationInput] | Unset = UNSET
    dry_run: bool | Unset = UNSET
    git: Git | Unset = UNSET
    helm: HelmSpecInput | Unset = UNSET
    kustomize: KustomizeInput | Unset = UNSET
    protect: bool | Unset = UNSET
    renderers: list[ServiceRendererInput] | Unset = UNSET
    repository_id: str | Unset = UNSET
    sources: list[ServiceSourceInput] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        namespace = self.namespace

        configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = []
            for configuration_item_data in self.configuration:
                configuration_item = configuration_item_data.to_dict()
                configuration.append(configuration_item)

        dry_run = self.dry_run

        git: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git, Unset):
            git = self.git.to_dict()

        helm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.helm, Unset):
            helm = self.helm.to_dict()

        kustomize: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kustomize, Unset):
            kustomize = self.kustomize.to_dict()

        protect = self.protect

        renderers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.renderers, Unset):
            renderers = []
            for renderers_item_data in self.renderers:
                renderers_item = renderers_item_data.to_dict()
                renderers.append(renderers_item)

        repository_id = self.repository_id

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "namespace": namespace,
            }
        )
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if git is not UNSET:
            field_dict["git"] = git
        if helm is not UNSET:
            field_dict["helm"] = helm
        if kustomize is not UNSET:
            field_dict["kustomize"] = kustomize
        if protect is not UNSET:
            field_dict["protect"] = protect
        if renderers is not UNSET:
            field_dict["renderers"] = renderers
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git import Git
        from ..models.helm_spec_input import HelmSpecInput
        from ..models.kustomize_input import KustomizeInput
        from ..models.service_configuration_input import ServiceConfigurationInput
        from ..models.service_renderer_input import ServiceRendererInput
        from ..models.service_source_input import ServiceSourceInput

        d = dict(src_dict)
        name = d.pop("name")

        namespace = d.pop("namespace")

        _configuration = d.pop("configuration", UNSET)
        configuration: list[ServiceConfigurationInput] | Unset = UNSET
        if _configuration is not UNSET:
            configuration = []
            for configuration_item_data in _configuration:
                configuration_item = ServiceConfigurationInput.from_dict(
                    configuration_item_data
                )

                configuration.append(configuration_item)

        dry_run = d.pop("dry_run", UNSET)

        _git = d.pop("git", UNSET)
        git: Git | Unset
        if isinstance(_git, Unset):
            git = UNSET
        else:
            git = Git.from_dict(_git)

        _helm = d.pop("helm", UNSET)
        helm: HelmSpecInput | Unset
        if isinstance(_helm, Unset):
            helm = UNSET
        else:
            helm = HelmSpecInput.from_dict(_helm)

        _kustomize = d.pop("kustomize", UNSET)
        kustomize: KustomizeInput | Unset
        if isinstance(_kustomize, Unset):
            kustomize = UNSET
        else:
            kustomize = KustomizeInput.from_dict(_kustomize)

        protect = d.pop("protect", UNSET)

        _renderers = d.pop("renderers", UNSET)
        renderers: list[ServiceRendererInput] | Unset = UNSET
        if _renderers is not UNSET:
            renderers = []
            for renderers_item_data in _renderers:
                renderers_item = ServiceRendererInput.from_dict(renderers_item_data)

                renderers.append(renderers_item)

        repository_id = d.pop("repository_id", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: list[ServiceSourceInput] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = ServiceSourceInput.from_dict(sources_item_data)

                sources.append(sources_item)

        service_input = cls(
            name=name,
            namespace=namespace,
            configuration=configuration,
            dry_run=dry_run,
            git=git,
            helm=helm,
            kustomize=kustomize,
            protect=protect,
            renderers=renderers,
            repository_id=repository_id,
            sources=sources,
        )

        service_input.additional_properties = d
        return service_input

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
