"""
    Tests for catalogs apis.
"""

import pytest
import respx

import pinterest as pin


@respx.mock
def test_list_feeds(api, helpers):
    respx.get(f"{pin.Api.DEFAULT_API_URL}catalogs/feeds").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/list_feeds_resp.json"),
    )
    feeds = api.catalogs.list_catalogs_feeds(bookmark="bookmark")
    assert len(feeds.items) == 1


@respx.mock
def test_create_feed(api, helpers):
    respx.post(f"{pin.Api.DEFAULT_API_URL}catalogs/feeds").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/create_feed_resp.json"),
    )
    feed = api.catalogs.create_catalogs_feed(
        name="string",
        format="TSV",
        location="string",
        default_country="US",
        default_availability="IN_STOCK",
        default_currency="USD",
        default_locale="en_US",
        credentials={"password": "pa$$word", "username": "string"},
        preferred_processing_schedule={"time": "02:59", "timezone": "Africa/Abidjan"},
    )
    assert feed.name == "string"


@respx.mock
def test_get_feed(api, helpers):
    feed_id = "string"
    respx.get(f"{pin.Api.DEFAULT_API_URL}catalogs/feeds/{feed_id}").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/get_feed_resp.json"),
    )
    feed = api.catalogs.get_catalogs_feed(feed_id=feed_id)
    assert feed.name == "string"


@respx.mock
def test_update_feed(api, helpers):
    feed_id = "string"
    respx.patch(f"{pin.Api.DEFAULT_API_URL}catalogs/feeds/{feed_id}").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/update_feed_resp.json"),
    )
    feed = api.catalogs.update_catalogs_feed(
        feed_id=feed_id,
        default_availability="IN_STOCK",
        default_currency="USD",
        name="string",
        format="TSV",
        location="string",
        status="ACTIVE",
        credentials={"password": "pa$$word", "username": "string"},
        preferred_processing_schedule={"time": "02:59", "timezone": "Africa/Abidjan"},
    )
    assert feed.name == "string"


@respx.mock
def test_delete_feed(api, helpers):
    feed_id = "string"
    respx.delete(f"{pin.Api.DEFAULT_API_URL}catalogs/feeds/{feed_id}").respond(
        status_code=200,
        json={"code": 0, "message": "string"},
    )
    feed_del = api.catalogs.delete_catalogs_feed(feed_id=feed_id)
    assert feed_del


@respx.mock
def test_list_catalogs_feed_processing_results(api, helpers):
    feed_id = "string"
    respx.get(
        f"{pin.Api.DEFAULT_API_URL}catalogs/feeds/{feed_id}/processing_results"
    ).respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/feed_processing_results_resp.json"),
    )
    results = api.catalogs.list_catalogs_feed_processing_results(feed_id=feed_id)
    assert len(results.items) == 1


@respx.mock
def test_get_catalog_items(api, helpers):
    respx.get(f"{pin.Api.DEFAULT_API_URL}catalogs/items").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/get_catalog_items_resp.json"),
    )
    items = api.catalogs.get_catalogs_items(
        country="US", item_ids=["CR123"], language="EN"
    )
    assert len(items.items) == 1


@respx.mock
def test_get_catalog_items_batch(api, helpers):
    batch_id = "595953100599279259-66753b9bb65c46c49bd8503b27fecf9e"
    respx.get(f"{pin.Api.DEFAULT_API_URL}catalogs/items/batch/{batch_id}").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/get_catalog_items_batch_resp.json"),
    )
    batch = api.catalogs.get_catalogs_items_batch(batch_id=batch_id)
    assert batch.batch_id == batch_id


@respx.mock
def test_perform_items_batch(api, helpers):
    respx.post(f"{pin.Api.DEFAULT_API_URL}catalogs/items/batch").respond(
        status_code=200,
        json=helpers.load_data(
            "tests/data/catalogs/perform_operation_item_batch_resp.json"
        ),
    )
    batch = api.catalogs.perform_items_batch(
        operation="UPDATE",
        country="US",
        language="EN",
        items=[
            {
                "item_id": "DS0294-M",
                "attributes": {
                    "ad_link": "https://www.example.com/cat/denim-shirt/item012?utm_source=Pinterest",
                    "additional_image_link": [
                        "https://scene.example.com/image/image_v2.jpg",
                        "https://scene.example.com/image/image_v3.jpg",
                    ],
                    "adult": True,
                    "age_group": "newborn",
                    "availability": "in stock",
                    "average_review_rating": 5,
                    "brand": "Josie’s Denim",
                    "color": "blue",
                    "condition": "new",
                    "custom_label_0": "Best sellers",
                    "custom_label_1": "Summer promotion",
                    "custom_label_2": "Winter sales",
                    "custom_label_3": "Woman dress",
                    "custom_label_4": "Man hat",
                    "description": "Casual fit denim shirt made with the finest quality Japanese denim.",
                    "free_shipping_label": True,
                    "free_shipping_limit": "35 USD",
                    "gender": "unisex",
                    "google_product_category": "Apparel & Accessories > Clothing > Shirts & Tops",
                    "gtin": 3234567890126,
                    "id": "DS0294-L",
                    "image_link": ["https://scene.example.com/image/image.jpg"],
                    "item_group_id": "DS0294",
                    "last_updated_time": 1641483432072,
                    "link": "https://www.example.com/cat/womens-clothing/denim-shirt-0294",
                    "material": "cotton",
                    "min_ad_price": "19.99 USD",
                    "mobile_link": "https://m.example.com/cat/womens-clothing/denim-shirt-0294",
                    "mpn": "PI12345NTEREST",
                    "number_of_ratings": 10,
                    "number_of_reviews": 10,
                    "pattern": "plaid",
                    "price": "24.99 USD",
                    "product_type": "Clothing > Women’s > Shirts > Denim",
                    "sale_price": "14.99 USD",
                    "shipping": "US:CA:Ground:0 USD",
                    "shipping_height": "12 in",
                    "shipping_weight": "3 kg",
                    "shipping_width": "16 in",
                    "size": "M",
                    "size_system": "US",
                    "size_type": "regular",
                    "tax": "US:1025433:6.00:y",
                    "title": "Women’s denim shirt, large",
                },
            }
        ],
    )
    assert batch.batch_id == "595953100599279259-66753b9bb65c46c49bd8503b27fecf9e"
    assert batch.status == "PROCESSING"


@respx.mock
def test_get_product_group(api, helpers):
    product_group_id = "443727193917"
    respx.get(
        f"{pin.Api.DEFAULT_API_URL}catalogs/product_groups/{product_group_id}"
    ).respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/get_product_group_resp.json"),
    )
    pg = api.catalogs.get_product_group(product_group_id=product_group_id)
    assert pg.name == "Most Popular"


@respx.mock
def test_create_product_group(api, helpers):
    respx.post(f"{pin.Api.DEFAULT_API_URL}catalogs/product_groups").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/create_product_group_resp.json"),
    )
    pg = api.catalogs.create_product_group(
        feed_id="2680059592705",
        name="Most Popular",
        filters={
            "any_of": [{"MIN_PRICE": {"inclusion": True, "values": 0, "negated": True}}]
        },
        description="string",
    )
    assert pg.name == "Most Popular"


@respx.mock
def test_update_product_group(api, helpers):
    product_group_id = "443727193917"
    respx.patch(
        f"{pin.Api.DEFAULT_API_URL}catalogs/product_groups/{product_group_id}"
    ).respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/update_product_group_resp.json"),
    )
    pg = api.catalogs.update_product_group(
        product_group_id=product_group_id,
        feed_id="2680059592705",
        name="Most Popular",
        description="string",
        filters={
            "any_of": [{"MIN_PRICE": {"inclusion": True, "values": 0, "negated": True}}]
        },
    )
    assert pg.id == product_group_id


@respx.mock
def test_delete_product_group(api, helpers):
    product_group_id = "443727193917"
    respx.delete(
        f"{pin.Api.DEFAULT_API_URL}catalogs/product_groups/{product_group_id}"
    ).respond(
        status_code=204,
        json={"code": 0, "message": "string"},
    )
    st = api.catalogs.delete_product_group(product_group_id=product_group_id)
    assert st


@respx.mock
def test_get_product_group_list(api, helpers):
    feed_id = "2680059592705"
    respx.get(f"{pin.Api.DEFAULT_API_URL}catalogs/product_groups").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/get_product_groups_list_resp.json"),
    )
    pgs = api.catalogs.get_product_group_list(
        feed_id=feed_id,
        page_size=1,
        bookmark="string",
    )
    assert len(pgs.items) == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_list_feeds(async_api, helpers):
    respx.get(f"{pin.Api.DEFAULT_API_URL}catalogs/feeds").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/list_feeds_resp.json"),
    )
    feeds = await async_api.catalogs.list_catalogs_feeds(bookmark="bookmark")
    assert len(feeds.items) == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_create_feed(async_api, helpers):
    respx.post(f"{pin.Api.DEFAULT_API_URL}catalogs/feeds").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/create_feed_resp.json"),
    )
    feed = await async_api.catalogs.create_catalogs_feed(
        name="string",
        format="TSV",
        location="string",
        default_country="US",
        default_availability="IN_STOCK",
        default_currency="USD",
        default_locale="en_US",
        credentials={"password": "pa$$word", "username": "string"},
        preferred_processing_schedule={"time": "02:59", "timezone": "Africa/Abidjan"},
    )
    assert feed.name == "string"


@respx.mock
@pytest.mark.asyncio
async def test_async_get_feed(async_api, helpers):
    feed_id = "string"
    respx.get(f"{pin.Api.DEFAULT_API_URL}catalogs/feeds/{feed_id}").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/get_feed_resp.json"),
    )
    feed = await async_api.catalogs.get_catalogs_feed(feed_id=feed_id)
    assert feed.name == "string"


@respx.mock
@pytest.mark.asyncio
async def test_async_update_feed(async_api, helpers):
    feed_id = "string"
    respx.patch(f"{pin.Api.DEFAULT_API_URL}catalogs/feeds/{feed_id}").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/update_feed_resp.json"),
    )
    feed = await async_api.catalogs.update_catalogs_feed(
        feed_id=feed_id,
        default_availability="IN_STOCK",
        default_currency="USD",
        name="string",
        format="TSV",
        location="string",
        status="ACTIVE",
        credentials={"password": "pa$$word", "username": "string"},
        preferred_processing_schedule={"time": "02:59", "timezone": "Africa/Abidjan"},
    )
    assert feed.name == "string"


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_feed(async_api, helpers):
    feed_id = "string"
    respx.delete(f"{pin.Api.DEFAULT_API_URL}catalogs/feeds/{feed_id}").respond(
        status_code=200,
        json={"code": 0, "message": "string"},
    )
    feed_del = await async_api.catalogs.delete_catalogs_feed(feed_id=feed_id)
    assert feed_del


@respx.mock
@pytest.mark.asyncio
async def test_async_list_catalogs_feed_processing_results(async_api, helpers):
    feed_id = "string"
    respx.get(
        f"{pin.Api.DEFAULT_API_URL}catalogs/feeds/{feed_id}/processing_results"
    ).respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/feed_processing_results_resp.json"),
    )
    results = await async_api.catalogs.list_catalogs_feed_processing_results(
        feed_id=feed_id
    )
    assert len(results.items) == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_get_catalog_items(async_api, helpers):
    respx.get(f"{pin.Api.DEFAULT_API_URL}catalogs/items").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/get_catalog_items_resp.json"),
    )
    items = await async_api.catalogs.get_catalogs_items(
        country="US", item_ids=["CR123"], language="EN"
    )
    assert len(items.items) == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_get_catalog_items_batch(async_api, helpers):
    batch_id = "595953100599279259-66753b9bb65c46c49bd8503b27fecf9e"
    respx.get(f"{pin.Api.DEFAULT_API_URL}catalogs/items/batch/{batch_id}").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/get_catalog_items_batch_resp.json"),
    )
    batch = await async_api.catalogs.get_catalogs_items_batch(batch_id=batch_id)
    assert batch.batch_id == batch_id


@respx.mock
@pytest.mark.asyncio
async def test_async_perform_items_batch(async_api, helpers):
    respx.post(f"{pin.Api.DEFAULT_API_URL}catalogs/items/batch").respond(
        status_code=200,
        json=helpers.load_data(
            "tests/data/catalogs/perform_operation_item_batch_resp.json"
        ),
    )
    batch = await async_api.catalogs.perform_items_batch(
        operation="UPDATE",
        country="US",
        language="EN",
        items=[
            {
                "item_id": "DS0294-M",
                "attributes": {
                    "ad_link": "https://www.example.com/cat/denim-shirt/item012?utm_source=Pinterest",
                    "additional_image_link": [
                        "https://scene.example.com/image/image_v2.jpg",
                        "https://scene.example.com/image/image_v3.jpg",
                    ],
                    "adult": True,
                    "age_group": "newborn",
                    "availability": "in stock",
                    "average_review_rating": 5,
                    "brand": "Josie’s Denim",
                    "color": "blue",
                    "condition": "new",
                    "custom_label_0": "Best sellers",
                    "custom_label_1": "Summer promotion",
                    "custom_label_2": "Winter sales",
                    "custom_label_3": "Woman dress",
                    "custom_label_4": "Man hat",
                    "description": "Casual fit denim shirt made with the finest quality Japanese denim.",
                    "free_shipping_label": True,
                    "free_shipping_limit": "35 USD",
                    "gender": "unisex",
                    "google_product_category": "Apparel & Accessories > Clothing > Shirts & Tops",
                    "gtin": 3234567890126,
                    "id": "DS0294-L",
                    "image_link": ["https://scene.example.com/image/image.jpg"],
                    "item_group_id": "DS0294",
                    "last_updated_time": 1641483432072,
                    "link": "https://www.example.com/cat/womens-clothing/denim-shirt-0294",
                    "material": "cotton",
                    "min_ad_price": "19.99 USD",
                    "mobile_link": "https://m.example.com/cat/womens-clothing/denim-shirt-0294",
                    "mpn": "PI12345NTEREST",
                    "number_of_ratings": 10,
                    "number_of_reviews": 10,
                    "pattern": "plaid",
                    "price": "24.99 USD",
                    "product_type": "Clothing > Women’s > Shirts > Denim",
                    "sale_price": "14.99 USD",
                    "shipping": "US:CA:Ground:0 USD",
                    "shipping_height": "12 in",
                    "shipping_weight": "3 kg",
                    "shipping_width": "16 in",
                    "size": "M",
                    "size_system": "US",
                    "size_type": "regular",
                    "tax": "US:1025433:6.00:y",
                    "title": "Women’s denim shirt, large",
                },
            }
        ],
    )
    assert batch.batch_id == "595953100599279259-66753b9bb65c46c49bd8503b27fecf9e"
    assert batch.status == "PROCESSING"


@respx.mock
@pytest.mark.asyncio
async def test_async_get_product_group(async_api, helpers):
    product_group_id = "443727193917"
    respx.get(
        f"{pin.Api.DEFAULT_API_URL}catalogs/product_groups/{product_group_id}"
    ).respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/get_product_group_resp.json"),
    )
    pg = await async_api.catalogs.get_product_group(product_group_id=product_group_id)
    assert pg.name == "Most Popular"


@respx.mock
@pytest.mark.asyncio
async def test_async_create_product_group(async_api, helpers):
    respx.post(f"{pin.Api.DEFAULT_API_URL}catalogs/product_groups").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/create_product_group_resp.json"),
    )
    pg = await async_api.catalogs.create_product_group(
        feed_id="2680059592705",
        name="Most Popular",
        filters={
            "any_of": [{"MIN_PRICE": {"inclusion": True, "values": 0, "negated": True}}]
        },
        description="string",
    )
    assert pg.name == "Most Popular"


@respx.mock
@pytest.mark.asyncio
async def test_async_update_product_group(async_api, helpers):
    product_group_id = "443727193917"
    respx.patch(
        f"{pin.Api.DEFAULT_API_URL}catalogs/product_groups/{product_group_id}"
    ).respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/update_product_group_resp.json"),
    )
    pg = await async_api.catalogs.update_product_group(
        product_group_id=product_group_id,
        feed_id="2680059592705",
        name="Most Popular",
        description="string",
        filters={
            "any_of": [{"MIN_PRICE": {"inclusion": True, "values": 0, "negated": True}}]
        },
    )
    assert pg.id == product_group_id


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_product_group(async_api, helpers):
    product_group_id = "443727193917"
    respx.delete(
        f"{pin.Api.DEFAULT_API_URL}catalogs/product_groups/{product_group_id}"
    ).respond(
        status_code=204,
        json={"code": 0, "message": "string"},
    )
    st = await async_api.catalogs.delete_product_group(
        product_group_id=product_group_id
    )
    assert st


@respx.mock
@pytest.mark.asyncio
async def test_async_get_product_group_list(async_api, helpers):
    feed_id = "2680059592705"
    respx.get(f"{pin.Api.DEFAULT_API_URL}catalogs/product_groups").respond(
        status_code=200,
        json=helpers.load_data("tests/data/catalogs/get_product_groups_list_resp.json"),
    )
    pgs = await async_api.catalogs.get_product_group_list(
        feed_id=feed_id,
        page_size=1,
        bookmark="string",
    )
    assert len(pgs.items) == 1
