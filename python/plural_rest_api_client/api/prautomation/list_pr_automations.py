from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.console_open_apiscm_pr_automation_list import ConsoleOpenAPISCMPrAutomationList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    project_id: str | Unset = UNSET,
    catalog_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["project_id"] = project_id

    params["catalog_id"] = catalog_id

    params["q"] = q

    params["page"] = page

    params["per_page"] = per_page


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/api/scm/prautomations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConsoleOpenAPISCMPrAutomationList | None:
    if response.status_code == 200:
        response_200 = ConsoleOpenAPISCMPrAutomationList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConsoleOpenAPISCMPrAutomationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    catalog_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> Response[ConsoleOpenAPISCMPrAutomationList]:
    """ 
    Args:
        project_id (str | Unset):
        catalog_id (str | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPISCMPrAutomationList]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
catalog_id=catalog_id,
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
    project_id: str | Unset = UNSET,
    catalog_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> ConsoleOpenAPISCMPrAutomationList | None:
    """ 
    Args:
        project_id (str | Unset):
        catalog_id (str | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPISCMPrAutomationList
     """


    return sync_detailed(
        client=client,
project_id=project_id,
catalog_id=catalog_id,
q=q,
page=page,
per_page=per_page,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    catalog_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> Response[ConsoleOpenAPISCMPrAutomationList]:
    """ 
    Args:
        project_id (str | Unset):
        catalog_id (str | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPISCMPrAutomationList]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
catalog_id=catalog_id,
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
    project_id: str | Unset = UNSET,
    catalog_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> ConsoleOpenAPISCMPrAutomationList | None:
    """ 
    Args:
        project_id (str | Unset):
        catalog_id (str | Unset):
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPISCMPrAutomationList
     """


    return (await asyncio_detailed(
        client=client,
project_id=project_id,
catalog_id=catalog_id,
q=q,
page=page,
per_page=per_page,

    )).parsed
