import logging
from datetime import datetime

from cloudreactor_python_api_client import AuthenticatedClient
from cloudreactor_python_api_client.api.tasks import (
    tasks_create,
    tasks_destroy,
    tasks_partial_update,
)
from cloudreactor_python_api_client.models import (
    NameAndUuid,
    PatchedTask,
    Task,
    UnknownExecutionMethodCapability,
)

logger = logging.getLogger(__name__)


def test_task_manipulation(api_client: AuthenticatedClient, sample_run_environment_name: str):
    now = datetime.now()
    task_name = "python-api-client-test-" + now.isoformat()
    description = "Test Task for Python API Client"

    run_environment = NameAndUuid(name=sample_run_environment_name)
    emc = UnknownExecutionMethodCapability()

    task = Task(
        name=task_name,
        description=description,
        run_environment=run_environment,
        passive=True,
        enabled=True,
        execution_method_capability=emc,
    )

    try:
        create_response = tasks_create.sync_detailed(client=api_client, json_body=task)

        assert create_response.status_code == 201

        created_task = create_response.parsed
        assert created_task
        assert created_task.name == task_name
        assert created_task.description == description
        assert created_task.run_environment.name == run_environment.name
        assert created_task.passive
        assert created_task.enabled
        assert created_task.execution_method_capability.type == "Unknown"

        patched_task = PatchedTask(
            name=task_name + "-patched",
            description=description + "-patched",
            enabled=False,
        )

        patch_response = tasks_partial_update.sync_detailed(
            uuid=created_task.uuid, client=api_client, json_body=patched_task
        )

        updated_task = patch_response.parsed
        assert updated_task
        assert updated_task.name == patched_task.name
        assert updated_task.description == patched_task.description
        assert not updated_task.enabled
    finally:
        destroy_response = tasks_destroy.sync_detailed(uuid=created_task.uuid, client=api_client)

        assert destroy_response.status_code == 204
