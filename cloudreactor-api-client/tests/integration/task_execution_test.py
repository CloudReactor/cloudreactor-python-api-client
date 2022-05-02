import logging

from cloudreactor_api_client import AuthenticatedClient
from cloudreactor_api_client.api.task_executions import (
    task_executions_create,
    task_executions_list,
    task_executions_retrieve,
)
from cloudreactor_api_client.models import TaskExecution, TaskExecutionStatus

logger = logging.getLogger(__name__)


def test_start_task_execution(api_client: AuthenticatedClient, sample_task_name: str):
    task_name = sample_task_name

    task_dict = {"name": task_name}

    te = TaskExecution.from_dict({"task": task_dict, "status": TaskExecutionStatus.MANUALLY_STARTED})

    response_te = task_executions_create.sync_detailed(client=api_client, json_body=te)

    assert response_te.status_code == 201

    parsed_te = response_te.parsed

    assert parsed_te

    te_uuid = parsed_te.uuid
    assert te_uuid
    assert parsed_te.task.uuid
    assert parsed_te.task.name == task_name
    assert parsed_te.status == TaskExecutionStatus.MANUALLY_STARTED
    assert parsed_te.created_at
    assert parsed_te.started_at
    assert parsed_te.updated_at

    get_response_te = task_executions_retrieve.sync_detailed(uuid=te_uuid, client=api_client)

    assert get_response_te.status_code == 200

    get_parsed_te = get_response_te.parsed

    assert get_parsed_te
    assert get_parsed_te.uuid == te_uuid
    assert get_parsed_te.task.uuid == parsed_te.task.uuid
    assert get_parsed_te.task.name == task_name
    assert get_parsed_te.created_at == parsed_te.created_at
    assert get_parsed_te.started_at == parsed_te.started_at
    assert parsed_te.updated_at

    list_response = task_executions_list.sync_detailed(
        client=api_client, task_uuid=parsed_te.task.uuid, ordering="-started_at"
    )

    assert list_response.status_code == 200

    found = False
    for parsed in list_response.parsed.results:
        if parsed.uuid == te_uuid:
            found = True
            assert parsed.task.uuid == parsed_te.task.uuid
            assert parsed.task.name == task_name
            assert parsed.created_at == parsed_te.created_at
            assert parsed.started_at == parsed_te.started_at
            break

    assert found
