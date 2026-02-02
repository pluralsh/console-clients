from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.global_service import GlobalService
from ...models.global_service_input import GlobalServiceInput
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: GlobalServiceInput,
    service_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["service_id"] = service_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/api/cd/globalservices",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GlobalService | None:
    if response.status_code == 200:
        response_200 = GlobalService.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GlobalService]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GlobalServiceInput,
    service_id: str | Unset = UNSET,

) -> Response[GlobalService]:
    """ 
    Args:
        service_id (str | Unset):
        body (GlobalServiceInput): Input for creating or updating a global service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GlobalService]
     """


    kwargs = _get_kwargs(
        body=body,
service_id=service_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: GlobalServiceInput,
    service_id: str | Unset = UNSET,

) -> GlobalService | None:
    """ 
    Args:
        service_id (str | Unset):
        body (GlobalServiceInput): Input for creating or updating a global service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GlobalService
     """


    return sync_detailed(
        client=client,
body=body,
service_id=service_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GlobalServiceInput,
    service_id: str | Unset = UNSET,

) -> Response[GlobalService]:
    """ 
    Args:
        service_id (str | Unset):
        body (GlobalServiceInput): Input for creating or updating a global service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GlobalService]
     """


    kwargs = _get_kwargs(
        body=body,
service_id=service_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GlobalServiceInput,
    service_id: str | Unset = UNSET,

) -> GlobalService | None:
    """ 
    Args:
        service_id (str | Unset):
        body (GlobalServiceInput): Input for creating or updating a global service

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GlobalService
     """


    return (await asyncio_detailed(
        client=client,
body=body,
service_id=service_id,

    )).parsed
