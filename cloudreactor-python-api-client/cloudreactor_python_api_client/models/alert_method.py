import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.alert_method_method_details import AlertMethodMethodDetails
from ..models.group import Group
from ..models.name_and_uuid import NameAndUuid
from ..models.notification_severity import NotificationSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertMethod")


@attr.s(auto_attribs=True)
class AlertMethod:
    """An AlertMethod specifies one or more configured methods of notifying
    users or external sources of events that trigger when one or more
    conditions are satisfied.

        Attributes:
            url (str):
            uuid (str):
            name (str):
            dashboard_url (str):
            method_details (AlertMethodMethodDetails):
            created_by_user (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
            created_by_group (Group):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            description (Union[Unset, str]):
            enabled (Union[Unset, bool]):
            notify_on_success (Union[Unset, bool]):
            notify_on_failure (Union[Unset, bool]):
            notify_on_timeout (Union[Unset, bool]):
            error_severity_on_missing_execution (Union[Unset, NotificationSeverity]):
            error_severity_on_missing_heartbeat (Union[Unset, NotificationSeverity]):
            error_severity_on_service_down (Union[Unset, NotificationSeverity]):
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
    method_details: AlertMethodMethodDetails
    created_by_user: str
    created_by_group: Group
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    notify_on_success: Union[Unset, bool] = UNSET
    notify_on_failure: Union[Unset, bool] = UNSET
    notify_on_timeout: Union[Unset, bool] = UNSET
    error_severity_on_missing_execution: Union[Unset, NotificationSeverity] = UNSET
    error_severity_on_missing_heartbeat: Union[Unset, NotificationSeverity] = UNSET
    error_severity_on_service_down: Union[Unset, NotificationSeverity] = UNSET
    run_environment: Union[Unset, None, NameAndUuid] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        uuid = self.uuid
        name = self.name
        dashboard_url = self.dashboard_url
        method_details = self.method_details.to_dict()

        created_by_user = self.created_by_user
        created_by_group = self.created_by_group.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description
        enabled = self.enabled
        notify_on_success = self.notify_on_success
        notify_on_failure = self.notify_on_failure
        notify_on_timeout = self.notify_on_timeout
        error_severity_on_missing_execution: Union[Unset, str] = UNSET
        if not isinstance(self.error_severity_on_missing_execution, Unset):
            error_severity_on_missing_execution = self.error_severity_on_missing_execution.value

        error_severity_on_missing_heartbeat: Union[Unset, str] = UNSET
        if not isinstance(self.error_severity_on_missing_heartbeat, Unset):
            error_severity_on_missing_heartbeat = self.error_severity_on_missing_heartbeat.value

        error_severity_on_service_down: Union[Unset, str] = UNSET
        if not isinstance(self.error_severity_on_service_down, Unset):
            error_severity_on_service_down = self.error_severity_on_service_down.value

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
                "method_details": method_details,
                "created_by_user": created_by_user,
                "created_by_group": created_by_group,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if notify_on_success is not UNSET:
            field_dict["notify_on_success"] = notify_on_success
        if notify_on_failure is not UNSET:
            field_dict["notify_on_failure"] = notify_on_failure
        if notify_on_timeout is not UNSET:
            field_dict["notify_on_timeout"] = notify_on_timeout
        if error_severity_on_missing_execution is not UNSET:
            field_dict["error_severity_on_missing_execution"] = error_severity_on_missing_execution
        if error_severity_on_missing_heartbeat is not UNSET:
            field_dict["error_severity_on_missing_heartbeat"] = error_severity_on_missing_heartbeat
        if error_severity_on_service_down is not UNSET:
            field_dict["error_severity_on_service_down"] = error_severity_on_service_down
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
        method_details = (None, json.dumps(self.method_details.to_dict()).encode(), "application/json")

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
        enabled = self.enabled if isinstance(self.enabled, Unset) else (None, str(self.enabled).encode(), "text/plain")
        notify_on_success = (
            self.notify_on_success
            if isinstance(self.notify_on_success, Unset)
            else (None, str(self.notify_on_success).encode(), "text/plain")
        )
        notify_on_failure = (
            self.notify_on_failure
            if isinstance(self.notify_on_failure, Unset)
            else (None, str(self.notify_on_failure).encode(), "text/plain")
        )
        notify_on_timeout = (
            self.notify_on_timeout
            if isinstance(self.notify_on_timeout, Unset)
            else (None, str(self.notify_on_timeout).encode(), "text/plain")
        )
        error_severity_on_missing_execution: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.error_severity_on_missing_execution, Unset):
            error_severity_on_missing_execution = (
                None,
                str(self.error_severity_on_missing_execution.value).encode(),
                "text/plain",
            )

        error_severity_on_missing_heartbeat: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.error_severity_on_missing_heartbeat, Unset):
            error_severity_on_missing_heartbeat = (
                None,
                str(self.error_severity_on_missing_heartbeat.value).encode(),
                "text/plain",
            )

        error_severity_on_service_down: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.error_severity_on_service_down, Unset):
            error_severity_on_service_down = (
                None,
                str(self.error_severity_on_service_down.value).encode(),
                "text/plain",
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
                "method_details": method_details,
                "created_by_user": created_by_user,
                "created_by_group": created_by_group,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if notify_on_success is not UNSET:
            field_dict["notify_on_success"] = notify_on_success
        if notify_on_failure is not UNSET:
            field_dict["notify_on_failure"] = notify_on_failure
        if notify_on_timeout is not UNSET:
            field_dict["notify_on_timeout"] = notify_on_timeout
        if error_severity_on_missing_execution is not UNSET:
            field_dict["error_severity_on_missing_execution"] = error_severity_on_missing_execution
        if error_severity_on_missing_heartbeat is not UNSET:
            field_dict["error_severity_on_missing_heartbeat"] = error_severity_on_missing_heartbeat
        if error_severity_on_service_down is not UNSET:
            field_dict["error_severity_on_service_down"] = error_severity_on_service_down
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

        method_details = AlertMethodMethodDetails.from_dict(d.pop("method_details"))

        created_by_user = d.pop("created_by_user")

        created_by_group = Group.from_dict(d.pop("created_by_group"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        notify_on_success = d.pop("notify_on_success", UNSET)

        notify_on_failure = d.pop("notify_on_failure", UNSET)

        notify_on_timeout = d.pop("notify_on_timeout", UNSET)

        _error_severity_on_missing_execution = d.pop("error_severity_on_missing_execution", UNSET)
        error_severity_on_missing_execution: Union[Unset, NotificationSeverity]
        if isinstance(_error_severity_on_missing_execution, Unset):
            error_severity_on_missing_execution = UNSET
        else:
            error_severity_on_missing_execution = NotificationSeverity(_error_severity_on_missing_execution)

        _error_severity_on_missing_heartbeat = d.pop("error_severity_on_missing_heartbeat", UNSET)
        error_severity_on_missing_heartbeat: Union[Unset, NotificationSeverity]
        if isinstance(_error_severity_on_missing_heartbeat, Unset):
            error_severity_on_missing_heartbeat = UNSET
        else:
            error_severity_on_missing_heartbeat = NotificationSeverity(_error_severity_on_missing_heartbeat)

        _error_severity_on_service_down = d.pop("error_severity_on_service_down", UNSET)
        error_severity_on_service_down: Union[Unset, NotificationSeverity]
        if isinstance(_error_severity_on_service_down, Unset):
            error_severity_on_service_down = UNSET
        else:
            error_severity_on_service_down = NotificationSeverity(_error_severity_on_service_down)

        _run_environment = d.pop("run_environment", UNSET)
        run_environment: Union[Unset, None, NameAndUuid]
        if _run_environment is None:
            run_environment = None
        elif isinstance(_run_environment, Unset):
            run_environment = UNSET
        else:
            run_environment = NameAndUuid.from_dict(_run_environment)

        alert_method = cls(
            url=url,
            uuid=uuid,
            name=name,
            dashboard_url=dashboard_url,
            method_details=method_details,
            created_by_user=created_by_user,
            created_by_group=created_by_group,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            enabled=enabled,
            notify_on_success=notify_on_success,
            notify_on_failure=notify_on_failure,
            notify_on_timeout=notify_on_timeout,
            error_severity_on_missing_execution=error_severity_on_missing_execution,
            error_severity_on_missing_heartbeat=error_severity_on_missing_heartbeat,
            error_severity_on_service_down=error_severity_on_service_down,
            run_environment=run_environment,
        )

        alert_method.additional_properties = d
        return alert_method

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
