import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.group import Group
from ..models.name_and_uuid import NameAndUuid
from ..models.workflow_execution_summary import WorkflowExecutionSummary
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowSummary")


@attr.s(auto_attribs=True)
class WorkflowSummary:
    """Selected properties of Workflows.

    Attributes:
        url (str):
        uuid (str):
        name (str):
        dashboard_url (str):
        created_by_user (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        created_by_group (Group):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
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
    """

    url: str
    uuid: str
    name: str
    dashboard_url: str
    created_by_user: str
    created_by_group: Group
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Union[Unset, str] = UNSET
    schedule: Union[Unset, str] = UNSET
    max_concurrency: Union[Unset, None, int] = UNSET
    max_age_seconds: Union[Unset, None, int] = UNSET
    default_max_retries: Union[Unset, int] = UNSET
    latest_workflow_execution: Union[Unset, WorkflowExecutionSummary] = UNSET
    run_environment: Union[Unset, None, NameAndUuid] = UNSET
    enabled: Union[Unset, bool] = UNSET
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

        workflow_summary = cls(
            url=url,
            uuid=uuid,
            name=name,
            dashboard_url=dashboard_url,
            created_by_user=created_by_user,
            created_by_group=created_by_group,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            schedule=schedule,
            max_concurrency=max_concurrency,
            max_age_seconds=max_age_seconds,
            default_max_retries=default_max_retries,
            latest_workflow_execution=latest_workflow_execution,
            run_environment=run_environment,
            enabled=enabled,
        )

        workflow_summary.additional_properties = d
        return workflow_summary

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
