from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.console_open_apicd_cluster_list import ConsoleOpenAPICDClusterList
from ...models.list_clusters_compliance import ListClustersCompliance
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    healthy: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    upgradeable: bool | Unset = UNSET,
    compliance: ListClustersCompliance | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q

    params["project_id"] = project_id

    params["healthy"] = healthy

    params["tag"] = tag

    params["upgradeable"] = upgradeable

    json_compliance: str | Unset = UNSET
    if not isinstance(compliance, Unset):
        json_compliance = compliance.value

    params["compliance"] = json_compliance

    params["page"] = page

    params["per_page"] = per_page


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/api/cd/clusters",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConsoleOpenAPICDClusterList | None:
    if response.status_code == 200:
        response_200 = ConsoleOpenAPICDClusterList.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConsoleOpenAPICDClusterList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    healthy: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    upgradeable: bool | Unset = UNSET,
    compliance: ListClustersCompliance | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> Response[ConsoleOpenAPICDClusterList]:
    """ 
    Args:
        q (str | Unset):
        project_id (str | Unset):
        healthy (bool | Unset):
        tag (str | Unset):
        upgradeable (bool | Unset):
        compliance (ListClustersCompliance | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPICDClusterList]
     """


    kwargs = _get_kwargs(
        q=q,
project_id=project_id,
healthy=healthy,
tag=tag,
upgradeable=upgradeable,
compliance=compliance,
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
    q: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    healthy: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    upgradeable: bool | Unset = UNSET,
    compliance: ListClustersCompliance | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> ConsoleOpenAPICDClusterList | None:
    """ 
    Args:
        q (str | Unset):
        project_id (str | Unset):
        healthy (bool | Unset):
        tag (str | Unset):
        upgradeable (bool | Unset):
        compliance (ListClustersCompliance | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPICDClusterList
     """


    return sync_detailed(
        client=client,
q=q,
project_id=project_id,
healthy=healthy,
tag=tag,
upgradeable=upgradeable,
compliance=compliance,
page=page,
per_page=per_page,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    healthy: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    upgradeable: bool | Unset = UNSET,
    compliance: ListClustersCompliance | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> Response[ConsoleOpenAPICDClusterList]:
    """ 
    Args:
        q (str | Unset):
        project_id (str | Unset):
        healthy (bool | Unset):
        tag (str | Unset):
        upgradeable (bool | Unset):
        compliance (ListClustersCompliance | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPICDClusterList]
     """


    kwargs = _get_kwargs(
        q=q,
project_id=project_id,
healthy=healthy,
tag=tag,
upgradeable=upgradeable,
compliance=compliance,
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
    q: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    healthy: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    upgradeable: bool | Unset = UNSET,
    compliance: ListClustersCompliance | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,

) -> ConsoleOpenAPICDClusterList | None:
    """ 
    Args:
        q (str | Unset):
        project_id (str | Unset):
        healthy (bool | Unset):
        tag (str | Unset):
        upgradeable (bool | Unset):
        compliance (ListClustersCompliance | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPICDClusterList
     """


    return (await asyncio_detailed(
        client=client,
q=q,
project_id=project_id,
healthy=healthy,
tag=tag,
upgradeable=upgradeable,
compliance=compliance,
page=page,
per_page=per_page,

    )).parsed
