"""
    Tests for user accounts
"""
import pytest
import respx

import pinterest as pin


@respx.mock
def test_get_user_account(api):
    respx.get(f"{pin.Api.DEFAULT_API_URL}user_account").respond(
        200, json={"username": "merleliukun", "account_type": "BUSINESS"}
    )
    user = api.user_account.get()
    assert user.username == "merleliukun"


@respx.mock
@pytest.mark.asyncio
async def test_async_get_user_account(async_api):
    respx.get(f"{pin.Api.DEFAULT_API_URL}user_account").respond(
        200, json={"username": "merleliukun", "account_type": "BUSINESS"}
    )
    user = await async_api.user_account.get()
    assert user.username == "merleliukun"
