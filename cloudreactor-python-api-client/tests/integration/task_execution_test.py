import logging
import os

#from dotenv import load_dotenv

from typing import Any, Dict, Optional

from cloudreactor_python_api_client import AuthenticatedClient
from cloudreactor_python_api_client.models import (
  NameAndUuid, TaskExecution, TaskExecutionStatus
)
from cloudreactor_python_api_client.api.task_executions import task_executions_create
from cloudreactor_python_api_client.types import Response

import pytest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)


def test_smoke():
    api_host = os.environ.get('CLOUDREACTOR_API_HOST', 'https://api.cloudreactor.io')
    api_key = os.environ.get('CLOUDREACTOR_API_KEY')
    task_name = os.environ.get('CLOUDREACTOR_SAMPLE_TASK_NAME')

    logging.info(f"api_key = {api_key}")

    client = AuthenticatedClient(base_url=api_host,
        token=api_key)

    task = NameAndUuid.from_dict({
      'name': task_name,
      'url': ''
    })

    te = TaskExecution.from_dict({
        'task': task,
        'status': TaskExecutionStatus.MANUALLY_STARTED,
        'url': ''
    })

    task_executions_create.sync(client=client, json_body=te)

    assert True == False