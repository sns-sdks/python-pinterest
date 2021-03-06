"""
    Model for Catalogs

    Refer: https://developers.pinterest.com/docs/api/v5/#tag/catalogs
"""

from dataclasses import dataclass, field
from typing import List, Optional

from .base import BaseModel


@dataclass
class CatalogsFeedCredentials(BaseModel):
    password: Optional[str] = field(default=None)
    username: Optional[str] = field(default=None)


@dataclass
class CatalogsProcessingSchedule(BaseModel):
    time: Optional[str] = field(default=None)
    timezone: Optional[str] = field(default=None)


@dataclass
class CatalogFeed(BaseModel):
    id: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None, repr=False)
    country: Optional[str] = field(default=None)
    default_availability: Optional[str] = field(default=None, repr=False)
    default_currency: Optional[str] = field(default=None, repr=False)
    format: Optional[str] = field(default=None, repr=False)
    locale: Optional[str] = field(default=None, repr=False)
    location: Optional[str] = field(default=None, repr=False)
    credentials: Optional[CatalogsFeedCredentials] = field(default=None, repr=False)
    preferred_processing_schedule: Optional[CatalogsProcessingSchedule] = field(
        default=None, repr=False
    )
    created_at: Optional[str] = field(default=None, repr=False)
    updated_at: Optional[str] = field(default=None, repr=False)
    status: Optional[str] = field(default=None, repr=False)


@dataclass
class CatalogFeedsResponse(BaseModel):
    items: List[CatalogFeed] = field(default=None)
    bookmark: Optional[str] = field(default=None)


@dataclass
class CatalogsFeedIngestionErrors(BaseModel):
    image_download_error: Optional[int] = field(default=None)
    image_download_connection_timeout: Optional[int] = field(default=None, repr=False)
    image_format_unrecognize: Optional[int] = field(default=None, repr=False)
    line_level_internal_error: Optional[int] = field(default=None, repr=False)
    indexed_product_count_large_delta_failure: Optional[int] = field(
        default=None, repr=False
    )


@dataclass
class CatalogsFeedIngestionInfo(BaseModel):
    in_stock: Optional[int] = field(default=None)
    out_of_stock: Optional[int] = field(default=None)
    preorder: Optional[int] = field(default=None)


@dataclass
class CatalogsFeedIngestionDetails(BaseModel):
    errors: Optional[CatalogsFeedIngestionErrors] = field(default=None, repr=False)
    info: Optional[CatalogsFeedIngestionInfo] = field(default=None)


@dataclass
class CatalogsFeedProductCounts(BaseModel):
    original: Optional[int] = field(default=None)
    in_stock: Optional[int] = field(default=None)
    out_of_stock: Optional[int] = field(default=None)
    preorder: Optional[int] = field(default=None)
    total: Optional[int] = field(default=None)


@dataclass
class CatalogsFeedValidationErrors(BaseModel):
    fetch_error: Optional[int] = field(default=None)
    fetch_inactive_feed_error: Optional[int] = field(default=None)
    encoding_error: Optional[int] = field(default=None)
    delimiter_error: Optional[int] = field(default=None)
    required_columns_missing: Optional[int] = field(default=None)
    image_link_invalid: Optional[int] = field(default=None)
    itemid_missing: Optional[int] = field(default=None)
    title_missing: Optional[int] = field(default=None)
    description_missing: Optional[int] = field(default=None)
    product_category_invalid: Optional[int] = field(default=None)
    product_link_missing: Optional[int] = field(default=None)
    image_link_missing: Optional[int] = field(default=None)
    availability_invalid: Optional[int] = field(default=None)
    product_price_invalid: Optional[int] = field(default=None)
    link_format_invalid: Optional[int] = field(default=None)
    parse_line_error: Optional[int] = field(default=None)
    adwords_format_invalid: Optional[int] = field(default=None)
    product_category_missing: Optional[int] = field(default=None)
    internal_service_error: Optional[int] = field(default=None)
    no_verified_domain: Optional[int] = field(default=None)
    adult_invalid: Optional[int] = field(default=None)
    invalid_domain: Optional[int] = field(default=None)
    feed_length_too_long: Optional[int] = field(default=None)
    link_length_too_long: Optional[int] = field(default=None)
    malformed_xml: Optional[int] = field(default=None)
    redirect_invalid: Optional[int] = field(default=None)
    price_missing: Optional[int] = field(default=None)
    feed_too_small: Optional[int] = field(default=None)
    condition_invalid: Optional[int] = field(default=None)
    shopify_no_products: Optional[int] = field(default=None)
    max_items_per_item_group_exceeded: Optional[int] = field(default=None)
    item_main_image_download_failure: Optional[int] = field(default=None)
    pinjoin_content_unsafe: Optional[int] = field(default=None)
    blocklisted_image_signature: Optional[int] = field(default=None)


@dataclass
class CatalogsFeedValidationWarnings(BaseModel):
    title_length_too_long: Optional[int] = field(default=None)
    description_length_too_long: Optional[int] = field(default=None)
    gender_invalid: Optional[int] = field(default=None)
    age_group_invalid: Optional[int] = field(default=None)
    size_type_invalid: Optional[int] = field(default=None)
    link_format_warning: Optional[int] = field(default=None)
    duplicate_products: Optional[int] = field(default=None)
    duplicate_links: Optional[int] = field(default=None)
    sales_price_invalid: Optional[int] = field(default=None)
    product_category_depth_warning: Optional[int] = field(default=None)
    adwords_same_as_link: Optional[int] = field(default=None)
    duplicate_headers: Optional[int] = field(default=None)
    fetch_same_signature: Optional[int] = field(default=None)
    adwords_format_warning: Optional[int] = field(default=None)
    additional_image_link_warning: Optional[int] = field(default=None)
    image_link_warning: Optional[int] = field(default=None)
    shipping_invalid: Optional[int] = field(default=None)
    tax_invalid: Optional[int] = field(default=None)
    shipping_weight_invalid: Optional[int] = field(default=None)
    expiration_date_invalid: Optional[int] = field(default=None)
    availability_date_invalid: Optional[int] = field(default=None)
    sale_date_invalid: Optional[int] = field(default=None)
    weight_unit_invalid: Optional[int] = field(default=None)
    is_bundle_invalid: Optional[int] = field(default=None)
    updated_time_invalid: Optional[int] = field(default=None)
    custom_label_length_too_long: Optional[int] = field(default=None)
    product_type_length_too_long: Optional[int] = field(default=None)
    too_many_additional_image_links: Optional[int] = field(default=None)
    multipack_invalid: Optional[int] = field(default=None)
    indexed_product_count_large_delta: Optional[int] = field(default=None)
    item_additional_image_download_failure: Optional[int] = field(default=None)
    optional_product_category_missing: Optional[int] = field(default=None)
    optional_product_category_invalid: Optional[int] = field(default=None)
    optional_condition_missing: Optional[int] = field(default=None)
    optional_condition_invalid: Optional[int] = field(default=None)
    ios_deep_link_invalid: Optional[int] = field(default=None)
    android_deep_link_invalid: Optional[int] = field(default=None)
    availability_normalized: Optional[int] = field(default=None)
    condition_normalized: Optional[int] = field(default=None)
    gender_normalized: Optional[int] = field(default=None)
    size_type_normalized: Optional[int] = field(default=None)
    age_group_normalized: Optional[int] = field(default=None)
    utm_source_auto_corrected: Optional[int] = field(default=None)
    country_does_not_map_to_currency: Optional[int] = field(default=None)
    min_ad_price_invalid: Optional[int] = field(default=None)


@dataclass
class CatalogsFeedValidationDetails(BaseModel):
    errors: Optional[CatalogsFeedValidationErrors] = field(default=None)
    warnings: Optional[CatalogsFeedValidationWarnings] = field(default=None)


@dataclass
class CatalogFeedProcessResult(BaseModel):
    id: Optional[str] = field(default=None)
    status: Optional[str] = field(default=None)
    created_at: Optional[str] = field(default=None, repr=False)
    updated_at: Optional[str] = field(default=None, repr=False)
    ingestion_details: Optional[CatalogsFeedIngestionDetails] = field(
        default=None, repr=False
    )
    product_counts: Optional[CatalogsFeedProductCounts] = field(
        default=None, repr=False
    )
    validation_details: Optional[CatalogsFeedValidationDetails] = field(
        default=None, repr=False
    )


@dataclass
class CatalogFeedProcessResultsResponse(BaseModel):
    items: Optional[List[CatalogFeedProcessResult]] = field(default=None)
    bookmark: Optional[str] = field(default=None)


@dataclass
class CatalogItemAttributes(BaseModel):
    ad_link: Optional[str] = field(default=None)
    additional_image_link: Optional[List[str]] = field(default=None)
    adult: Optional[bool] = field(default=None)
    age_group: Optional[str] = field(default=None)
    availability: Optional[str] = field(default=None)
    average_review_rating: Optional[int] = field(default=None)
    brand: Optional[str] = field(default=None)
    color: Optional[str] = field(default=None)
    condition: Optional[str] = field(default=None)
    custom_label_0: Optional[str] = field(default=None)
    custom_label_1: Optional[str] = field(default=None)
    custom_label_2: Optional[str] = field(default=None)
    custom_label_3: Optional[str] = field(default=None)
    custom_label_4: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    free_shipping_label: Optional[bool] = field(default=None)
    free_shipping_limit: Optional[str] = field(default=None)
    gender: Optional[str] = field(default=None)
    google_product_category: Optional[str] = field(default=None)
    gtin: Optional[int] = field(default=None)
    id: Optional[str] = field(default=None)
    image_link: Optional[List[str]] = field(default=None)
    item_group_id: Optional[str] = field(default=None)
    last_updated_time: Optional[int] = field(default=None)
    link: Optional[str] = field(default=None)
    material: Optional[str] = field(default=None)
    min_ad_price: Optional[str] = field(default=None)
    mobile_link: Optional[str] = field(default=None)
    mpn: Optional[str] = field(default=None)
    number_of_ratings: Optional[int] = field(default=None)
    number_of_reviews: Optional[int] = field(default=None)
    pattern: Optional[str] = field(default=None)
    price: Optional[str] = field(default=None)
    product_type: Optional[str] = field(default=None)
    sale_price: Optional[str] = field(default=None)
    shipping: Optional[str] = field(default=None)
    shipping_height: Optional[str] = field(default=None)
    shipping_weight: Optional[str] = field(default=None)
    shipping_width: Optional[str] = field(default=None)
    size: Optional[str] = field(default=None)
    size_system: Optional[str] = field(default=None)
    size_type: Optional[str] = field(default=None)
    tax: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)


@dataclass
class CatalogItem(BaseModel):
    item_id: Optional[str] = field(default=None)
    attributes: Optional[CatalogItemAttributes] = field(default=None)


@dataclass
class CatalogItemsResponse(BaseModel):
    items: Optional[List[CatalogItem]] = field(default=None)


@dataclass
class CatalogItemValidationEvent(BaseModel):
    attribute: Optional[str] = field(default=None)
    code: Optional[int] = field(default=None)
    message: Optional[str] = field(default=None)


@dataclass
class CatalogItemProcessingRecord(BaseModel):
    item_id: Optional[str] = field(default=None)
    errors: Optional[List[CatalogItemValidationEvent]] = field(default=None)
    warnings: Optional[List[CatalogItemValidationEvent]] = field(default=None)
    status: Optional[str] = field(default=None)


@dataclass
class CatalogItemProcessingRecordResponse(BaseModel):
    items: Optional[List[CatalogItemProcessingRecord]] = field(default=None)
    batch_id: Optional[str] = field(default=None)
    created_time: Optional[str] = field(default=None)
    completed_time: Optional[str] = field(default=None)
    status: Optional[str] = field(default=None)


@dataclass
class CatalogProductGroup(BaseModel):
    id: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    filters: Optional[dict] = field(default=None)
    type: Optional[str] = field(default=None)
    status: Optional[str] = field(default=None)
    feed_id: Optional[str] = field(default=None)
    created_at: Optional[str] = field(default=None)
    updated_at: Optional[str] = field(default=None)


@dataclass
class CatalogProductGroupsResponse(BaseModel):
    items: Optional[List[CatalogProductGroup]] = field(default=None)
    bookmark: Optional[str] = field(default=None)
