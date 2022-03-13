"""
    Model for pin.

   Refer: https://developers.pinterest.com/docs/api/v5/#tag/pins
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .base import BaseModel
from .common import Owner


@dataclass
class ImageDetail(BaseModel):
    width: Optional[int] = field(default=None)
    height: Optional[int] = field(default=None)
    url: Optional[str] = field(default=None)


class Media(BaseModel):
    images: Optional[Dict[str, ImageDetail]] = field(default=None, repr=False)
    media_type: Optional[str] = field(default=None)


@dataclass
class Pin(BaseModel):
    id: Optional[str] = field(default=None)
    created_at: Optional[str] = field(default=None)
    link: Optional[str] = field(default=None, repr=False)
    title: Optional[str] = field(default=None, repr=False)
    description: Optional[str] = field(default=None, repr=False)
    alt_text: Optional[str] = field(default=None, repr=False)
    board_id: Optional[str] = field(default=None, repr=False)
    board_section_id: Optional[str] = field(default=None, repr=False)
    board_owner: Optional[Owner] = field(default=None, repr=False)
    media: Optional[Media] = field(default=None, repr=False)


@dataclass
class PinsResponse(BaseModel):
    items: List[Pin] = field(default=None)
    bookmark: Optional[str] = field(default=None)
