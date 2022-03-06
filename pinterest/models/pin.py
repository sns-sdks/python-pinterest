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
    width: int = field(default=None)
    height: int = field(default=None)
    url: str = field(default=None)


class Media(BaseModel):
    images: Dict[str, ImageDetail] = field(default=None, repr=False)
    media_type: str = field(default=None)


@dataclass
class Pin(BaseModel):
    id: str = field(default=None)
    created_at: str = field(default=None)
    link: Optional[str] = field(default=None, repr=False)
    title: Optional[str] = field(default=None, repr=False)
    description: Optional[str] = field(default=None, repr=False)
    alt_text: Optional[str] = field(default=None, repr=False)
    board_id: str = field(default=None, repr=False)
    board_section_id: Optional[str] = field(default=None, repr=False)
    board_owner: Owner = field(default=None, repr=False)
    media: Media = field(default=None, repr=False)


@dataclass
class PinsResponse(BaseModel):
    items: List[Pin] = field(default=None)
    bookmark: Optional[str] = field(default=None)
