"""
    Analytics for objects

    Refer:
        user_account: https://developers.pinterest.com/docs/api/v5/#operation/user_account/analytics

"""

from dataclasses import dataclass, field
from typing import Dict, List

from .base import BaseModel


@dataclass
class DailyMetric(BaseModel):
    date: str = field(default=None)
    data_status: str = field(default=None, repr=False)
    metrics: Dict = field(default=None, repr=False)


@dataclass
class UserAccountAnalyticsAll(BaseModel):
    daily_metrics: List[DailyMetric] = field(default=None)
    summary_metrics: Dict = field(default=None, repr=False)


@dataclass
class UserAccountAnalytics(BaseModel):
    all: UserAccountAnalyticsAll = field(default=None)
