from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.run_environment import RunEnvironment
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: RunEnvironment,
    multipart_data: RunEnvironment,
    json_body: RunEnvironment,
) -> Dict[str, Any]:
    url = "{}/run_environments/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[RunEnvironment]:
    if response.status_code == 201:
        response_201 = RunEnvironment.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[RunEnvironment]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: RunEnvironment,
    multipart_data: RunEnvironment,
    json_body: RunEnvironment,
) -> Response[RunEnvironment]:
    """
    Args:
        multipart_data (RunEnvironment): RunEnvironments contain common settings for running a set
            of
            related Tasks. Usually RunEnvironments group Tasks in the same
            deployment environment (e.g. staging or production).
            Task and Workflows belong to a RunEnvironment but can override
            the RunEnvironment's settings.
        json_body (RunEnvironment): RunEnvironments contain common settings for running a set of
            related Tasks. Usually RunEnvironments group Tasks in the same
            deployment environment (e.g. staging or production).
            Task and Workflows belong to a RunEnvironment but can override
            the RunEnvironment's settings.

    Returns:
        Response[RunEnvironment]
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
    form_data: RunEnvironment,
    multipart_data: RunEnvironment,
    json_body: RunEnvironment,
) -> Optional[RunEnvironment]:
    """
    Args:
        multipart_data (RunEnvironment): RunEnvironments contain common settings for running a set
            of
            related Tasks. Usually RunEnvironments group Tasks in the same
            deployment environment (e.g. staging or production).
            Task and Workflows belong to a RunEnvironment but can override
            the RunEnvironment's settings.
        json_body (RunEnvironment): RunEnvironments contain common settings for running a set of
            related Tasks. Usually RunEnvironments group Tasks in the same
            deployment environment (e.g. staging or production).
            Task and Workflows belong to a RunEnvironment but can override
            the RunEnvironment's settings.

    Returns:
        Response[RunEnvironment]
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
    form_data: RunEnvironment,
    multipart_data: RunEnvironment,
    json_body: RunEnvironment,
) -> Response[RunEnvironment]:
    """
    Args:
        multipart_data (RunEnvironment): RunEnvironments contain common settings for running a set
            of
            related Tasks. Usually RunEnvironments group Tasks in the same
            deployment environment (e.g. staging or production).
            Task and Workflows belong to a RunEnvironment but can override
            the RunEnvironment's settings.
        json_body (RunEnvironment): RunEnvironments contain common settings for running a set of
            related Tasks. Usually RunEnvironments group Tasks in the same
            deployment environment (e.g. staging or production).
            Task and Workflows belong to a RunEnvironment but can override
            the RunEnvironment's settings.

    Returns:
        Response[RunEnvironment]
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
    form_data: RunEnvironment,
    multipart_data: RunEnvironment,
    json_body: RunEnvironment,
) -> Optional[RunEnvironment]:
    """
    Args:
        multipart_data (RunEnvironment): RunEnvironments contain common settings for running a set
            of
            related Tasks. Usually RunEnvironments group Tasks in the same
            deployment environment (e.g. staging or production).
            Task and Workflows belong to a RunEnvironment but can override
            the RunEnvironment's settings.
        json_body (RunEnvironment): RunEnvironments contain common settings for running a set of
            related Tasks. Usually RunEnvironments group Tasks in the same
            deployment environment (e.g. staging or production).
            Task and Workflows belong to a RunEnvironment but can override
            the RunEnvironment's settings.

    Returns:
        Response[RunEnvironment]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
