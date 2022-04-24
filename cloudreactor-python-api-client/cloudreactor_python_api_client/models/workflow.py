import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.group import Group
from ..models.name_and_uuid import NameAndUuid
from ..models.workflow_execution_summary import WorkflowExecutionSummary
from ..models.workflow_task_instance import WorkflowTaskInstance
from ..models.workflow_transition import WorkflowTransition
from ..types import UNSET, Unset

T = TypeVar("T", bound="Workflow")


@attr.s(auto_attribs=True)
class Workflow:
    """Workflows are Tasks arranged in a directed graph. Configured Tasks
    are held by WorkflowTaskInstances, and WorkflowTransitions connect
    WorkflowTaskInstances together.

        Attributes:
            url (str):
            uuid (str):
            name (str):
            dashboard_url (str):
            created_by_user (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
            created_by_group (Group):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            workflow_task_instances (List[WorkflowTaskInstance]):
            workflow_transitions (List[WorkflowTransition]):
            description (Union[Unset, str]):
            schedule (Union[Unset, str]):
            max_concurrency (Union[Unset, None, int]):
            max_age_seconds (Union[Unset, None, int]):
            default_max_retries (Union[Unset, int]):
            latest_workflow_execution (Union[Unset, WorkflowExecutionSummary]): A WorkflowExecution holds data on a specific
                execution (run) of a Workflow.
            run_environment (Union[Unset, None, NameAndUuid]): Identifies an entity in three ways: 1. UUID; 2. Name; and 3.
                URL.
                When used to indentify an entity in a request method body, only one of
                uuid and name needs to be specified. If both are present, they must
                refer to the same entity or else the response will be a 400 error.
            enabled (Union[Unset, bool]):
            alert_methods (Union[Unset, List[NameAndUuid]]):
    """

    url: str
    uuid: str
    name: str
    dashboard_url: str
    created_by_user: str
    created_by_group: Group
    created_at: datetime.datetime
    updated_at: datetime.datetime
    workflow_task_instances: List[WorkflowTaskInstance]
    workflow_transitions: List[WorkflowTransition]
    description: Union[Unset, str] = UNSET
    schedule: Union[Unset, str] = UNSET
    max_concurrency: Union[Unset, None, int] = UNSET
    max_age_seconds: Union[Unset, None, int] = UNSET
    default_max_retries: Union[Unset, int] = UNSET
    latest_workflow_execution: Union[Unset, WorkflowExecutionSummary] = UNSET
    run_environment: Union[Unset, None, NameAndUuid] = UNSET
    enabled: Union[Unset, bool] = UNSET
    alert_methods: Union[Unset, List[NameAndUuid]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        uuid = self.uuid
        name = self.name
        dashboard_url = self.dashboard_url
        created_by_user = self.created_by_user
        created_by_group = self.created_by_group.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        workflow_task_instances = []
        for workflow_task_instances_item_data in self.workflow_task_instances:
            workflow_task_instances_item = workflow_task_instances_item_data.to_dict()

            workflow_task_instances.append(workflow_task_instances_item)

        workflow_transitions = []
        for workflow_transitions_item_data in self.workflow_transitions:
            workflow_transitions_item = workflow_transitions_item_data.to_dict()

            workflow_transitions.append(workflow_transitions_item)

        description = self.description
        schedule = self.schedule
        max_concurrency = self.max_concurrency
        max_age_seconds = self.max_age_seconds
        default_max_retries = self.default_max_retries
        latest_workflow_execution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.latest_workflow_execution, Unset):
            latest_workflow_execution = self.latest_workflow_execution.to_dict()

        run_environment: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.run_environment, Unset):
            run_environment = self.run_environment.to_dict() if self.run_environment else None

        enabled = self.enabled
        alert_methods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alert_methods, Unset):
            alert_methods = []
            for alert_methods_item_data in self.alert_methods:
                alert_methods_item = alert_methods_item_data.to_dict()

                alert_methods.append(alert_methods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "name": name,
                "dashboard_url": dashboard_url,
                "created_by_user": created_by_user,
                "created_by_group": created_by_group,
                "created_at": created_at,
                "updated_at": updated_at,
                "workflow_task_instances": workflow_task_instances,
                "workflow_transitions": workflow_transitions,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if max_concurrency is not UNSET:
            field_dict["max_concurrency"] = max_concurrency
        if max_age_seconds is not UNSET:
            field_dict["max_age_seconds"] = max_age_seconds
        if default_max_retries is not UNSET:
            field_dict["default_max_retries"] = default_max_retries
        if latest_workflow_execution is not UNSET:
            field_dict["latest_workflow_execution"] = latest_workflow_execution
        if run_environment is not UNSET:
            field_dict["run_environment"] = run_environment
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if alert_methods is not UNSET:
            field_dict["alert_methods"] = alert_methods

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
        created_by_user = (
            self.created_by_user
            if isinstance(self.created_by_user, Unset)
            else (None, str(self.created_by_user).encode(), "text/plain")
        )
        created_by_group = (None, json.dumps(self.created_by_group.to_dict()).encode(), "application/json")

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        _temp_workflow_task_instances = []
        for workflow_task_instances_item_data in self.workflow_task_instances:
            workflow_task_instances_item = workflow_task_instances_item_data.to_dict()

            _temp_workflow_task_instances.append(workflow_task_instances_item)
        workflow_task_instances = (None, json.dumps(_temp_workflow_task_instances).encode(), "application/json")

        _temp_workflow_transitions = []
        for workflow_transitions_item_data in self.workflow_transitions:
            workflow_transitions_item = workflow_transitions_item_data.to_dict()

            _temp_workflow_transitions.append(workflow_transitions_item)
        workflow_transitions = (None, json.dumps(_temp_workflow_transitions).encode(), "application/json")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        schedule = (
            self.schedule if isinstance(self.schedule, Unset) else (None, str(self.schedule).encode(), "text/plain")
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
        latest_workflow_execution: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.latest_workflow_execution, Unset):
            latest_workflow_execution = (
                None,
                json.dumps(self.latest_workflow_execution.to_dict()).encode(),
                "application/json",
            )

        run_environment: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.run_environment, Unset):
            run_environment = (
                (None, json.dumps(self.run_environment.to_dict()).encode(), "application/json")
                if self.run_environment
                else None
            )

        enabled = self.enabled if isinstance(self.enabled, Unset) else (None, str(self.enabled).encode(), "text/plain")
        alert_methods: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.alert_methods, Unset):
            _temp_alert_methods = []
            for alert_methods_item_data in self.alert_methods:
                alert_methods_item = alert_methods_item_data.to_dict()

                _temp_alert_methods.append(alert_methods_item)
            alert_methods = (None, json.dumps(_temp_alert_methods).encode(), "application/json")

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
                "created_by_user": created_by_user,
                "created_by_group": created_by_group,
                "created_at": created_at,
                "updated_at": updated_at,
                "workflow_task_instances": workflow_task_instances,
                "workflow_transitions": workflow_transitions,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if max_concurrency is not UNSET:
            field_dict["max_concurrency"] = max_concurrency
        if max_age_seconds is not UNSET:
            field_dict["max_age_seconds"] = max_age_seconds
        if default_max_retries is not UNSET:
            field_dict["default_max_retries"] = default_max_retries
        if latest_workflow_execution is not UNSET:
            field_dict["latest_workflow_execution"] = latest_workflow_execution
        if run_environment is not UNSET:
            field_dict["run_environment"] = run_environment
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if alert_methods is not UNSET:
            field_dict["alert_methods"] = alert_methods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = d.pop("uuid")

        name = d.pop("name")

        dashboard_url = d.pop("dashboard_url")

        created_by_user = d.pop("created_by_user")

        created_by_group = Group.from_dict(d.pop("created_by_group"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        workflow_task_instances = []
        _workflow_task_instances = d.pop("workflow_task_instances")
        for workflow_task_instances_item_data in _workflow_task_instances:
            workflow_task_instances_item = WorkflowTaskInstance.from_dict(workflow_task_instances_item_data)

            workflow_task_instances.append(workflow_task_instances_item)

        workflow_transitions = []
        _workflow_transitions = d.pop("workflow_transitions")
        for workflow_transitions_item_data in _workflow_transitions:
            workflow_transitions_item = WorkflowTransition.from_dict(workflow_transitions_item_data)

            workflow_transitions.append(workflow_transitions_item)

        description = d.pop("description", UNSET)

        schedule = d.pop("schedule", UNSET)

        max_concurrency = d.pop("max_concurrency", UNSET)

        max_age_seconds = d.pop("max_age_seconds", UNSET)

        default_max_retries = d.pop("default_max_retries", UNSET)

        _latest_workflow_execution = d.pop("latest_workflow_execution", UNSET)
        latest_workflow_execution: Union[Unset, WorkflowExecutionSummary]
        if isinstance(_latest_workflow_execution, Unset):
            latest_workflow_execution = UNSET
        else:
            latest_workflow_execution = WorkflowExecutionSummary.from_dict(_latest_workflow_execution)

        _run_environment = d.pop("run_environment", UNSET)
        run_environment: Union[Unset, None, NameAndUuid]
        if _run_environment is None:
            run_environment = None
        elif isinstance(_run_environment, Unset):
            run_environment = UNSET
        else:
            run_environment = NameAndUuid.from_dict(_run_environment)

        enabled = d.pop("enabled", UNSET)

        alert_methods = []
        _alert_methods = d.pop("alert_methods", UNSET)
        for alert_methods_item_data in _alert_methods or []:
            alert_methods_item = NameAndUuid.from_dict(alert_methods_item_data)

            alert_methods.append(alert_methods_item)

        workflow = cls(
            url=url,
            uuid=uuid,
            name=name,
            dashboard_url=dashboard_url,
            created_by_user=created_by_user,
            created_by_group=created_by_group,
            created_at=created_at,
            updated_at=updated_at,
            workflow_task_instances=workflow_task_instances,
            workflow_transitions=workflow_transitions,
            description=description,
            schedule=schedule,
            max_concurrency=max_concurrency,
            max_age_seconds=max_age_seconds,
            default_max_retries=default_max_retries,
            latest_workflow_execution=latest_workflow_execution,
            run_environment=run_environment,
            enabled=enabled,
            alert_methods=alert_methods,
        )

        workflow.additional_properties = d
        return workflow

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
