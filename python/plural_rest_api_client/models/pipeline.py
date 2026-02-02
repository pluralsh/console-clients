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
  from ..models.pipeline_edge import PipelineEdge
  from ..models.pipeline_stage import PipelineStage





T = TypeVar("T", bound="Pipeline")



@_attrs_define
class Pipeline:
    """ A continuous deployment pipeline that orchestrates service promotions through stages

        Attributes:
            edges (list[PipelineEdge] | Unset): Edges connecting stages with promotion gates
            id (str | Unset): Unique identifier for the pipeline
            inserted_at (datetime.datetime | Unset):
            name (str | Unset): Name of the pipeline
            project_id (str | Unset): ID of the project this pipeline belongs to
            stages (list[PipelineStage] | Unset): Ordered list of stages in this pipeline
            updated_at (datetime.datetime | Unset):
     """

    edges: list[PipelineEdge] | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    stages: list[PipelineStage] | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pipeline_edge import PipelineEdge
        from ..models.pipeline_stage import PipelineStage
        edges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edges, Unset):
            edges = []
            for edges_item_data in self.edges:
                edges_item = edges_item_data.to_dict()
                edges.append(edges_item)



        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        name = self.name

        project_id = self.project_id

        stages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)



        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if edges is not UNSET:
            field_dict["edges"] = edges
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if stages is not UNSET:
            field_dict["stages"] = stages
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_edge import PipelineEdge
        from ..models.pipeline_stage import PipelineStage
        d = dict(src_dict)
        _edges = d.pop("edges", UNSET)
        edges: list[PipelineEdge] | Unset = UNSET
        if _edges is not UNSET:
            edges = []
            for edges_item_data in _edges:
                edges_item = PipelineEdge.from_dict(edges_item_data)



                edges.append(edges_item)


        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at,  Unset):
            inserted_at = UNSET
        else:
            inserted_at = isoparse(_inserted_at)




        name = d.pop("name", UNSET)

        project_id = d.pop("project_id", UNSET)

        _stages = d.pop("stages", UNSET)
        stages: list[PipelineStage] | Unset = UNSET
        if _stages is not UNSET:
            stages = []
            for stages_item_data in _stages:
                stages_item = PipelineStage.from_dict(stages_item_data)



                stages.append(stages_item)


        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        pipeline = cls(
            edges=edges,
            id=id,
            inserted_at=inserted_at,
            name=name,
            project_id=project_id,
            stages=stages,
            updated_at=updated_at,
        )


        pipeline.additional_properties = d
        return pipeline

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
