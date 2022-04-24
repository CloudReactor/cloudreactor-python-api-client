from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.patched_workflow import PatchedWorkflow
from ...models.workflow import Workflow
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedWorkflow,
    multipart_data: PatchedWorkflow,
    json_body: PatchedWorkflow,
) -> Dict[str, Any]:
    url = "{}/workflows/{uuid}/".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Workflow]:
    if response.status_code == 200:
        response_200 = Workflow.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Workflow]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedWorkflow,
    multipart_data: PatchedWorkflow,
    json_body: PatchedWorkflow,
) -> Response[Workflow]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedWorkflow): Workflows are Tasks arranged in a directed graph.
            Configured Tasks
            are held by WorkflowTaskInstances, and WorkflowTransitions connect
            WorkflowTaskInstances together.
        json_body (PatchedWorkflow): Workflows are Tasks arranged in a directed graph. Configured
            Tasks
            are held by WorkflowTaskInstances, and WorkflowTransitions connect
            WorkflowTaskInstances together.

    Returns:
        Response[Workflow]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedWorkflow,
    multipart_data: PatchedWorkflow,
    json_body: PatchedWorkflow,
) -> Optional[Workflow]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedWorkflow): Workflows are Tasks arranged in a directed graph.
            Configured Tasks
            are held by WorkflowTaskInstances, and WorkflowTransitions connect
            WorkflowTaskInstances together.
        json_body (PatchedWorkflow): Workflows are Tasks arranged in a directed graph. Configured
            Tasks
            are held by WorkflowTaskInstances, and WorkflowTransitions connect
            WorkflowTaskInstances together.

    Returns:
        Response[Workflow]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedWorkflow,
    multipart_data: PatchedWorkflow,
    json_body: PatchedWorkflow,
) -> Response[Workflow]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedWorkflow): Workflows are Tasks arranged in a directed graph.
            Configured Tasks
            are held by WorkflowTaskInstances, and WorkflowTransitions connect
            WorkflowTaskInstances together.
        json_body (PatchedWorkflow): Workflows are Tasks arranged in a directed graph. Configured
            Tasks
            are held by WorkflowTaskInstances, and WorkflowTransitions connect
            WorkflowTaskInstances together.

    Returns:
        Response[Workflow]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedWorkflow,
    multipart_data: PatchedWorkflow,
    json_body: PatchedWorkflow,
) -> Optional[Workflow]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedWorkflow): Workflows are Tasks arranged in a directed graph.
            Configured Tasks
            are held by WorkflowTaskInstances, and WorkflowTransitions connect
            WorkflowTaskInstances together.
        json_body (PatchedWorkflow): Workflows are Tasks arranged in a directed graph. Configured
            Tasks
            are held by WorkflowTaskInstances, and WorkflowTransitions connect
            WorkflowTaskInstances together.

    Returns:
        Response[Workflow]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
