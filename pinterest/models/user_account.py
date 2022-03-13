"""
   Model class for user account.

   Refer: https://developers.pinterest.com/docs/api/v5/#tag/user_account
"""

from dataclasses import dataclass, field
from typing import Optional

from .base import BaseModel


@dataclass
class UserAccount(BaseModel):
    username: Optional[str] = field(default=None)
    account_type: Optional[str] = field(default=None)
    profile_image: Optional[str] = field(default=None, repr=False)
    website_url: Optional[str] = field(default=None, repr=False)
