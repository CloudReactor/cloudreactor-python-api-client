import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.name_and_uuid import NameAndUuid

T = TypeVar("T", bound="WorkflowTransitionEvaluation")


@attr.s(auto_attribs=True)
class WorkflowTransitionEvaluation:
    """A WorkflowTransitionEvaluation is a saved evaluation of the conditions
    in a WorkflowTransition during a WorkflowExecution.

        Attributes:
            uuid (str):
            result (bool):
            workflow_transition (NameAndUuid): Identifies an entity in three ways: 1. UUID; 2. Name; and 3. URL.
                When used to indentify an entity in a request method body, only one of
                uuid and name needs to be specified. If both are present, they must
                refer to the same entity or else the response will be a 400 error.
            workflow_execution (NameAndUuid): Identifies an entity in three ways: 1. UUID; 2. Name; and 3. URL.
                When used to indentify an entity in a request method body, only one of
                uuid and name needs to be specified. If both are present, they must
                refer to the same entity or else the response will be a 400 error.
            evaluated_at (datetime.datetime):
            from_workflow_task_instance_execution (Optional[str]):
    """

    uuid: str
    result: bool
    workflow_transition: NameAndUuid
    workflow_execution: NameAndUuid
    evaluated_at: datetime.datetime
    from_workflow_task_instance_execution: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        result = self.result
        workflow_transition = self.workflow_transition.to_dict()

        workflow_execution = self.workflow_execution.to_dict()

        evaluated_at = self.evaluated_at.isoformat()

        from_workflow_task_instance_execution = self.from_workflow_task_instance_execution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "result": result,
                "workflow_transition": workflow_transition,
                "workflow_execution": workflow_execution,
                "evaluated_at": evaluated_at,
                "from_workflow_task_instance_execution": from_workflow_task_instance_execution,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        result = d.pop("result")

        workflow_transition = NameAndUuid.from_dict(d.pop("workflow_transition"))

        workflow_execution = NameAndUuid.from_dict(d.pop("workflow_execution"))

        evaluated_at = isoparse(d.pop("evaluated_at"))

        from_workflow_task_instance_execution = d.pop("from_workflow_task_instance_execution")

        workflow_transition_evaluation = cls(
            uuid=uuid,
            result=result,
            workflow_transition=workflow_transition,
            workflow_execution=workflow_execution,
            evaluated_at=evaluated_at,
            from_workflow_task_instance_execution=from_workflow_task_instance_execution,
        )

        workflow_transition_evaluation.additional_properties = d
        return workflow_transition_evaluation

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
