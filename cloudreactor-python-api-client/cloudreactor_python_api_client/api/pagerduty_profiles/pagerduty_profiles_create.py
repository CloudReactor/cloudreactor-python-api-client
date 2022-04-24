from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.pager_duty_profile import PagerDutyProfile
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: PagerDutyProfile,
    multipart_data: PagerDutyProfile,
    json_body: PagerDutyProfile,
) -> Dict[str, Any]:
    url = "{}/pagerduty_profiles/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[PagerDutyProfile]:
    if response.status_code == 201:
        response_201 = PagerDutyProfile.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[PagerDutyProfile]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: PagerDutyProfile,
    multipart_data: PagerDutyProfile,
    json_body: PagerDutyProfile,
) -> Response[PagerDutyProfile]:
    """
    Args:
        multipart_data (PagerDutyProfile): A PagerDutyProfile contains user-specific configuration
            on how to notify
            PagerDuty of events.
        json_body (PagerDutyProfile): A PagerDutyProfile contains user-specific configuration on
            how to notify
            PagerDuty of events.

    Returns:
        Response[PagerDutyProfile]
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
    form_data: PagerDutyProfile,
    multipart_data: PagerDutyProfile,
    json_body: PagerDutyProfile,
) -> Optional[PagerDutyProfile]:
    """
    Args:
        multipart_data (PagerDutyProfile): A PagerDutyProfile contains user-specific configuration
            on how to notify
            PagerDuty of events.
        json_body (PagerDutyProfile): A PagerDutyProfile contains user-specific configuration on
            how to notify
            PagerDuty of events.

    Returns:
        Response[PagerDutyProfile]
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
    form_data: PagerDutyProfile,
    multipart_data: PagerDutyProfile,
    json_body: PagerDutyProfile,
) -> Response[PagerDutyProfile]:
    """
    Args:
        multipart_data (PagerDutyProfile): A PagerDutyProfile contains user-specific configuration
            on how to notify
            PagerDuty of events.
        json_body (PagerDutyProfile): A PagerDutyProfile contains user-specific configuration on
            how to notify
            PagerDuty of events.

    Returns:
        Response[PagerDutyProfile]
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
    form_data: PagerDutyProfile,
    multipart_data: PagerDutyProfile,
    json_body: PagerDutyProfile,
) -> Optional[PagerDutyProfile]:
    """
    Args:
        multipart_data (PagerDutyProfile): A PagerDutyProfile contains user-specific configuration
            on how to notify
            PagerDuty of events.
        json_body (PagerDutyProfile): A PagerDutyProfile contains user-specific configuration on
            how to notify
            PagerDuty of events.

    Returns:
        Response[PagerDutyProfile]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
