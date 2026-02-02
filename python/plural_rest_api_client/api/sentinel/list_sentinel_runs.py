from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.console_open_apiai_sentinel_run_list import ConsoleOpenAPIAISentinelRunList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    sentinel_id: str,
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/api/ai/sentinels/{sentinel_id}/runs".format(sentinel_id=quote(str(sentinel_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConsoleOpenAPIAISentinelRunList | None:
    if response.status_code == 200:
        response_200 = ConsoleOpenAPIAISentinelRunList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConsoleOpenAPIAISentinelRunList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sentinel_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> Response[ConsoleOpenAPIAISentinelRunList]:
    """ 
    Args:
        sentinel_id (str):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPIAISentinelRunList]
     """


    kwargs = _get_kwargs(
        sentinel_id=sentinel_id,
page=page,
per_page=per_page,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    sentinel_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> ConsoleOpenAPIAISentinelRunList | None:
    """ 
    Args:
        sentinel_id (str):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPIAISentinelRunList
     """


    return sync_detailed(
        sentinel_id=sentinel_id,
client=client,
page=page,
per_page=per_page,

    ).parsed

async def asyncio_detailed(
    sentinel_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> Response[ConsoleOpenAPIAISentinelRunList]:
    """ 
    Args:
        sentinel_id (str):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPIAISentinelRunList]
     """


    kwargs = _get_kwargs(
        sentinel_id=sentinel_id,
page=page,
per_page=per_page,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    sentinel_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> ConsoleOpenAPIAISentinelRunList | None:
    """ 
    Args:
        sentinel_id (str):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPIAISentinelRunList
     """


    return (await asyncio_detailed(
        sentinel_id=sentinel_id,
client=client,
page=page,
per_page=per_page,

    )).parsed
