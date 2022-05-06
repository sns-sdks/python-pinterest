import json

import pytest

from pinterest import Api, AsyncApi


@pytest.fixture
def api():
    return Api(access_token="access token")


@pytest.fixture
def async_api():
    return AsyncApi(access_token="access token")


class Helpers:
    @staticmethod
    def load_data(filename):
        with open(filename, "rb") as f:
            return json.loads(f.read().decode("utf-8"))


@pytest.fixture
def helpers():
    return Helpers
