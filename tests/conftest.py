import pytest

from pinterest import Api, AsyncApi


@pytest.fixture
def api():
    return Api(access_token="access token")


@pytest.fixture
def async_api():
    return AsyncApi(access_token="access token")
