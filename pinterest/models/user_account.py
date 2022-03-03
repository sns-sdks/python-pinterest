"""
   Model class for user account.

   Refer: https://developers.pinterest.com/docs/api/v5/#tag/user_account
"""

from dataclasses import dataclass, field

from .base import BaseModel


@dataclass
class UserAccount(BaseModel):
    username: str = field(default=None)
    account_type: str = field(default=None)
    profile_image: str = field(default=None, repr=False)
    website_url: str = field(default=None, repr=False)
