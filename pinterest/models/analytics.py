"""
    Analytics for objects

    Refer:
        user_account: https://developers.pinterest.com/docs/api/v5/#operation/user_account/analytics
"""

from dataclasses import dataclass, field
from typing import Optional, List

from .base import BaseModel


@dataclass
class DailyMetric(BaseModel):
    date: Optional[str] = field(default=None)
    data_status: Optional[str] = field(default=None, repr=False)
    metrics: Optional[dict] = field(default=None, repr=False)


@dataclass
class AnalyticsAll(BaseModel):
    daily_metrics: Optional[List[DailyMetric]] = field(default=None)
    summary_metrics: Optional[dict] = field(default=None, repr=False)


@dataclass
class Analytics(BaseModel):
    all: Optional[AnalyticsAll] = field(default=None)
