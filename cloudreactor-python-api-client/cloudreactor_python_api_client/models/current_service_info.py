import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="CurrentServiceInfo")


@attr.s(auto_attribs=True)
class CurrentServiceInfo:
    """
    Attributes:
        type (str):
        service_arn (str):
        service_infrastructure_website_url (Optional[str]):
        service_arn_updated_at (Optional[datetime.datetime]):
    """

    type: str
    service_arn: str
    service_infrastructure_website_url: Optional[str]
    service_arn_updated_at: Optional[datetime.datetime]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        service_arn = self.service_arn
        service_infrastructure_website_url = self.service_infrastructure_website_url
        service_arn_updated_at = self.service_arn_updated_at.isoformat() if self.service_arn_updated_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "service_arn": service_arn,
                "service_infrastructure_website_url": service_infrastructure_website_url,
                "service_arn_updated_at": service_arn_updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        service_arn = d.pop("service_arn")

        service_infrastructure_website_url = d.pop("service_infrastructure_website_url")

        _service_arn_updated_at = d.pop("service_arn_updated_at")
        service_arn_updated_at: Optional[datetime.datetime]
        if _service_arn_updated_at is None:
            service_arn_updated_at = None
        else:
            service_arn_updated_at = isoparse(_service_arn_updated_at)

        current_service_info = cls(
            type=type,
            service_arn=service_arn,
            service_infrastructure_website_url=service_infrastructure_website_url,
            service_arn_updated_at=service_arn_updated_at,
        )

        current_service_info.additional_properties = d
        return current_service_info

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
