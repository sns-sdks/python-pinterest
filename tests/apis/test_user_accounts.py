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
def test_get_user_analytics(api, helpers):
    respx.get(f"{pin.Api.DEFAULT_API_URL}user_account/analytics").respond(
        status_code=200,
        json=helpers.load_data("tests/data/user_account/analytics.json"),
    )
    analytics = api.user_account.get_analytics(
        start_date="2022-08-09",
        end_date="2022-08-11",
    )
    assert analytics.all.summary_metrics["PIN_CLICK"] == 0


@respx.mock
def test_get_top_pins_analytics(api, helpers):
    respx.get(f"{pin.Api.DEFAULT_API_URL}user_account/analytics/top_pins").respond(
        status_code=200,
        json=helpers.load_data("tests/data/user_account/top_pins_analytics.json"),
    )
    analytics = api.user_account.get_top_pins_analytics(
        start_date="2022-08-09",
        end_date="2022-08-12",
        sort_by="IMPRESSION",
    )
    assert analytics.date_availability.latest_available_timestamp == 1660089599000
    assert analytics.pins[0].data_status["SAVE"] == "READY"


@respx.mock
def test_get_top_video_pins_analytics(api, helpers):
    respx.get(
        f"{pin.Api.DEFAULT_API_URL}user_account/analytics/top_video_pins"
    ).respond(
        status_code=200,
        json=helpers.load_data("tests/data/user_account/top_video_pins_analytics.json"),
    )
    analytics = api.user_account.get_top_video_pins_analytics(
        start_date="2022-08-09",
        end_date="2022-08-12",
        sort_by="IMPRESSION",
    )
    assert not analytics.date_availability.is_realtime
    assert analytics.pins[0].data_status["SAVE_RATE"] == "READY"


@respx.mock
@pytest.mark.asyncio
async def test_async_get_user_account(async_api):
    respx.get(f"{pin.Api.DEFAULT_API_URL}user_account").respond(
        200, json={"username": "merleliukun", "account_type": "BUSINESS"}
    )
    user = await async_api.user_account.get()
    assert user.username == "merleliukun"


@respx.mock
@pytest.mark.asyncio
async def test_async_get_user_analytics(async_api, helpers):
    respx.get(f"{pin.Api.DEFAULT_API_URL}user_account/analytics").respond(
        status_code=200,
        json=helpers.load_data("tests/data/user_account/analytics.json"),
    )
    analytics = await async_api.user_account.get_analytics(
        start_date="2022-08-09",
        end_date="2022-08-11",
    )
    assert analytics.all.summary_metrics["PIN_CLICK"] == 0


@respx.mock
@pytest.mark.asyncio
async def test_async_get_top_pins_analytics(async_api, helpers):
    respx.get(f"{pin.Api.DEFAULT_API_URL}user_account/analytics/top_pins").respond(
        status_code=200,
        json=helpers.load_data("tests/data/user_account/top_pins_analytics.json"),
    )
    analytics = await async_api.user_account.get_top_pins_analytics(
        start_date="2022-08-09",
        end_date="2022-08-12",
        sort_by="IMPRESSION",
    )
    assert analytics.date_availability.latest_available_timestamp == 1660089599000
    assert analytics.pins[0].data_status["SAVE"] == "READY"


@respx.mock
@pytest.mark.asyncio
async def test_async_get_top_video_pins_analytics(async_api, helpers):
    respx.get(
        f"{pin.Api.DEFAULT_API_URL}user_account/analytics/top_video_pins"
    ).respond(
        status_code=200,
        json=helpers.load_data("tests/data/user_account/top_video_pins_analytics.json"),
    )
    analytics = await async_api.user_account.get_top_video_pins_analytics(
        start_date="2022-08-09",
        end_date="2022-08-12",
        sort_by="IMPRESSION",
    )
    assert not analytics.date_availability.is_realtime
    assert analytics.pins[0].data_status["SAVE_RATE"] == "READY"
