"""
    Endpoint class for Pinterest. like pins,boards and so on.
"""
from httpx import Response


class BaseEndpoint:
    """Pinterest Endpoint base class"""

    def __init__(self, client=None):
        self._client = client

    @property
    def access_token(self):
        return self._client.access_token

    @property
    def app_id(self):
        return self._client.app_id

    @property
    def app_secret(self):
        return self._client.app_secret

    def _parse_response(self, response: Response):
        return self._client.parse_response(response=response)


class Endpoint(BaseEndpoint):
    def _get(self, url, **kwargs):
        return self._client.request(
            method="GET",
            url=url,
            **kwargs,
        )

    def _post(self, url, **kwargs):
        return self._client.request(
            method="POST",
            url=url,
            **kwargs,
        )

    def _patch(self, url, **kwargs):
        return self._client.request(
            method="PATCH",
            url=url,
            **kwargs,
        )

    def _delete(self, url, **kwargs):
        return self._client.request(
            method="DELETE",
            url=url,
            **kwargs,
        )


class AsyncEndpoint(BaseEndpoint):
    async def _get(self, url, **kwargs):
        return await self._client.request(
            method="GET",
            url=url,
            **kwargs,
        )

    async def _post(self, url, **kwargs):
        return await self._client.request(
            method="POST",
            url=url,
            **kwargs,
        )

    async def _patch(self, url, **kwargs):
        return await self._client.request(
            method="PATCH",
            url=url,
            **kwargs,
        )

    async def _delete(self, url, **kwargs):
        return await self._client.request(
            method="DELETE",
            url=url,
            **kwargs,
        )
