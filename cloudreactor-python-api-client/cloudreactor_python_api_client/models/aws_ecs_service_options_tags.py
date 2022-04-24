from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="AwsEcsServiceOptionsTags")


@attr.s(auto_attribs=True)
class AwsEcsServiceOptionsTags:
    """ """

    additional_properties: Dict[str, Optional[str]] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aws_ecs_service_options_tags = cls()

        aws_ecs_service_options_tags.additional_properties = d
        return aws_ecs_service_options_tags

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Optional[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Optional[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
