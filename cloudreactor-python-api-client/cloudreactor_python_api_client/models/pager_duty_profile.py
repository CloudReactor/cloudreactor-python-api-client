import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.group import Group
from ..models.name_and_uuid import NameAndUuid
from ..models.notification_severity import NotificationSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="PagerDutyProfile")


@attr.s(auto_attribs=True)
class PagerDutyProfile:
    """A PagerDutyProfile contains user-specific configuration on how to notify
    PagerDuty of events.

        Attributes:
            url (str):
            uuid (str):
            name (str):
            dashboard_url (str):
            integration_key (str):
            created_by_user (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
            created_by_group (Group):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            description (Union[Unset, str]):
            default_event_severity (Union[Unset, NotificationSeverity]):
            default_event_component_template (Union[Unset, str]):
            default_event_group_template (Union[Unset, str]):
            default_event_class_template (Union[Unset, str]):
            run_environment (Union[Unset, None, NameAndUuid]): Identifies an entity in three ways: 1. UUID; 2. Name; and 3.
                URL.
                When used to indentify an entity in a request method body, only one of
                uuid and name needs to be specified. If both are present, they must
                refer to the same entity or else the response will be a 400 error.
    """

    url: str
    uuid: str
    name: str
    dashboard_url: str
    integration_key: str
    created_by_user: str
    created_by_group: Group
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    default_event_severity: Union[Unset, NotificationSeverity] = UNSET
    default_event_component_template: Union[Unset, str] = UNSET
    default_event_group_template: Union[Unset, str] = UNSET
    default_event_class_template: Union[Unset, str] = UNSET
    run_environment: Union[Unset, None, NameAndUuid] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        uuid = self.uuid
        name = self.name
        dashboard_url = self.dashboard_url
        integration_key = self.integration_key
        created_by_user = self.created_by_user
        created_by_group = self.created_by_group.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description
        default_event_severity: Union[Unset, str] = UNSET
        if not isinstance(self.default_event_severity, Unset):
            default_event_severity = self.default_event_severity.value

        default_event_component_template = self.default_event_component_template
        default_event_group_template = self.default_event_group_template
        default_event_class_template = self.default_event_class_template
        run_environment: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.run_environment, Unset):
            run_environment = self.run_environment.to_dict() if self.run_environment else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "dashboard_url": dashboard_url,
                "integration_key": integration_key,
                "created_by_user": created_by_user,
                "created_by_group": created_by_group,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if default_event_severity is not UNSET:
            field_dict["default_event_severity"] = default_event_severity
        if default_event_component_template is not UNSET:
            field_dict["default_event_component_template"] = default_event_component_template
        if default_event_group_template is not UNSET:
            field_dict["default_event_group_template"] = default_event_group_template
        if default_event_class_template is not UNSET:
            field_dict["default_event_class_template"] = default_event_class_template
        if run_environment is not UNSET:
            field_dict["run_environment"] = run_environment

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        uuid = self.uuid if isinstance(self.uuid, Unset) else (None, str(self.uuid).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        dashboard_url = (
            self.dashboard_url
            if isinstance(self.dashboard_url, Unset)
            else (None, str(self.dashboard_url).encode(), "text/plain")
        )
        integration_key = (
            self.integration_key
            if isinstance(self.integration_key, Unset)
            else (None, str(self.integration_key).encode(), "text/plain")
        )
        created_by_user = (
            self.created_by_user
            if isinstance(self.created_by_user, Unset)
            else (None, str(self.created_by_user).encode(), "text/plain")
        )
        created_by_group = (None, json.dumps(self.created_by_group.to_dict()).encode(), "application/json")

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        default_event_severity: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.default_event_severity, Unset):
            default_event_severity = (None, str(self.default_event_severity.value).encode(), "text/plain")

        default_event_component_template = (
            self.default_event_component_template
            if isinstance(self.default_event_component_template, Unset)
            else (None, str(self.default_event_component_template).encode(), "text/plain")
        )
        default_event_group_template = (
            self.default_event_group_template
            if isinstance(self.default_event_group_template, Unset)
            else (None, str(self.default_event_group_template).encode(), "text/plain")
        )
        default_event_class_template = (
            self.default_event_class_template
            if isinstance(self.default_event_class_template, Unset)
            else (None, str(self.default_event_class_template).encode(), "text/plain")
        )
        run_environment: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.run_environment, Unset):
            run_environment = (
                (None, json.dumps(self.run_environment.to_dict()).encode(), "application/json")
                if self.run_environment
                else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "dashboard_url": dashboard_url,
                "integration_key": integration_key,
                "created_by_user": created_by_user,
                "created_by_group": created_by_group,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if default_event_severity is not UNSET:
            field_dict["default_event_severity"] = default_event_severity
        if default_event_component_template is not UNSET:
            field_dict["default_event_component_template"] = default_event_component_template
        if default_event_group_template is not UNSET:
            field_dict["default_event_group_template"] = default_event_group_template
        if default_event_class_template is not UNSET:
            field_dict["default_event_class_template"] = default_event_class_template
        if run_environment is not UNSET:
            field_dict["run_environment"] = run_environment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = d.pop("uuid")

        name = d.pop("name")

        dashboard_url = d.pop("dashboard_url")

        integration_key = d.pop("integration_key")

        created_by_user = d.pop("created_by_user")

        created_by_group = Group.from_dict(d.pop("created_by_group"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        _default_event_severity = d.pop("default_event_severity", UNSET)
        default_event_severity: Union[Unset, NotificationSeverity]
        if isinstance(_default_event_severity, Unset):
            default_event_severity = UNSET
        else:
            default_event_severity = NotificationSeverity(_default_event_severity)

        default_event_component_template = d.pop("default_event_component_template", UNSET)

        default_event_group_template = d.pop("default_event_group_template", UNSET)

        default_event_class_template = d.pop("default_event_class_template", UNSET)

        _run_environment = d.pop("run_environment", UNSET)
        run_environment: Union[Unset, None, NameAndUuid]
        if _run_environment is None:
            run_environment = None
        elif isinstance(_run_environment, Unset):
            run_environment = UNSET
        else:
            run_environment = NameAndUuid.from_dict(_run_environment)

        pager_duty_profile = cls(
            url=url,
            uuid=uuid,
            name=name,
            dashboard_url=dashboard_url,
            integration_key=integration_key,
            created_by_user=created_by_user,
            created_by_group=created_by_group,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            default_event_severity=default_event_severity,
            default_event_component_template=default_event_component_template,
            default_event_group_template=default_event_group_template,
            default_event_class_template=default_event_class_template,
            run_environment=run_environment,
        )

        pager_duty_profile.additional_properties = d
        return pager_duty_profile

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
