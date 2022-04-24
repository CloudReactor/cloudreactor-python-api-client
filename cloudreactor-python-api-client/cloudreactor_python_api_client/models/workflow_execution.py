import datetime
import json
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.name_and_uuid import NameAndUuid
from ..models.workflow_execution_status import WorkflowExecutionStatus
from ..models.workflow_execution_workflow_snapshot import WorkflowExecutionWorkflowSnapshot
from ..models.workflow_task_instance_execution import WorkflowTaskInstanceExecution
from ..models.workflow_transition_evaluation import WorkflowTransitionEvaluation
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowExecution")


@attr.s(auto_attribs=True)
class WorkflowExecution:
    """
    Attributes:
        url (str):
        uuid (str):
        dashboard_url (str):
        workflow (NameAndUuid): Identifies an entity in three ways: 1. UUID; 2. Name; and 3. URL.
            When used to indentify an entity in a request method body, only one of
            uuid and name needs to be specified. If both are present, they must
            refer to the same entity or else the response will be a 400 error.
        status (WorkflowExecutionStatus):
        started_at (datetime.datetime):
        started_by (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        marked_done_by (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        killed_by (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        workflow_snapshot (WorkflowExecutionWorkflowSnapshot):
        workflow_task_instance_executions (List[WorkflowTaskInstanceExecution]):
        workflow_transition_evaluations (List[WorkflowTransitionEvaluation]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        run_reason (Union[Unset, int]):
        finished_at (Union[Unset, None, datetime.datetime]):
        last_heartbeat_at (Union[Unset, None, datetime.datetime]):
        stop_reason (Union[Unset, None, int]):
        marked_done_at (Union[Unset, None, datetime.datetime]):
        kill_started_at (Union[Unset, None, datetime.datetime]):
        kill_finished_at (Union[Unset, None, datetime.datetime]):
        kill_error_code (Union[Unset, None, int]):
        failed_attempts (Union[Unset, int]):
        timed_out_attempts (Union[Unset, int]):
    """

    url: str
    uuid: str
    dashboard_url: str
    workflow: NameAndUuid
    status: WorkflowExecutionStatus
    started_at: datetime.datetime
    started_by: str
    marked_done_by: str
    killed_by: str
    workflow_snapshot: WorkflowExecutionWorkflowSnapshot
    workflow_task_instance_executions: List[WorkflowTaskInstanceExecution]
    workflow_transition_evaluations: List[WorkflowTransitionEvaluation]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    run_reason: Union[Unset, int] = UNSET
    finished_at: Union[Unset, None, datetime.datetime] = UNSET
    last_heartbeat_at: Union[Unset, None, datetime.datetime] = UNSET
    stop_reason: Union[Unset, None, int] = UNSET
    marked_done_at: Union[Unset, None, datetime.datetime] = UNSET
    kill_started_at: Union[Unset, None, datetime.datetime] = UNSET
    kill_finished_at: Union[Unset, None, datetime.datetime] = UNSET
    kill_error_code: Union[Unset, None, int] = UNSET
    failed_attempts: Union[Unset, int] = UNSET
    timed_out_attempts: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        uuid = self.uuid
        dashboard_url = self.dashboard_url
        workflow = self.workflow.to_dict()

        status = self.status.value

        started_at = self.started_at.isoformat()

        started_by = self.started_by
        marked_done_by = self.marked_done_by
        killed_by = self.killed_by
        workflow_snapshot = self.workflow_snapshot.to_dict()

        workflow_task_instance_executions = []
        for workflow_task_instance_executions_item_data in self.workflow_task_instance_executions:
            workflow_task_instance_executions_item = workflow_task_instance_executions_item_data.to_dict()

            workflow_task_instance_executions.append(workflow_task_instance_executions_item)

        workflow_transition_evaluations = []
        for workflow_transition_evaluations_item_data in self.workflow_transition_evaluations:
            workflow_transition_evaluations_item = workflow_transition_evaluations_item_data.to_dict()

            workflow_transition_evaluations.append(workflow_transition_evaluations_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        run_reason = self.run_reason
        finished_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat() if self.finished_at else None

        last_heartbeat_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_heartbeat_at, Unset):
            last_heartbeat_at = self.last_heartbeat_at.isoformat() if self.last_heartbeat_at else None

        stop_reason = self.stop_reason
        marked_done_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.marked_done_at, Unset):
            marked_done_at = self.marked_done_at.isoformat() if self.marked_done_at else None

        kill_started_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.kill_started_at, Unset):
            kill_started_at = self.kill_started_at.isoformat() if self.kill_started_at else None

        kill_finished_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.kill_finished_at, Unset):
            kill_finished_at = self.kill_finished_at.isoformat() if self.kill_finished_at else None

        kill_error_code = self.kill_error_code
        failed_attempts = self.failed_attempts
        timed_out_attempts = self.timed_out_attempts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "dashboard_url": dashboard_url,
                "workflow": workflow,
                "status": status,
                "started_at": started_at,
                "started_by": started_by,
                "marked_done_by": marked_done_by,
                "killed_by": killed_by,
                "workflow_snapshot": workflow_snapshot,
                "workflow_task_instance_executions": workflow_task_instance_executions,
                "workflow_transition_evaluations": workflow_transition_evaluations,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if run_reason is not UNSET:
            field_dict["run_reason"] = run_reason
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if last_heartbeat_at is not UNSET:
            field_dict["last_heartbeat_at"] = last_heartbeat_at
        if stop_reason is not UNSET:
            field_dict["stop_reason"] = stop_reason
        if marked_done_at is not UNSET:
            field_dict["marked_done_at"] = marked_done_at
        if kill_started_at is not UNSET:
            field_dict["kill_started_at"] = kill_started_at
        if kill_finished_at is not UNSET:
            field_dict["kill_finished_at"] = kill_finished_at
        if kill_error_code is not UNSET:
            field_dict["kill_error_code"] = kill_error_code
        if failed_attempts is not UNSET:
            field_dict["failed_attempts"] = failed_attempts
        if timed_out_attempts is not UNSET:
            field_dict["timed_out_attempts"] = timed_out_attempts

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        uuid = self.uuid if isinstance(self.uuid, Unset) else (None, str(self.uuid).encode(), "text/plain")
        dashboard_url = (
            self.dashboard_url
            if isinstance(self.dashboard_url, Unset)
            else (None, str(self.dashboard_url).encode(), "text/plain")
        )
        workflow = (None, json.dumps(self.workflow.to_dict()).encode(), "application/json")

        status = (None, str(self.status.value).encode(), "text/plain")

        started_at = self.started_at.isoformat().encode()

        started_by = (
            self.started_by
            if isinstance(self.started_by, Unset)
            else (None, str(self.started_by).encode(), "text/plain")
        )
        marked_done_by = (
            self.marked_done_by
            if isinstance(self.marked_done_by, Unset)
            else (None, str(self.marked_done_by).encode(), "text/plain")
        )
        killed_by = (
            self.killed_by if isinstance(self.killed_by, Unset) else (None, str(self.killed_by).encode(), "text/plain")
        )
        workflow_snapshot = (None, json.dumps(self.workflow_snapshot.to_dict()).encode(), "application/json")

        _temp_workflow_task_instance_executions = []
        for workflow_task_instance_executions_item_data in self.workflow_task_instance_executions:
            workflow_task_instance_executions_item = workflow_task_instance_executions_item_data.to_dict()

            _temp_workflow_task_instance_executions.append(workflow_task_instance_executions_item)
        workflow_task_instance_executions = (
            None,
            json.dumps(_temp_workflow_task_instance_executions).encode(),
            "application/json",
        )

        _temp_workflow_transition_evaluations = []
        for workflow_transition_evaluations_item_data in self.workflow_transition_evaluations:
            workflow_transition_evaluations_item = workflow_transition_evaluations_item_data.to_dict()

            _temp_workflow_transition_evaluations.append(workflow_transition_evaluations_item)
        workflow_transition_evaluations = (
            None,
            json.dumps(_temp_workflow_transition_evaluations).encode(),
            "application/json",
        )

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        run_reason = (
            self.run_reason
            if isinstance(self.run_reason, Unset)
            else (None, str(self.run_reason).encode(), "text/plain")
        )
        finished_at: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat().encode() if self.finished_at else None

        last_heartbeat_at: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.last_heartbeat_at, Unset):
            last_heartbeat_at = self.last_heartbeat_at.isoformat().encode() if self.last_heartbeat_at else None

        stop_reason = (
            self.stop_reason
            if isinstance(self.stop_reason, Unset)
            else (None, str(self.stop_reason).encode(), "text/plain")
        )
        marked_done_at: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.marked_done_at, Unset):
            marked_done_at = self.marked_done_at.isoformat().encode() if self.marked_done_at else None

        kill_started_at: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.kill_started_at, Unset):
            kill_started_at = self.kill_started_at.isoformat().encode() if self.kill_started_at else None

        kill_finished_at: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.kill_finished_at, Unset):
            kill_finished_at = self.kill_finished_at.isoformat().encode() if self.kill_finished_at else None

        kill_error_code = (
            self.kill_error_code
            if isinstance(self.kill_error_code, Unset)
            else (None, str(self.kill_error_code).encode(), "text/plain")
        )
        failed_attempts = (
            self.failed_attempts
            if isinstance(self.failed_attempts, Unset)
            else (None, str(self.failed_attempts).encode(), "text/plain")
        )
        timed_out_attempts = (
            self.timed_out_attempts
            if isinstance(self.timed_out_attempts, Unset)
            else (None, str(self.timed_out_attempts).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "url": url,
                "uuid": uuid,
                "dashboard_url": dashboard_url,
                "workflow": workflow,
                "status": status,
                "started_at": started_at,
                "started_by": started_by,
                "marked_done_by": marked_done_by,
                "killed_by": killed_by,
                "workflow_snapshot": workflow_snapshot,
                "workflow_task_instance_executions": workflow_task_instance_executions,
                "workflow_transition_evaluations": workflow_transition_evaluations,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if run_reason is not UNSET:
            field_dict["run_reason"] = run_reason
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if last_heartbeat_at is not UNSET:
            field_dict["last_heartbeat_at"] = last_heartbeat_at
        if stop_reason is not UNSET:
            field_dict["stop_reason"] = stop_reason
        if marked_done_at is not UNSET:
            field_dict["marked_done_at"] = marked_done_at
        if kill_started_at is not UNSET:
            field_dict["kill_started_at"] = kill_started_at
        if kill_finished_at is not UNSET:
            field_dict["kill_finished_at"] = kill_finished_at
        if kill_error_code is not UNSET:
            field_dict["kill_error_code"] = kill_error_code
        if failed_attempts is not UNSET:
            field_dict["failed_attempts"] = failed_attempts
        if timed_out_attempts is not UNSET:
            field_dict["timed_out_attempts"] = timed_out_attempts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        uuid = d.pop("uuid")

        dashboard_url = d.pop("dashboard_url")

        workflow = NameAndUuid.from_dict(d.pop("workflow"))

        status = WorkflowExecutionStatus(d.pop("status"))

        started_at = isoparse(d.pop("started_at"))

        started_by = d.pop("started_by")

        marked_done_by = d.pop("marked_done_by")

        killed_by = d.pop("killed_by")

        workflow_snapshot = WorkflowExecutionWorkflowSnapshot.from_dict(d.pop("workflow_snapshot"))

        workflow_task_instance_executions = []
        _workflow_task_instance_executions = d.pop("workflow_task_instance_executions")
        for workflow_task_instance_executions_item_data in _workflow_task_instance_executions:
            workflow_task_instance_executions_item = WorkflowTaskInstanceExecution.from_dict(
                workflow_task_instance_executions_item_data
            )

            workflow_task_instance_executions.append(workflow_task_instance_executions_item)

        workflow_transition_evaluations = []
        _workflow_transition_evaluations = d.pop("workflow_transition_evaluations")
        for workflow_transition_evaluations_item_data in _workflow_transition_evaluations:
            workflow_transition_evaluations_item = WorkflowTransitionEvaluation.from_dict(
                workflow_transition_evaluations_item_data
            )

            workflow_transition_evaluations.append(workflow_transition_evaluations_item)

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        run_reason = d.pop("run_reason", UNSET)

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: Union[Unset, None, datetime.datetime]
        if _finished_at is None:
            finished_at = None
        elif isinstance(_finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = isoparse(_finished_at)

        _last_heartbeat_at = d.pop("last_heartbeat_at", UNSET)
        last_heartbeat_at: Union[Unset, None, datetime.datetime]
        if _last_heartbeat_at is None:
            last_heartbeat_at = None
        elif isinstance(_last_heartbeat_at, Unset):
            last_heartbeat_at = UNSET
        else:
            last_heartbeat_at = isoparse(_last_heartbeat_at)

        stop_reason = d.pop("stop_reason", UNSET)

        _marked_done_at = d.pop("marked_done_at", UNSET)
        marked_done_at: Union[Unset, None, datetime.datetime]
        if _marked_done_at is None:
            marked_done_at = None
        elif isinstance(_marked_done_at, Unset):
            marked_done_at = UNSET
        else:
            marked_done_at = isoparse(_marked_done_at)

        _kill_started_at = d.pop("kill_started_at", UNSET)
        kill_started_at: Union[Unset, None, datetime.datetime]
        if _kill_started_at is None:
            kill_started_at = None
        elif isinstance(_kill_started_at, Unset):
            kill_started_at = UNSET
        else:
            kill_started_at = isoparse(_kill_started_at)

        _kill_finished_at = d.pop("kill_finished_at", UNSET)
        kill_finished_at: Union[Unset, None, datetime.datetime]
        if _kill_finished_at is None:
            kill_finished_at = None
        elif isinstance(_kill_finished_at, Unset):
            kill_finished_at = UNSET
        else:
            kill_finished_at = isoparse(_kill_finished_at)

        kill_error_code = d.pop("kill_error_code", UNSET)

        failed_attempts = d.pop("failed_attempts", UNSET)

        timed_out_attempts = d.pop("timed_out_attempts", UNSET)

        workflow_execution = cls(
            url=url,
            uuid=uuid,
            dashboard_url=dashboard_url,
            workflow=workflow,
            status=status,
            started_at=started_at,
            started_by=started_by,
            marked_done_by=marked_done_by,
            killed_by=killed_by,
            workflow_snapshot=workflow_snapshot,
            workflow_task_instance_executions=workflow_task_instance_executions,
            workflow_transition_evaluations=workflow_transition_evaluations,
            created_at=created_at,
            updated_at=updated_at,
            run_reason=run_reason,
            finished_at=finished_at,
            last_heartbeat_at=last_heartbeat_at,
            stop_reason=stop_reason,
            marked_done_at=marked_done_at,
            kill_started_at=kill_started_at,
            kill_finished_at=kill_finished_at,
            kill_error_code=kill_error_code,
            failed_attempts=failed_attempts,
            timed_out_attempts=timed_out_attempts,
        )

        workflow_execution.additional_properties = d
        return workflow_execution

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
