from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pr_configuration_type import PrConfigurationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pr_configuration_validation import PrConfigurationValidation


T = TypeVar("T", bound="PrConfiguration")


@_attrs_define
class PrConfiguration:
    """A configuration field for a PR automation

    Attributes:
        default (str | Unset): Default value for the configuration field
        documentation (str | Unset): Documentation describing the configuration field
        longform (str | Unset): Extended documentation for the configuration field
        name (str | Unset): Name of the configuration field
        optional (bool | Unset): Whether the configuration field is optional
        placeholder (str | Unset): Placeholder text for the configuration field input
        type_ (PrConfigurationType | Unset): Type of the configuration field (string, int, bool, domain, file, function,
            enum, password)
        validation (PrConfigurationValidation | Unset): Validation rules for a configuration field
    """

    default: str | Unset = UNSET
    documentation: str | Unset = UNSET
    longform: str | Unset = UNSET
    name: str | Unset = UNSET
    optional: bool | Unset = UNSET
    placeholder: str | Unset = UNSET
    type_: PrConfigurationType | Unset = UNSET
    validation: PrConfigurationValidation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default

        documentation = self.documentation

        longform = self.longform

        name = self.name

        optional = self.optional

        placeholder = self.placeholder

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        validation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.validation, Unset):
            validation = self.validation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default is not UNSET:
            field_dict["default"] = default
        if documentation is not UNSET:
            field_dict["documentation"] = documentation
        if longform is not UNSET:
            field_dict["longform"] = longform
        if name is not UNSET:
            field_dict["name"] = name
        if optional is not UNSET:
            field_dict["optional"] = optional
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if type_ is not UNSET:
            field_dict["type"] = type_
        if validation is not UNSET:
            field_dict["validation"] = validation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pr_configuration_validation import PrConfigurationValidation

        d = dict(src_dict)
        default = d.pop("default", UNSET)

        documentation = d.pop("documentation", UNSET)

        longform = d.pop("longform", UNSET)

        name = d.pop("name", UNSET)

        optional = d.pop("optional", UNSET)

        placeholder = d.pop("placeholder", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PrConfigurationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PrConfigurationType(_type_)

        _validation = d.pop("validation", UNSET)
        validation: PrConfigurationValidation | Unset
        if isinstance(_validation, Unset):
            validation = UNSET
        else:
            validation = PrConfigurationValidation.from_dict(_validation)

        pr_configuration = cls(
            default=default,
            documentation=documentation,
            longform=longform,
            name=name,
            optional=optional,
            placeholder=placeholder,
            type_=type_,
            validation=validation,
        )

        pr_configuration.additional_properties = d
        return pr_configuration

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
