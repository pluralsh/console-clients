from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.console_open_apiai_agent_runtime_list import ConsoleOpenAPIAIAgentRuntimeList
from ...models.list_agent_runtimes_type import ListAgentRuntimesType
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    type_: ListAgentRuntimesType | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["page"] = page

    params["per_page"] = per_page


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/api/ai/runtimes",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConsoleOpenAPIAIAgentRuntimeList | None:
    if response.status_code == 200:
        response_200 = ConsoleOpenAPIAIAgentRuntimeList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConsoleOpenAPIAIAgentRuntimeList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: ListAgentRuntimesType | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> Response[ConsoleOpenAPIAIAgentRuntimeList]:
    """ 
    Args:
        type_ (ListAgentRuntimesType | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPIAIAgentRuntimeList]
     """


    kwargs = _get_kwargs(
        type_=type_,
page=page,
per_page=per_page,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: ListAgentRuntimesType | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> ConsoleOpenAPIAIAgentRuntimeList | None:
    """ 
    Args:
        type_ (ListAgentRuntimesType | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPIAIAgentRuntimeList
     """


    return sync_detailed(
        client=client,
type_=type_,
page=page,
per_page=per_page,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: ListAgentRuntimesType | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> Response[ConsoleOpenAPIAIAgentRuntimeList]:
    """ 
    Args:
        type_ (ListAgentRuntimesType | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPIAIAgentRuntimeList]
     """


    kwargs = _get_kwargs(
        type_=type_,
page=page,
per_page=per_page,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: ListAgentRuntimesType | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> ConsoleOpenAPIAIAgentRuntimeList | None:
    """ 
    Args:
        type_ (ListAgentRuntimesType | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPIAIAgentRuntimeList
     """


    return (await asyncio_detailed(
        client=client,
type_=type_,
page=page,
per_page=per_page,

    )).parsed
