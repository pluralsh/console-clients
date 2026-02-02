from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.console_open_apiscm_pull_request_list import ConsoleOpenAPISCMPullRequestList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    cluster_id: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    stack_id: str | Unset = UNSET,
    open_: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["cluster_id"] = cluster_id

    params["service_id"] = service_id

    params["stack_id"] = stack_id

    params["open"] = open_

    params["q"] = q

    params["page"] = page

    params["per_page"] = per_page


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/api/scm/pullrequests",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConsoleOpenAPISCMPullRequestList | None:
    if response.status_code == 200:
        response_200 = ConsoleOpenAPISCMPullRequestList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConsoleOpenAPISCMPullRequestList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cluster_id: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    stack_id: str | Unset = UNSET,
    open_: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> Response[ConsoleOpenAPISCMPullRequestList]:
    """ 
    Args:
        cluster_id (str | Unset):
        service_id (str | Unset):
        stack_id (str | Unset):
        open_ (bool | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPISCMPullRequestList]
     """


    kwargs = _get_kwargs(
        cluster_id=cluster_id,
service_id=service_id,
stack_id=stack_id,
open_=open_,
q=q,
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
    cluster_id: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    stack_id: str | Unset = UNSET,
    open_: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> ConsoleOpenAPISCMPullRequestList | None:
    """ 
    Args:
        cluster_id (str | Unset):
        service_id (str | Unset):
        stack_id (str | Unset):
        open_ (bool | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPISCMPullRequestList
     """


    return sync_detailed(
        client=client,
cluster_id=cluster_id,
service_id=service_id,
stack_id=stack_id,
open_=open_,
q=q,
page=page,
per_page=per_page,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cluster_id: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    stack_id: str | Unset = UNSET,
    open_: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> Response[ConsoleOpenAPISCMPullRequestList]:
    """ 
    Args:
        cluster_id (str | Unset):
        service_id (str | Unset):
        stack_id (str | Unset):
        open_ (bool | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPISCMPullRequestList]
     """


    kwargs = _get_kwargs(
        cluster_id=cluster_id,
service_id=service_id,
stack_id=stack_id,
open_=open_,
q=q,
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
    cluster_id: str | Unset = UNSET,
    service_id: str | Unset = UNSET,
    stack_id: str | Unset = UNSET,
    open_: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> ConsoleOpenAPISCMPullRequestList | None:
    """ 
    Args:
        cluster_id (str | Unset):
        service_id (str | Unset):
        stack_id (str | Unset):
        open_ (bool | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPISCMPullRequestList
     """


    return (await asyncio_detailed(
        client=client,
cluster_id=cluster_id,
service_id=service_id,
stack_id=stack_id,
open_=open_,
q=q,
page=page,
per_page=per_page,

    )).parsed
