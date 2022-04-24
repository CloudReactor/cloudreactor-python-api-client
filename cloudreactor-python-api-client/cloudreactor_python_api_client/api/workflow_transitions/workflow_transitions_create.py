from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.workflow_transition import WorkflowTransition
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: WorkflowTransition,
    multipart_data: WorkflowTransition,
    json_body: WorkflowTransition,
) -> Dict[str, Any]:
    url = "{}/workflow_transitions/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[WorkflowTransition]:
    if response.status_code == 201:
        response_201 = WorkflowTransition.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[WorkflowTransition]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: WorkflowTransition,
    multipart_data: WorkflowTransition,
    json_body: WorkflowTransition,
) -> Response[WorkflowTransition]:
    """
    Args:
        multipart_data (WorkflowTransition): A WorkflowTransition is a directed edge in a
            Worfklow, which is a directed
            graph. It contains a source WorkflowTaskInstance, a destination
            WorkflowTaskInstance, as well as conditions for triggering the destination
            to execution.
        json_body (WorkflowTransition): A WorkflowTransition is a directed edge in a Worfklow,
            which is a directed
            graph. It contains a source WorkflowTaskInstance, a destination
            WorkflowTaskInstance, as well as conditions for triggering the destination
            to execution.

    Returns:
        Response[WorkflowTransition]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    form_data: WorkflowTransition,
    multipart_data: WorkflowTransition,
    json_body: WorkflowTransition,
) -> Optional[WorkflowTransition]:
    """
    Args:
        multipart_data (WorkflowTransition): A WorkflowTransition is a directed edge in a
            Worfklow, which is a directed
            graph. It contains a source WorkflowTaskInstance, a destination
            WorkflowTaskInstance, as well as conditions for triggering the destination
            to execution.
        json_body (WorkflowTransition): A WorkflowTransition is a directed edge in a Worfklow,
            which is a directed
            graph. It contains a source WorkflowTaskInstance, a destination
            WorkflowTaskInstance, as well as conditions for triggering the destination
            to execution.

    Returns:
        Response[WorkflowTransition]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: WorkflowTransition,
    multipart_data: WorkflowTransition,
    json_body: WorkflowTransition,
) -> Response[WorkflowTransition]:
    """
    Args:
        multipart_data (WorkflowTransition): A WorkflowTransition is a directed edge in a
            Worfklow, which is a directed
            graph. It contains a source WorkflowTaskInstance, a destination
            WorkflowTaskInstance, as well as conditions for triggering the destination
            to execution.
        json_body (WorkflowTransition): A WorkflowTransition is a directed edge in a Worfklow,
            which is a directed
            graph. It contains a source WorkflowTaskInstance, a destination
            WorkflowTaskInstance, as well as conditions for triggering the destination
            to execution.

    Returns:
        Response[WorkflowTransition]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: WorkflowTransition,
    multipart_data: WorkflowTransition,
    json_body: WorkflowTransition,
) -> Optional[WorkflowTransition]:
    """
    Args:
        multipart_data (WorkflowTransition): A WorkflowTransition is a directed edge in a
            Worfklow, which is a directed
            graph. It contains a source WorkflowTaskInstance, a destination
            WorkflowTaskInstance, as well as conditions for triggering the destination
            to execution.
        json_body (WorkflowTransition): A WorkflowTransition is a directed edge in a Worfklow,
            which is a directed
            graph. It contains a source WorkflowTaskInstance, a destination
            WorkflowTaskInstance, as well as conditions for triggering the destination
            to execution.

    Returns:
        Response[WorkflowTransition]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
