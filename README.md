# cloudreactor-python-api-client

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/CloudReactor/cloudreactor-python-api-client/CI)](https://github.com/CloudReactor/cloudreactor-python-api-client/actions/workflows/ci.yml)
[![Codecov](https://img.shields.io/codecov/c/github/CloudReactor/cloudreactor-python-api-client)](https://app.codecov.io/github/CloudReactor/cloudreactor-python-api-client)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![PyPI](https://img.shields.io/pypi/v/cloudreactor-api-client)](https://pypi.org/project/cloudreactor-api-client/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cloudreactor-api-client)
[![PyPI - License](https://img.shields.io/pypi/l/cloudreactor-api-client)](https://opensource.org/licenses/BSD-2-Clause)
![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/CloudReactor/cloudreactor-python-api-client)


Python client for the CloudReactor API

## Overview

This python package allows python applications to programmatically
create, monitor, and manage Tasks and Workflows in CloudReactor. Most
notably, you can start and stop Tasks and Workflows by creating Task
Executions and Workflow Executions.

## Installation

Get this package from PyPI:

```bash
pip install cloudreactor_api_client
```

## Usage

First, create a client:

```python
from cloudreactor-python_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.cloudreactor.io", token="YOUR_API_KEY")

```

To start a Task, create a Task Execution:

```python
from cloudreactor_api_client.api.task_executions import (
    task_executions_create
)
from cloudreactor_api_client.models import TaskExecution, TaskExecutionStatus

# Identify the Task by name. Alternatively, you can specifiy the "uuid".
task_dict = {"name": task_name}

task_execution = TaskExecution.from_dict({"task": task_dict, "status": TaskExecutionStatus.MANUALLY_STARTED})

response = task_executions_create.sync_detailed(client=client, json_body=task_execution)

parsed_task_execution = response.parsed

print(f"Task Execution {parsed_task_execution.uuid} started!")

```

More details on how to use API clients in general (async mode, disabling SSL)
can be found in the generated [README](cloudreactor-api-client/README.md).


## Credits

Code generated by [openapi-python-client](https://github.com/openapi-generators/openapi-python-client)
