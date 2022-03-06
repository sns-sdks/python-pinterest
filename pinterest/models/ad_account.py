"""
    Models for ad accounts.

    Refer: https://developers.pinterest.com/docs/api/v5/#tag/ad_accounts
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .base import BaseModel


@dataclass
class AdAccount(BaseModel):
    id: str = field(default=None)
    name: str = field(default=None)
    owner: str = field(default=None)
    country: str = field(default=None)
    currency: str = field(default=None)


@dataclass
class AdAccountsResponse(BaseModel):
    items: List[AdAccount] = field(default=None)
    bookmark: Optional[str] = field(default=None)


@dataclass
class TrackingURL(BaseModel):
    impression: Optional[List[str]] = field(default=None)
    click: Optional[List[str]] = field(default=None, repr=False)
    engagement: Optional[List[str]] = field(default=None, repr=False)
    buyable_button: Optional[List[str]] = field(default=None, repr=False)
    audience_verification: Optional[List[str]] = field(default=None, repr=False)


@dataclass
class Campaign(BaseModel):
    id: str = field(default=None)
    ad_account_id: str = field(default=None)
    name: str = field(default=None)
    status: str = field(default=None)
    lifetime_spend_cap: int = field(default=None, repr=False)
    daily_spend_cap: int = field(default=None, repr=False)
    order_line_id: str = field(default=None, repr=False)
    tracking_urls: TrackingURL = field(default=None, repr=False)
    start_time: int = field(default=None, repr=False)
    end_time: int = field(default=None, repr=False)
    objective_type: str = field(default=None, repr=False)
    created_time: int = field(default=None, repr=False)
    updated_time: int = field(default=None, repr=False)
    type: str = field(default=None, repr=False)


@dataclass
class CampaignsResponse(BaseModel):
    items: List[Campaign] = field(default=None)
    bookmark: Optional[str] = field(default=None)


@dataclass
class AdGroup(BaseModel):
    id: str = field(default=None)
    ad_account_id: str = field(default=None, repr=False)
    campaign_id: str = field(default=None, repr=False)
    name: str = field(default=None)
    status: str = field(default=None)
    budget_in_micro_currency: int = field(default=None, repr=False)
    bid_in_micro_currency: int = field(default=None, repr=False)
    budget_type: str = field(default=None, repr=False)
    start_time: int = field(default=None, repr=False)
    end_time: int = field(default=None, repr=False)
    targeting_spec: Dict = field(default=None, repr=False)
    lifetime_frequency_cap: Optional[int] = field(default=None, repr=False)
    tracking_urls: Optional[TrackingURL] = field(default=None, repr=False)
    auto_targeting_enabled: Optional[bool] = field(default=None, repr=False)
    placement_group: Optional[str] = field(default=None, repr=False)
    pacing_delivery_type: Optional[str] = field(default=None, repr=False)
    conversion_learning_mode_type: Optional[str] = field(default=None, repr=False)
    summary_status: Optional[str] = field(default=None, repr=False)
    feed_profile_id: Optional[str] = field(default=None, repr=False)
    billable_event: Optional[str] = field(default=None, repr=False)
    type: Optional[str] = field(default=None, repr=False)
    created_time: Optional[int] = field(default=None, repr=False)
    updated_time: Optional[int] = field(default=None, repr=False)


@dataclass
class AdGroupsResponse(BaseModel):
    items: List[AdGroup] = field(default=None)
    bookmark: Optional[str] = field(default=None)


@dataclass
class Ad(BaseModel):
    id: Optional[str] = field(default=None)
    type: Optional[str] = field(default=None)
    status: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None, repr=False)
    ad_group_id: Optional[str] = field(default=None, repr=False)
    campaign_id: Optional[str] = field(default=None, repr=False)
    android_deep_link: Optional[str] = field(default=None, repr=False)
    carousel_android_deep_links: Optional[List[str]] = field(default=None, repr=False)
    carousel_destination_urls: Optional[List[str]] = field(default=None, repr=False)
    carousel_ios_deep_links: Optional[List[str]] = field(default=None, repr=False)
    click_tracking_url: Optional[str] = field(default=None, repr=False)
    creative_type: Optional[str] = field(default=None, repr=False)
    destination_url: Optional[str] = field(default=None, repr=False)
    ios_deep_link: Optional[str] = field(default=None, repr=False)
    is_pin_deleted: Optional[bool] = field(default=None, repr=False)
    is_removable: Optional[bool] = field(default=None, repr=False)
    pin_id: Optional[str] = field(default=None, repr=False)
    tracking_urls: Optional[TrackingURL] = field(default=None, repr=False)
    view_tracking_url: Optional[str] = field(default=None, repr=False)
    collection_items_destination_url_template: Optional[str] = field(
        default=None, repr=False
    )
    created_time: Optional[str] = field(default=None, repr=False)
    rejected_reasons: Optional[List[str]] = field(default=None, repr=False)
    rejection_labels: Optional[List[str]] = field(default=None, repr=False)
    review_status: Optional[str] = field(default=None, repr=False)
    updated_time: Optional[str] = field(default=None, repr=False)
    summary_status: Optional[str] = field(default=None, repr=False)


@dataclass
class AdsResponse(BaseModel):
    items: List[Ad] = field(default=None)
    bookmark: Optional[str] = field(default=None)
