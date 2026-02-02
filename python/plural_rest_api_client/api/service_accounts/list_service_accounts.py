from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.console_open_api_user_list import ConsoleOpenAPIUserList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/api/serviceaccounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConsoleOpenAPIUserList | None:
    if response.status_code == 200:
        response_200 = ConsoleOpenAPIUserList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConsoleOpenAPIUserList]:
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
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[ConsoleOpenAPIUserList]:
    """
    Args:
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPIUserList]
    """

    kwargs = _get_kwargs(
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
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> ConsoleOpenAPIUserList | None:
    """
    Args:
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPIUserList
    """

    return sync_detailed(
        client=client,
        q=q,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> Response[ConsoleOpenAPIUserList]:
    """
    Args:
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsoleOpenAPIUserList]
    """

    kwargs = _get_kwargs(
        q=q,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
) -> ConsoleOpenAPIUserList | None:
    """
    Args:
        q (str | Unset):
        page (int | Unset):
        per_page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsoleOpenAPIUserList
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            page=page,
            per_page=per_page,
        )
    ).parsed
