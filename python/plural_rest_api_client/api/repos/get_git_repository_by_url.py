from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.git_repository import GitRepository
from typing import cast



def _get_kwargs(
    *,
    url_query: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["url"] = url_query


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/api/cd/git/repositories/url",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GitRepository | None:
    if response.status_code == 200:
        response_200 = GitRepository.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GitRepository]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    url_query: str,

) -> Response[GitRepository]:
    """ 
    Args:
        url_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GitRepository]
     """


    kwargs = _get_kwargs(
        url_query=url_query,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    url_query: str,

) -> GitRepository | None:
    """ 
    Args:
        url_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GitRepository
     """


    return sync_detailed(
        client=client,
url_query=url_query,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    url_query: str,

) -> Response[GitRepository]:
    """ 
    Args:
        url_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GitRepository]
     """


    kwargs = _get_kwargs(
        url_query=url_query,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    url_query: str,

) -> GitRepository | None:
    """ 
    Args:
        url_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GitRepository
     """


    return (await asyncio_detailed(
        client=client,
url_query=url_query,

    )).parsed
