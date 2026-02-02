from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.service import Service
from ...models.service_input import ServiceInput
from typing import cast



def _get_kwargs(
    *,
    body: ServiceInput,
    cluster_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["cluster_id"] = cluster_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/api/cd/services",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Service | None:
    if response.status_code == 200:
        response_200 = Service.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Service]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ServiceInput,
    cluster_id: str,

) -> Response[Service]:
    """ 
    Args:
        cluster_id (str):
        body (ServiceInput): Input for creating or updating a service deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Service]
     """


    kwargs = _get_kwargs(
        body=body,
cluster_id=cluster_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ServiceInput,
    cluster_id: str,

) -> Service | None:
    """ 
    Args:
        cluster_id (str):
        body (ServiceInput): Input for creating or updating a service deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Service
     """


    return sync_detailed(
        client=client,
body=body,
cluster_id=cluster_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ServiceInput,
    cluster_id: str,

) -> Response[Service]:
    """ 
    Args:
        cluster_id (str):
        body (ServiceInput): Input for creating or updating a service deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Service]
     """


    kwargs = _get_kwargs(
        body=body,
cluster_id=cluster_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ServiceInput,
    cluster_id: str,

) -> Service | None:
    """ 
    Args:
        cluster_id (str):
        body (ServiceInput): Input for creating or updating a service deployment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Service
     """


    return (await asyncio_detailed(
        client=client,
body=body,
cluster_id=cluster_id,

    )).parsed
