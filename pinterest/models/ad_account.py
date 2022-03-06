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
