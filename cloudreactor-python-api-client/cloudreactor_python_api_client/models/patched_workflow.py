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

T = TypeVar("T", bound="PatchedWorkflow")


@attr.s(auto_attribs=True)
class PatchedWorkflow:
    """Workflows are Tasks arranged in a directed graph. Configured Tasks
    are held by WorkflowTaskInstances, and WorkflowTransitions connect
    WorkflowTaskInstances together.

        Attributes:
            url (Union[Unset, str]):
            uuid (Union[Unset, str]):
            name (Union[Unset, str]):
            description (Union[Unset, str]):
            dashboard_url (Union[Unset, str]):
            schedule (Union[Unset, str]):
            max_concurrency (Union[Unset, None, int]):
            max_age_seconds (Union[Unset, None, int]):
            default_max_retries (Union[Unset, int]):
            latest_workflow_execution (Union[Unset, WorkflowExecutionSummary]): A WorkflowExecution holds data on a specific
                execution (run) of a Workflow.
            created_by_user (Union[Unset, str]): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
            created_by_group (Union[Unset, Group]):
            run_environment (Union[Unset, None, NameAndUuid]): Identifies an entity in three ways: 1. UUID; 2. Name; and 3.
                URL.
                When used to indentify an entity in a request method body, only one of
                uuid and name needs to be specified. If both are present, they must
                refer to the same entity or else the response will be a 400 error.
            enabled (Union[Unset, bool]):
            created_at (Union[Unset, datetime.datetime]):
            updated_at (Union[Unset, datetime.datetime]):
            alert_methods (Union[Unset, List[NameAndUuid]]):
            workflow_task_instances (Union[Unset, List[WorkflowTaskInstance]]):
            workflow_transitions (Union[Unset, List[WorkflowTransition]]):
    """

    url: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    dashboard_url: Union[Unset, str] = UNSET
    schedule: Union[Unset, str] = UNSET
    max_concurrency: Union[Unset, None, int] = UNSET
    max_age_seconds: Union[Unset, None, int] = UNSET
    default_max_retries: Union[Unset, int] = UNSET
    latest_workflow_execution: Union[Unset, WorkflowExecutionSummary] = UNSET
    created_by_user: Union[Unset, str] = UNSET
    created_by_group: Union[Unset, Group] = UNSET
    run_environment: Union[Unset, None, NameAndUuid] = UNSET
    enabled: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    alert_methods: Union[Unset, List[NameAndUuid]] = UNSET
    workflow_task_instances: Union[Unset, List[WorkflowTaskInstance]] = UNSET
    workflow_transitions: Union[Unset, List[WorkflowTransition]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        uuid = self.uuid
        name = self.name
        description = self.description
        dashboard_url = self.dashboard_url
        schedule = self.schedule
        max_concurrency = self.max_concurrency
        max_age_seconds = self.max_age_seconds
        default_max_retries = self.default_max_retries
        latest_workflow_execution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.latest_workflow_execution, Unset):
            latest_workflow_execution = self.latest_workflow_execution.to_dict()

        created_by_user = self.created_by_user
        created_by_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by_group, Unset):
            created_by_group = self.created_by_group.to_dict()

        run_environment: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.run_environment, Unset):
            run_environment = self.run_environment.to_dict() if self.run_environment else None

        enabled = self.enabled
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        alert_methods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alert_methods, Unset):
            alert_methods = []
            for alert_methods_item_data in self.alert_methods:
                alert_methods_item = alert_methods_item_data.to_dict()

                alert_methods.append(alert_methods_item)

        workflow_task_instances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workflow_task_instances, Unset):
            workflow_task_instances = []
            for workflow_task_instances_item_data in self.workflow_task_instances:
                workflow_task_instances_item = workflow_task_instances_item_data.to_dict()

                workflow_task_instances.append(workflow_task_instances_item)

        workflow_transitions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workflow_transitions, Unset):
            workflow_transitions = []
            for workflow_transitions_item_data in self.workflow_transitions:
                workflow_transitions_item = workflow_transitions_item_data.to_dict()

                workflow_transitions.append(workflow_transitions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if dashboard_url is not UNSET:
            field_dict["dashboard_url"] = dashboard_url
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
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if created_by_group is not UNSET:
            field_dict["created_by_group"] = created_by_group
        if run_environment is not UNSET:
            field_dict["run_environment"] = run_environment
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if alert_methods is not UNSET:
            field_dict["alert_methods"] = alert_methods
        if workflow_task_instances is not UNSET:
            field_dict["workflow_task_instances"] = workflow_task_instances
        if workflow_transitions is not UNSET:
            field_dict["workflow_transitions"] = workflow_transitions

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        uuid = self.uuid if isinstance(self.uuid, Unset) else (None, str(self.uuid).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        dashboard_url = (
            self.dashboard_url
            if isinstance(self.dashboard_url, Unset)
            else (None, str(self.dashboard_url).encode(), "text/plain")
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

        created_by_user = (
            self.created_by_user
            if isinstance(self.created_by_user, Unset)
            else (None, str(self.created_by_user).encode(), "text/plain")
        )
        created_by_group: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.created_by_group, Unset):
            created_by_group = (None, json.dumps(self.created_by_group.to_dict()).encode(), "application/json")

        run_environment: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.run_environment, Unset):
            run_environment = (
                (None, json.dumps(self.run_environment.to_dict()).encode(), "application/json")
                if self.run_environment
                else None
            )

        enabled = self.enabled if isinstance(self.enabled, Unset) else (None, str(self.enabled).encode(), "text/plain")
        created_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Union[Unset, bytes] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        alert_methods: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.alert_methods, Unset):
            _temp_alert_methods = []
            for alert_methods_item_data in self.alert_methods:
                alert_methods_item = alert_methods_item_data.to_dict()

                _temp_alert_methods.append(alert_methods_item)
            alert_methods = (None, json.dumps(_temp_alert_methods).encode(), "application/json")

        workflow_task_instances: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.workflow_task_instances, Unset):
            _temp_workflow_task_instances = []
            for workflow_task_instances_item_data in self.workflow_task_instances:
                workflow_task_instances_item = workflow_task_instances_item_data.to_dict()

                _temp_workflow_task_instances.append(workflow_task_instances_item)
            workflow_task_instances = (None, json.dumps(_temp_workflow_task_instances).encode(), "application/json")

        workflow_transitions: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.workflow_transitions, Unset):
            _temp_workflow_transitions = []
            for workflow_transitions_item_data in self.workflow_transitions:
                workflow_transitions_item = workflow_transitions_item_data.to_dict()

                _temp_workflow_transitions.append(workflow_transitions_item)
            workflow_transitions = (None, json.dumps(_temp_workflow_transitions).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if dashboard_url is not UNSET:
            field_dict["dashboard_url"] = dashboard_url
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
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if created_by_group is not UNSET:
            field_dict["created_by_group"] = created_by_group
        if run_environment is not UNSET:
            field_dict["run_environment"] = run_environment
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if alert_methods is not UNSET:
            field_dict["alert_methods"] = alert_methods
        if workflow_task_instances is not UNSET:
            field_dict["workflow_task_instances"] = workflow_task_instances
        if workflow_transitions is not UNSET:
            field_dict["workflow_transitions"] = workflow_transitions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        dashboard_url = d.pop("dashboard_url", UNSET)

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

        created_by_user = d.pop("created_by_user", UNSET)

        _created_by_group = d.pop("created_by_group", UNSET)
        created_by_group: Union[Unset, Group]
        if isinstance(_created_by_group, Unset):
            created_by_group = UNSET
        else:
            created_by_group = Group.from_dict(_created_by_group)

        _run_environment = d.pop("run_environment", UNSET)
        run_environment: Union[Unset, None, NameAndUuid]
        if _run_environment is None:
            run_environment = None
        elif isinstance(_run_environment, Unset):
            run_environment = UNSET
        else:
            run_environment = NameAndUuid.from_dict(_run_environment)

        enabled = d.pop("enabled", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        alert_methods = []
        _alert_methods = d.pop("alert_methods", UNSET)
        for alert_methods_item_data in _alert_methods or []:
            alert_methods_item = NameAndUuid.from_dict(alert_methods_item_data)

            alert_methods.append(alert_methods_item)

        workflow_task_instances = []
        _workflow_task_instances = d.pop("workflow_task_instances", UNSET)
        for workflow_task_instances_item_data in _workflow_task_instances or []:
            workflow_task_instances_item = WorkflowTaskInstance.from_dict(workflow_task_instances_item_data)

            workflow_task_instances.append(workflow_task_instances_item)

        workflow_transitions = []
        _workflow_transitions = d.pop("workflow_transitions", UNSET)
        for workflow_transitions_item_data in _workflow_transitions or []:
            workflow_transitions_item = WorkflowTransition.from_dict(workflow_transitions_item_data)

            workflow_transitions.append(workflow_transitions_item)

        patched_workflow = cls(
            url=url,
            uuid=uuid,
            name=name,
            description=description,
            dashboard_url=dashboard_url,
            schedule=schedule,
            max_concurrency=max_concurrency,
            max_age_seconds=max_age_seconds,
            default_max_retries=default_max_retries,
            latest_workflow_execution=latest_workflow_execution,
            created_by_user=created_by_user,
            created_by_group=created_by_group,
            run_environment=run_environment,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            alert_methods=alert_methods,
            workflow_task_instances=workflow_task_instances,
            workflow_transitions=workflow_transitions,
        )

        patched_workflow.additional_properties = d
        return patched_workflow

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
