"""
    Tests for pins
"""

import pytest
import respx

import pinterest as pin


@respx.mock
def test_create_pin(api, helpers):
    respx.post(f"{pin.Api.DEFAULT_API_URL}pins").respond(
        status_code=201, json=helpers.load_data("tests/data/pins/pin_data.json")
    )

    p = api.pins.create(
        board_id="1022106146619703648",
        media_source={"source_type": "image_url", "url": "url for image"},
        title="粉堕百花洲，香残燕子楼。 by 曹雪芹",
        description="诗词选自《唐多令·柳絮》 图片来自 https://unsplash.com/",
    )
    assert p.board_id == "1022106146619703648"
    assert p.media.media_type == "image"


@respx.mock
def test_get_pin(api, helpers):
    pin_id = "1022106077905927852"
    respx.get(f"{pin.Api.DEFAULT_API_URL}pins/{pin_id}").respond(
        status_code=200, json=helpers.load_data("tests/data/pins/pin_data.json")
    )
    p = api.pins.get(pin_id=pin_id)
    assert p.id == pin_id
    assert p.parent_pin_id is None


@respx.mock
def test_delete_pin(api):
    pin_id = "1022106077905927852"
    respx.delete(f"{pin.Api.DEFAULT_API_URL}pins/{pin_id}").respond(
        status_code=204,
    )

    deleted = api.pins.delete(pin_id=pin_id)
    assert deleted


@respx.mock
def test_save_pin(api, helpers):
    pin_id = "986429124607234265"
    board_id = "1022106146619857390"

    respx.post(f"{pin.Api.DEFAULT_API_URL}pins/{pin_id}/save").respond(
        status_code=201, json=helpers.load_data("tests/data/pins/pin_save.json")
    )

    saved_pin = api.pins.save(pin_id=pin_id, board_id=board_id)
    assert saved_pin.board_id == board_id
    assert saved_pin.parent_pin_id == pin_id


@respx.mock
def test_get_pin_analytics(api, helpers):
    pin_id = "1022106077905927852"

    respx.get(f"{pin.Api.DEFAULT_API_URL}pins/{pin_id}/analytics").respond(
        status_code=200, json=helpers.load_data("tests/data/pins/pin_analytics.json")
    )

    analytics = api.pins.get_analytics(
        pin_id=pin_id,
        start_date="2022-08-11",
        end_date="2022-08-12",
        metric_types=["IMPRESSION", "SAVE", "PIN_CLICK"],
    )
    assert analytics.all.summary_metrics["IMPRESSION"] == 0.0
    assert analytics.all.daily_metrics[0].data_status == "PROCESSING"


@respx.mock
@pytest.mark.asyncio
async def test_async_create_pin(async_api, helpers):
    respx.post(f"{pin.Api.DEFAULT_API_URL}pins").respond(
        status_code=201, json=helpers.load_data("tests/data/pins/pin_data.json")
    )

    p = await async_api.pins.create(
        board_id="1022106146619703648",
        media_source={"source_type": "image_url", "url": "url for image"},
        title="粉堕百花洲，香残燕子楼。 by 曹雪芹",
        description="诗词选自《唐多令·柳絮》 图片来自 https://unsplash.com/",
    )
    assert p.board_id == "1022106146619703648"
    assert p.media.media_type == "image"


@respx.mock
@pytest.mark.asyncio
async def test_async_get_pin(async_api, helpers):
    pin_id = "1022106077905927852"
    respx.get(f"{pin.Api.DEFAULT_API_URL}pins/{pin_id}").respond(
        status_code=200, json=helpers.load_data("tests/data/pins/pin_data.json")
    )
    p = await async_api.pins.get(pin_id=pin_id)
    assert p.id == pin_id
    assert p.parent_pin_id is None


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_pin(async_api):
    pin_id = "1022106077905927852"
    respx.delete(f"{pin.Api.DEFAULT_API_URL}pins/{pin_id}").respond(
        status_code=204,
    )

    deleted = await async_api.pins.delete(pin_id=pin_id)
    assert deleted


@respx.mock
@pytest.mark.asyncio
async def test_async_save_pin(async_api, helpers):
    pin_id = "986429124607234265"
    board_id = "1022106146619857390"

    respx.post(f"{pin.Api.DEFAULT_API_URL}pins/{pin_id}/save").respond(
        status_code=201, json=helpers.load_data("tests/data/pins/pin_save.json")
    )

    saved_pin = await async_api.pins.save(pin_id=pin_id, board_id=board_id)
    assert saved_pin.board_id == board_id
    assert saved_pin.parent_pin_id == pin_id


@respx.mock
@pytest.mark.asyncio
async def test_async_get_pin_analytics(async_api, helpers):
    pin_id = "1022106077905927852"

    respx.get(f"{pin.Api.DEFAULT_API_URL}pins/{pin_id}/analytics").respond(
        status_code=200, json=helpers.load_data("tests/data/pins/pin_analytics.json")
    )

    analytics = await async_api.pins.get_analytics(
        pin_id=pin_id,
        start_date="2022-08-11",
        end_date="2022-08-12",
        metric_types=["IMPRESSION", "SAVE", "PIN_CLICK"],
    )
    assert analytics.all.summary_metrics["IMPRESSION"] == 0.0
    assert analytics.all.daily_metrics[0].data_status == "PROCESSING"
