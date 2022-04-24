import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.name_and_uuid import NameAndUuid

T = TypeVar("T", bound="WorkflowTaskInstanceExecutionBase")


@attr.s(auto_attribs=True)
class WorkflowTaskInstanceExecutionBase:
    """WorkflowTaskInstanceExecutions hold the execution information
    for a WorkflowTaskInstance (which holds a Task) for a specific
    WorkflowExection (run of a Workflow).

        Attributes:
            uuid (str):
            workflow_execution (NameAndUuid): Identifies an entity in three ways: 1. UUID; 2. Name; and 3. URL.
                When used to indentify an entity in a request method body, only one of
                uuid and name needs to be specified. If both are present, they must
                refer to the same entity or else the response will be a 400 error.
            workflow_task_instance (NameAndUuid): Identifies an entity in three ways: 1. UUID; 2. Name; and 3. URL.
                When used to indentify an entity in a request method body, only one of
                uuid and name needs to be specified. If both are present, they must
                refer to the same entity or else the response will be a 400 error.
            is_latest (bool):
            created_at (datetime.datetime):
    """

    uuid: str
    workflow_execution: NameAndUuid
    workflow_task_instance: NameAndUuid
    is_latest: bool
    created_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        workflow_execution = self.workflow_execution.to_dict()

        workflow_task_instance = self.workflow_task_instance.to_dict()

        is_latest = self.is_latest
        created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "workflow_execution": workflow_execution,
                "workflow_task_instance": workflow_task_instance,
                "is_latest": is_latest,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        workflow_execution = NameAndUuid.from_dict(d.pop("workflow_execution"))

        workflow_task_instance = NameAndUuid.from_dict(d.pop("workflow_task_instance"))

        is_latest = d.pop("is_latest")

        created_at = isoparse(d.pop("created_at"))

        workflow_task_instance_execution_base = cls(
            uuid=uuid,
            workflow_execution=workflow_execution,
            workflow_task_instance=workflow_task_instance,
            is_latest=is_latest,
            created_at=created_at,
        )

        workflow_task_instance_execution_base.additional_properties = d
        return workflow_task_instance_execution_base

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
