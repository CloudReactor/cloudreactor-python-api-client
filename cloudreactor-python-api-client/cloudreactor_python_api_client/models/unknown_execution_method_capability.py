from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="UnknownExecutionMethodCapability")


@attr.s(auto_attribs=True)
class UnknownExecutionMethodCapability:
    """A ModelSerializer that takes additional arguments for
    "fields", "omit" and "expand" in order to
    control which fields are displayed, and whether to replace simple
    values with complex, nested serializations

        Attributes:
            type (str):
            capabilities (List[str]):
    """

    type: str
    capabilities: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        capabilities = self.capabilities

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "capabilities": capabilities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        capabilities = cast(List[str], d.pop("capabilities"))

        unknown_execution_method_capability = cls(
            type=type,
            capabilities=capabilities,
        )

        unknown_execution_method_capability.additional_properties = d
        return unknown_execution_method_capability

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
