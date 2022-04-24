import datetime
import json
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.aws_ecs_execution_method_capability import AwsEcsExecutionMethodCapability
from ..models.current_service_info import CurrentServiceInfo
from ..models.group import Group
from ..models.link import Link
from ..models.name_and_uuid import NameAndUuid
from ..models.task_execution import TaskExecution
from ..models.task_other_metadata import TaskOtherMetadata
from ..models.unknown_execution_method_capability import UnknownExecutionMethodCapability
from ..types import UNSET, Unset

T = TypeVar("T", bound="Task")


@attr.s(auto_attribs=True)
class Task:
    """A Task is a specification for a runnable job, including details on how to
    run the task and how often the task is supposed to run.

        Attributes:
            url (str):
            uuid (str):
            name (str):
            dashboard_url (str):
            is_service (bool):
            execution_method_capability (Union[AwsEcsExecutionMethodCapability, UnknownExecutionMethodCapability]):
            latest_task_execution (TaskExecution): A Task Execution is an execution / run instance of a Task.
            current_service_info (CurrentServiceInfo):
            created_by_user (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
            created_by_group (Group):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            description (Union[Unset, str]):
            infrastructure_website_url (Optional[str]):
            max_manual_start_delay_before_alert_seconds (Union[Unset, None, int]):
            max_manual_start_delay_before_abandonment_seconds (Union[Unset, None, int]):
            heartbeat_interval_seconds (Union[Unset, None, int]):
            max_heartbeat_lateness_before_alert_seconds (Union[Unset, None, int]):
            max_heartbeat_lateness_before_abandonment_seconds (Union[Unset, None, int]):
            schedule (Union[Unset, str]):
            scheduled_instance_count (Union[Unset, None, int]):
            service_instance_count (Union[Unset, None, int]):
            min_service_instance_count (Union[Unset, None, int]):
            max_concurrency (Union[Unset, None, int]):
            max_age_seconds (Union[Unset, None, int]):
            default_max_retries (Union[Unset, int]):
            project_url (Union[Unset, str]):
            log_query (Union[Unset, str]):
            logs_url (Optional[str]):
            links (Union[Unset, List[Link]]):
            run_environment (Union[Unset, None, NameAndUuid]): Identifies an entity in three ways: 1. UUID; 2. Name; and 3.
                URL.
                When used to indentify an entity in a request method body, only one of
                uuid and name needs to be specified. If both are present, they must
                refer to the same entity or else the response will be a 400 error.
            alert_methods (Union[Unset, List[NameAndUuid]]):
            other_metadata (Union[Unset, None, TaskOtherMetadata]):
            was_auto_created (Union[Unset, None, bool]):
            passive (Union[Unset, bool]):
            enabled (Union[Unset, bool]):
    """

    url: str
    uuid: str
    name: str
    dashboard_url: str
    is_service: bool
    execution_method_capability: Union[AwsEcsExecutionMethodCapability, UnknownExecutionMethodCapability]
    latest_task_execution: TaskExecution
    current_service_info: CurrentServiceInfo
    created_by_user: str
    created_by_group: Group
    created_at: datetime.datetime
    updated_at: datetime.datetime
    infrastructure_website_url: Optional[str]
    logs_url: Optional[str]
    description: Union[Unset, str] = UNSET
    max_manual_start_delay_before_alert_seconds: Union[Unset, None, int] = UNSET
    max_manual_start_delay_before_abandonment_seconds: Union[Unset, None, int] = UNSET
    heartbeat_interval_seconds: Union[Unset, None, int] = UNSET
    max_heartbeat_lateness_before_alert_seconds: Union[Unset, None, int] = UNSET
    max_heartbeat_lateness_before_abandonment_seconds: Union[Unset, None, int] = UNSET
    schedule: Union[Unset, str] = UNSET
    scheduled_instance_count: Union[Unset, None, int] = UNSET
    service_instance_count: Union[Unset, None, int] = UNSET
    min_service_instance_count: Union[Unset, None, int] = UNSET
    max_concurrency: Union[Unset, None, int] = UNSET
    max_age_seconds: Union[Unset, None, int] = UNSET
    default_max_retries: Union[Unset, int] = UNSET
    project_url: Union[Unset, str] = UNSET
    log_query: Union[Unset, str] = UNSET
    links: Union[Unset, List[Link]] = UNSET
    run_environment: Union[Unset, None, NameAndUuid] = UNSET
    alert_methods: Union[Unset, List[NameAndUuid]] = UNSET
    other_metadata: Union[Unset, None, TaskOtherMetadata] = UNSET
    was_auto_created: Union[Unset, None, bool] = UNSET
    passive: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        uuid = self.uuid
        name = self.name
        dashboard_url = self.dashboard_url
        is_service = self.is_service

        if isinstance(self.execution_method_capability, AwsEcsExecutionMethodCapability):
            execution_method_capability = self.execution_method_capability.to_dict()

        else:
            execution_method_capability = self.execution_method_capability.to_dict()

        latest_task_execution = self.latest_task_execution.to_dict()

        current_service_info = self.current_service_info.to_dict()

        created_by_user = self.created_by_user
        created_by_group = self.created_by_group.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description
        infrastructure_website_url = self.infrastructure_website_url
        max_manual_start_delay_before_alert_seconds = self.max_manual_start_delay_before_alert_seconds
        max_manual_start_delay_before_abandonment_seconds = self.max_manual_start_delay_before_abandonment_seconds
        heartbeat_interval_seconds = self.heartbeat_interval_seconds
        max_heartbeat_lateness_before_alert_seconds = self.max_heartbeat_lateness_before_alert_seconds
        max_heartbeat_lateness_before_abandonment_seconds = self.max_heartbeat_lateness_before_abandonment_seconds
        schedule = self.schedule
        scheduled_instance_count = self.scheduled_instance_count
        service_instance_count = self.service_instance_count
        min_service_instance_count = self.min_service_instance_count
        max_concurrency = self.max_concurrency
        max_age_seconds = self.max_age_seconds
        default_max_retries = self.default_max_retries
        project_url = self.project_url
        log_query = self.log_query
        logs_url = self.logs_url
        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()

                links.append(links_item)

        run_environment: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.run_environment, Unset):
            run_environment = self.run_environment.to_dict() if self.run_environment else None

        alert_methods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alert_methods, Unset):
            alert_methods = []
            for alert_methods_item_data in self.alert_methods:
                alert_methods_item = alert_methods_item_data.to_dict()

                alert_methods.append(alert_methods_item)

        other_metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.other_metadata, Unset):
            other_metadata = self.other_metadata.to_dict() if self.other_metadata else None

        was_auto_created = self.was_auto_created
        passive = self.passive
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "dashboard_url": dashboard_url,
                "is_service": is_service,
                "execution_method_capability": execution_method_capability,
                "latest_task_execution": latest_task_execution,
                "current_service_info": current_service_info,
                "created_by_user": created_by_user,
                "created_by_group": created_by_group,
                "created_at": created_at,
                "updated_at": updated_at,
                "infrastructure_website_url": infrastructure_website_url,
                "logs_url": logs_url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if max_manual_start_delay_before_alert_seconds is not UNSET:
            field_dict["max_manual_start_delay_before_alert_seconds"] = max_manual_start_delay_before_alert_seconds
        if max_manual_start_delay_before_abandonment_seconds is not UNSET:
            field_dict[
                "max_manual_start_delay_before_abandonment_seconds"
            ] = max_manual_start_delay_before_abandonment_seconds
        if heartbeat_interval_seconds is not UNSET:
            field_dict["heartbeat_interval_seconds"] = heartbeat_interval_seconds
        if max_heartbeat_lateness_before_alert_seconds is not UNSET:
            field_dict["max_heartbeat_lateness_before_alert_seconds"] = max_heartbeat_lateness_before_alert_seconds
        if max_heartbeat_lateness_before_abandonment_seconds is not UNSET:
            field_dict[
                "max_heartbeat_lateness_before_abandonment_seconds"
            ] = max_heartbeat_lateness_before_abandonment_seconds
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if scheduled_instance_count is not UNSET:
            field_dict["scheduled_instance_count"] = scheduled_instance_count
        if service_instance_count is not UNSET:
            field_dict["service_instance_count"] = service_instance_count
        if min_service_instance_count is not UNSET:
            field_dict["min_service_instance_count"] = min_service_instance_count
        if max_concurrency is not UNSET:
            field_dict["max_concurrency"] = max_concurrency
        if max_age_seconds is not UNSET:
            field_dict["max_age_seconds"] = max_age_seconds
        if default_max_retries is not UNSET:
            field_dict["default_max_retries"] = default_max_retries
        if project_url is not UNSET:
            field_dict["project_url"] = project_url
        if log_query is not UNSET:
            field_dict["log_query"] = log_query
        if links is not UNSET:
            field_dict["links"] = links
        if run_environment is not UNSET:
            field_dict["run_environment"] = run_environment
        if alert_methods is not UNSET:
            field_dict["alert_methods"] = alert_methods
        if other_metadata is not UNSET:
            field_dict["other_metadata"] = other_metadata
        if was_auto_created is not UNSET:
            field_dict["was_auto_created"] = was_auto_created
        if passive is not UNSET:
            field_dict["passive"] = passive
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

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
        is_service = (
            self.is_service
            if isinstance(self.is_service, Unset)
            else (None, str(self.is_service).encode(), "text/plain")
        )

        if isinstance(self.execution_method_capability, AwsEcsExecutionMethodCapability):
            execution_method_capability = (
                None,
                json.dumps(self.execution_method_capability.to_dict()).encode(),
                "application/json",
            )

        else:
            execution_method_capability = (
                None,
                json.dumps(self.execution_method_capability.to_dict()).encode(),
                "application/json",
            )

        latest_task_execution = (None, json.dumps(self.latest_task_execution.to_dict()).encode(), "application/json")

        current_service_info = (None, json.dumps(self.current_service_info.to_dict()).encode(), "application/json")

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
        infrastructure_website_url = (
            self.infrastructure_website_url
            if isinstance(self.infrastructure_website_url, Unset)
            else (None, str(self.infrastructure_website_url).encode(), "text/plain")
        )
        max_manual_start_delay_before_alert_seconds = (
            self.max_manual_start_delay_before_alert_seconds
            if isinstance(self.max_manual_start_delay_before_alert_seconds, Unset)
            else (None, str(self.max_manual_start_delay_before_alert_seconds).encode(), "text/plain")
        )
        max_manual_start_delay_before_abandonment_seconds = (
            self.max_manual_start_delay_before_abandonment_seconds
            if isinstance(self.max_manual_start_delay_before_abandonment_seconds, Unset)
            else (None, str(self.max_manual_start_delay_before_abandonment_seconds).encode(), "text/plain")
        )
        heartbeat_interval_seconds = (
            self.heartbeat_interval_seconds
            if isinstance(self.heartbeat_interval_seconds, Unset)
            else (None, str(self.heartbeat_interval_seconds).encode(), "text/plain")
        )
        max_heartbeat_lateness_before_alert_seconds = (
            self.max_heartbeat_lateness_before_alert_seconds
            if isinstance(self.max_heartbeat_lateness_before_alert_seconds, Unset)
            else (None, str(self.max_heartbeat_lateness_before_alert_seconds).encode(), "text/plain")
        )
        max_heartbeat_lateness_before_abandonment_seconds = (
            self.max_heartbeat_lateness_before_abandonment_seconds
            if isinstance(self.max_heartbeat_lateness_before_abandonment_seconds, Unset)
            else (None, str(self.max_heartbeat_lateness_before_abandonment_seconds).encode(), "text/plain")
        )
        schedule = (
            self.schedule if isinstance(self.schedule, Unset) else (None, str(self.schedule).encode(), "text/plain")
        )
        scheduled_instance_count = (
            self.scheduled_instance_count
            if isinstance(self.scheduled_instance_count, Unset)
            else (None, str(self.scheduled_instance_count).encode(), "text/plain")
        )
        service_instance_count = (
            self.service_instance_count
            if isinstance(self.service_instance_count, Unset)
            else (None, str(self.service_instance_count).encode(), "text/plain")
        )
        min_service_instance_count = (
            self.min_service_instance_count
            if isinstance(self.min_service_instance_count, Unset)
            else (None, str(self.min_service_instance_count).encode(), "text/plain")
        )
        max_concurrency = (
            self.max_concurrency
            if isinstance(self.max_concurrency, Unset)
            else (None, str(self.max_concurrency).encode(), "text/plain")
        )
        max_age_seconds = (
            self.max_age_seconds
            if isinstance(self.max_age_seconds, Unset)
            else (None, str(self.max_age_seconds).encode(), "text/plain")
        )
        default_max_retries = (
            self.default_max_retries
            if isinstance(self.default_max_retries, Unset)
            else (None, str(self.default_max_retries).encode(), "text/plain")
        )
        project_url = (
            self.project_url
            if isinstance(self.project_url, Unset)
            else (None, str(self.project_url).encode(), "text/plain")
        )
        log_query = (
            self.log_query if isinstance(self.log_query, Unset) else (None, str(self.log_query).encode(), "text/plain")
        )
        logs_url = (
            self.logs_url if isinstance(self.logs_url, Unset) else (None, str(self.logs_url).encode(), "text/plain")
        )
        links: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.links, Unset):
            _temp_links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()

                _temp_links.append(links_item)
            links = (None, json.dumps(_temp_links).encode(), "application/json")

        run_environment: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.run_environment, Unset):
            run_environment = (
                (None, json.dumps(self.run_environment.to_dict()).encode(), "application/json")
                if self.run_environment
                else None
            )

        alert_methods: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.alert_methods, Unset):
            _temp_alert_methods = []
            for alert_methods_item_data in self.alert_methods:
                alert_methods_item = alert_methods_item_data.to_dict()

                _temp_alert_methods.append(alert_methods_item)
            alert_methods = (None, json.dumps(_temp_alert_methods).encode(), "application/json")

        other_metadata: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.other_metadata, Unset):
            other_metadata = (
                (None, json.dumps(self.other_metadata.to_dict()).encode(), "application/json")
                if self.other_metadata
                else None
            )

        was_auto_created = (
            self.was_auto_created
            if isinstance(self.was_auto_created, Unset)
            else (None, str(self.was_auto_created).encode(), "text/plain")
        )
        passive = self.passive if isinstance(self.passive, Unset) else (None, str(self.passive).encode(), "text/plain")
        enabled = self.enabled if isinstance(self.enabled, Unset) else (None, str(self.enabled).encode(), "text/plain")

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
                "is_service": is_service,
                "execution_method_capability": execution_method_capability,
                "latest_task_execution": latest_task_execution,
                "current_service_info": current_service_info,
                "created_by_user": created_by_user,
                "created_by_group": created_by_group,
                "created_at": created_at,
                "updated_at": updated_at,
                "infrastructure_website_url": infrastructure_website_url,
                "logs_url": logs_url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if max_manual_start_delay_before_alert_seconds is not UNSET:
            field_dict["max_manual_start_delay_before_alert_seconds"] = max_manual_start_delay_before_alert_seconds
        if max_manual_start_delay_before_abandonment_seconds is not UNSET:
            field_dict[
                "max_manual_start_delay_before_abandonment_seconds"
            ] = max_manual_start_delay_before_abandonment_seconds
        if heartbeat_interval_seconds is not UNSET:
            field_dict["heartbeat_interval_seconds"] = heartbeat_interval_seconds
        if max_heartbeat_lateness_before_alert_seconds is not UNSET:
            field_dict["max_heartbeat_lateness_before_alert_seconds"] = max_heartbeat_lateness_before_alert_seconds
        if max_heartbeat_lateness_before_abandonment_seconds is not UNSET:
            field_dict[
                "max_heartbeat_lateness_before_abandonment_seconds"
            ] = max_heartbeat_lateness_before_abandonment_seconds
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if scheduled_instance_count is not UNSET:
            field_dict["scheduled_instance_count"] = scheduled_instance_count
        if service_instance_count is not UNSET:
            field_dict["service_instance_count"] = service_instance_count
        if min_service_instance_count is not UNSET:
            field_dict["min_service_instance_count"] = min_service_instance_count
        if max_concurrency is not UNSET:
            field_dict["max_concurrency"] = max_concurrency
        if max_age_seconds is not UNSET:
            field_dict["max_age_seconds"] = max_age_seconds
        if default_max_retries is not UNSET:
            field_dict["default_max_retries"] = default_max_retries
        if project_url is not UNSET:
            field_dict["project_url"] = project_url
        if log_query is not UNSET:
            field_dict["log_query"] = log_query
        if links is not UNSET:
            field_dict["links"] = links
        if run_environment is not UNSET:
            field_dict["run_environment"] = run_environment
        if alert_methods is not UNSET:
            field_dict["alert_methods"] = alert_methods
        if other_metadata is not UNSET:
            field_dict["other_metadata"] = other_metadata
        if was_auto_created is not UNSET:
            field_dict["was_auto_created"] = was_auto_created
        if passive is not UNSET:
            field_dict["passive"] = passive
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = d.pop("uuid")

        name = d.pop("name")

        dashboard_url = d.pop("dashboard_url")

        is_service = d.pop("is_service")

        def _parse_execution_method_capability(
            data: object,
        ) -> Union[AwsEcsExecutionMethodCapability, UnknownExecutionMethodCapability]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_execution_method_capability_type_0 = AwsEcsExecutionMethodCapability.from_dict(data)

                return componentsschemas_execution_method_capability_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_execution_method_capability_type_1 = UnknownExecutionMethodCapability.from_dict(data)

            return componentsschemas_execution_method_capability_type_1

        execution_method_capability = _parse_execution_method_capability(d.pop("execution_method_capability"))

        latest_task_execution = TaskExecution.from_dict(d.pop("latest_task_execution"))

        current_service_info = CurrentServiceInfo.from_dict(d.pop("current_service_info"))

        created_by_user = d.pop("created_by_user")

        created_by_group = Group.from_dict(d.pop("created_by_group"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        infrastructure_website_url = d.pop("infrastructure_website_url")

        max_manual_start_delay_before_alert_seconds = d.pop("max_manual_start_delay_before_alert_seconds", UNSET)

        max_manual_start_delay_before_abandonment_seconds = d.pop(
            "max_manual_start_delay_before_abandonment_seconds", UNSET
        )

        heartbeat_interval_seconds = d.pop("heartbeat_interval_seconds", UNSET)

        max_heartbeat_lateness_before_alert_seconds = d.pop("max_heartbeat_lateness_before_alert_seconds", UNSET)

        max_heartbeat_lateness_before_abandonment_seconds = d.pop(
            "max_heartbeat_lateness_before_abandonment_seconds", UNSET
        )

        schedule = d.pop("schedule", UNSET)

        scheduled_instance_count = d.pop("scheduled_instance_count", UNSET)

        service_instance_count = d.pop("service_instance_count", UNSET)

        min_service_instance_count = d.pop("min_service_instance_count", UNSET)

        max_concurrency = d.pop("max_concurrency", UNSET)

        max_age_seconds = d.pop("max_age_seconds", UNSET)

        default_max_retries = d.pop("default_max_retries", UNSET)

        project_url = d.pop("project_url", UNSET)

        log_query = d.pop("log_query", UNSET)

        logs_url = d.pop("logs_url")

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        _run_environment = d.pop("run_environment", UNSET)
        run_environment: Union[Unset, None, NameAndUuid]
        if _run_environment is None:
            run_environment = None
        elif isinstance(_run_environment, Unset):
            run_environment = UNSET
        else:
            run_environment = NameAndUuid.from_dict(_run_environment)

        alert_methods = []
        _alert_methods = d.pop("alert_methods", UNSET)
        for alert_methods_item_data in _alert_methods or []:
            alert_methods_item = NameAndUuid.from_dict(alert_methods_item_data)

            alert_methods.append(alert_methods_item)

        _other_metadata = d.pop("other_metadata", UNSET)
        other_metadata: Union[Unset, None, TaskOtherMetadata]
        if _other_metadata is None:
            other_metadata = None
        elif isinstance(_other_metadata, Unset):
            other_metadata = UNSET
        else:
            other_metadata = TaskOtherMetadata.from_dict(_other_metadata)

        was_auto_created = d.pop("was_auto_created", UNSET)

        passive = d.pop("passive", UNSET)

        enabled = d.pop("enabled", UNSET)

        task = cls(
            url=url,
            uuid=uuid,
            name=name,
            dashboard_url=dashboard_url,
            is_service=is_service,
            execution_method_capability=execution_method_capability,
            latest_task_execution=latest_task_execution,
            current_service_info=current_service_info,
            created_by_user=created_by_user,
            created_by_group=created_by_group,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            infrastructure_website_url=infrastructure_website_url,
            max_manual_start_delay_before_alert_seconds=max_manual_start_delay_before_alert_seconds,
            max_manual_start_delay_before_abandonment_seconds=max_manual_start_delay_before_abandonment_seconds,
            heartbeat_interval_seconds=heartbeat_interval_seconds,
            max_heartbeat_lateness_before_alert_seconds=max_heartbeat_lateness_before_alert_seconds,
            max_heartbeat_lateness_before_abandonment_seconds=max_heartbeat_lateness_before_abandonment_seconds,
            schedule=schedule,
            scheduled_instance_count=scheduled_instance_count,
            service_instance_count=service_instance_count,
            min_service_instance_count=min_service_instance_count,
            max_concurrency=max_concurrency,
            max_age_seconds=max_age_seconds,
            default_max_retries=default_max_retries,
            project_url=project_url,
            log_query=log_query,
            logs_url=logs_url,
            links=links,
            run_environment=run_environment,
            alert_methods=alert_methods,
            other_metadata=other_metadata,
            was_auto_created=was_auto_created,
            passive=passive,
            enabled=enabled,
        )

        task.additional_properties = d
        return task

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
