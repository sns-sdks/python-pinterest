"""
    Api implementation.
"""
import inspect
from typing import List, Optional, Tuple, Union

from authlib.integrations.httpx_client import OAuth2Client, AsyncOAuth2Client
from httpx import AsyncClient, Client, Headers, Response

from pinterest import sync, asynchronous
from pinterest.base_endpoint import BaseEndpoint
from pinterest.exceptions import PinterestException


def _is_resource_endpoint(obj):
    return isinstance(obj, BaseEndpoint)


class BaseApi:
    DEFAULT_API_URL = "https://api.pinterest.com/v5/"
    AUTHORIZATION_URL = "https://www.pinterest.com/oauth"
    ACCESS_TOKEN_URL = "https://api.pinterest.com/v5/oauth/token"
    DEFAULT_REDIRECT_URI = "https://localhost/"
    DEFAULT_SCOPE = ["user_accounts:read", "pins:read", "boards:read"]
    STATE = "python-pinterest"

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        api_endpoints = inspect.getmembers(self, _is_resource_endpoint)
        for name, api in api_endpoints:
            api_cls = type(api)
            api = api_cls(self)
            setattr(self, name, api)
        return self

    def __init__(
        self,
        app_id: Optional[int] = None,
        app_secret: Optional[str] = None,
        access_token: Optional[str] = None,
        timeout: Optional[int] = None,
        proxies: Optional[dict] = None,
        headers: Optional[dict] = None,
    ):
        """
        :param app_id: ID for the app.
        :param app_secret: Secret for the app.
        :param access_token: Access token for user.
        :param timeout: Timeout for request.
        :param proxies: Proxies for the request.
        :param headers: Headers for the request.
        """
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = access_token
        self.timeout = timeout
        self.proxies = proxies
        self.headers = headers
        self.client: Optional[Union[Client, AsyncClient]] = None
        self.build_client()

    def build_client(self):
        raise NotImplementedError

    def add_access_token_to_headers(self) -> Headers:
        return Headers({"Authorization": "Bearer " + self.access_token})

    @staticmethod
    def parse_response(response: Response) -> dict:
        """
        Response parser.
        :param response: Response for the request.
        :return: response data.
        """
        if response.is_success:
            return response.json()
        raise PinterestException(**response.json())


class Api(BaseApi):
    user_account = sync.UserAccountEndpoint()
    boards = sync.BoardsEndpoint()
    pins = sync.PinsEndpoint()
    media = sync.MediaEndpoint()
    ad_accounts = sync.AdAccountsEndpoint()

    def build_client(self):
        self.client = Client(
            headers=self.headers, proxies=self.proxies, timeout=self.timeout
        )

    def request(
        self,
        method: str,
        url: str,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
        auth_need: bool = True,
    ) -> Response:
        """
        :param method: Http method.
        :param url: URL for request.
        :param params: URL parameters for request.
        :param json: Json data for request.
        :param auth_need: Is request authorization required.
        :return: Response for the request.
        """
        # Add Authorize Info
        headers = self.add_access_token_to_headers() if auth_need else None

        if not url.startswith("http"):
            url = self.DEFAULT_API_URL + url

        try:
            resp = self.client.request(
                method=method,
                url=url,
                params=params,
                json=json,
                headers=headers,
            )
        except Exception as e:
            raise Exception(e)
        return resp

    def _get_oauth_client(
        self,
        redirect_uri: Optional[str] = None,
        scope: Optional[List[str]] = None,
        **kwargs,
    ) -> OAuth2Client:
        """
        Build a client for OAuth.
        :param redirect_uri: URL for pinterest to redirect.
        :param scope: Scopes for OAuth.
        :param kwargs: Additional parameters for OAuth.
        :return: OAuth2Client
        """
        if not all([self.app_id, self.app_secret]):
            raise PinterestException(code=-1, message="OAuth need app credentials")

        if redirect_uri is None:
            redirect_uri = self.DEFAULT_REDIRECT_URI
        if scope is None:
            scope = self.DEFAULT_SCOPE
        scope = ",".join(scope)

        client = OAuth2Client(
            client_id=self.app_id,
            client_secret=self.app_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            **kwargs,
        )
        return client

    def get_authorization_url(
        self,
        redirect_uri: Optional[str] = None,
        scope: Optional[List[str]] = None,
        **kwargs,
    ) -> Tuple[str, str]:
        """
        Generate an authorization URL and state.

        :param redirect_uri: URL for pinterest to redirect.
        :param scope: Scopes for OAuth.
        :param kwargs: Additional parameters for OAuth.
        :return: Authorize URL and state
        """
        client = self._get_oauth_client(
            redirect_uri=redirect_uri, scope=scope, **kwargs
        )
        authorization_url, state = client.create_authorization_url(
            url=self.AUTHORIZATION_URL
        )
        return authorization_url, state

    def generate_access_token(
        self, response: str, redirect_uri: Optional[str] = None
    ) -> dict:
        """
        Generate the access token by the response.
        :param response: Response url for OAuth.
        :param redirect_uri: URL for pinterest to redirect.
        :return: Access token data
        """
        client = self._get_oauth_client(redirect_uri=redirect_uri)
        token = client.fetch_token(
            url=self.ACCESS_TOKEN_URL,
            authorization_response=response,
            grant_type="authorization_code",
        )
        return token

    def refresh_access_token(
        self, refresh_token: str, scope: Optional[List[str]] = None
    ) -> dict:
        """
        Generate a new access token by the refresh token.
        :param refresh_token: Refresh token.
        :param scope: Scopes for OAuth.
        :return: New access token data.
        """
        client = self._get_oauth_client(scope=scope)
        token = client.refresh_token(
            url=self.ACCESS_TOKEN_URL,
            refresh_token=refresh_token,
            grant_type="refresh_token",
        )
        return token


class AsyncApi(BaseApi):
    user_account = asynchronous.UserAccountAsyncEndpoint()
    boards = asynchronous.BoardsAsyncEndpoint()
    pins = asynchronous.PinsAsyncEndpoint()
    media = asynchronous.MediaAsyncEndpoint()
    ad_accounts = asynchronous.AdAccountsAsyncEndpoint()

    def build_client(self):
        self.client = AsyncClient(
            headers=self.headers, proxies=self.proxies, timeout=self.timeout
        )

    async def request(
        self,
        method: str,
        url: str,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
        auth_need: bool = True,
    ) -> Response:
        """
        :param method: Http method.
        :param url: URL for request.
        :param params: URL parameters for request.
        :param json: Json data for request.
        :param auth_need: Is request authorization required.
        :return: Response for the request.
        """
        # Add Authorize Info
        headers = self.add_access_token_to_headers() if auth_need else None

        if not url.startswith("http"):
            url = self.DEFAULT_API_URL + url

        try:
            resp = await self.client.request(
                method=method,
                url=url,
                params=params,
                json=json,
                headers=headers,
            )
        except Exception as e:
            raise Exception(e)
        return resp

    def _get_oauth_client(
        self,
        redirect_uri: Optional[str] = None,
        scope: Optional[List[str]] = None,
        **kwargs,
    ) -> AsyncOAuth2Client:
        """
        Build a client for OAuth.
        :param redirect_uri: URL for pinterest to redirect.
        :param scope: Scopes for OAuth.
        :param kwargs: Additional parameters for OAuth.
        :return: AsyncOAuth2Client
        """
        if not all([self.app_id, self.app_secret]):
            raise PinterestException(code=-1, message="OAuth need app credentials")

        if redirect_uri is None:
            redirect_uri = self.DEFAULT_REDIRECT_URI
        if scope is None:
            scope = self.DEFAULT_SCOPE
        scope = ",".join(scope)

        client = AsyncOAuth2Client(
            client_id=self.app_id,
            client_secret=self.app_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            **kwargs,
        )
        return client

    def get_authorization_url(
        self,
        redirect_uri: Optional[str] = None,
        scope: Optional[List[str]] = None,
        **kwargs,
    ) -> Tuple[str, str]:
        """

        :param redirect_uri: URL for pinterest to redirect.
        :param scope: Scopes for OAuth.
        :param kwargs: Additional parameters for OAuth.
        :return: Authorize URL and state
        """
        client: AsyncOAuth2Client = self._get_oauth_client(
            redirect_uri=redirect_uri, scope=scope, **kwargs
        )
        authorization_url, state = client.create_authorization_url(
            url=self.AUTHORIZATION_URL
        )
        return authorization_url, state

    async def generate_access_token(
        self, response: str, redirect_uri: Optional[str] = None
    ) -> dict:
        """
        Generate the access token by the response.
        :param response: Response url for OAuth.
        :param redirect_uri: URL for pinterest to redirect.
        :return: Access token data
        """
        client: AsyncOAuth2Client = self._get_oauth_client(redirect_uri=redirect_uri)
        token = await client.fetch_token(
            url=self.ACCESS_TOKEN_URL,
            authorization_response=response,
            grant_type="authorization_code",
        )
        return token

    async def refresh_access_token(
        self, refresh_token: str, scope: Optional[List[str]] = None
    ) -> dict:
        """
        Generate a new access token by the refresh token.
        :param refresh_token: Refresh token.
        :param scope: Scopes for OAuth.
        :return: New access token data.
        """
        client = self._get_oauth_client(scope=scope)
        token = await client.refresh_token(
            url=self.ACCESS_TOKEN_URL,
            refresh_token=refresh_token,
            grant_type="refresh_token",
        )
        return token
