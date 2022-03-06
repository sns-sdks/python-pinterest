"""
    Models for media.

    Refer: https://developers.pinterest.com/docs/api/v5/#tag/media
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .base import BaseModel


@dataclass
class MediaUpload(BaseModel):
    media_id: str = field(default=None)
    media_type: str = field(default=None)
    status: str = field(default=None)


@dataclass
class MediaUploadsResponse(BaseModel):
    items: List[MediaUpload] = field(default=None)
    bookmark: Optional[str] = field(default=None)


@dataclass
class RegisterMediaUploadResponse(BaseModel):
    media_id: str = field(default=None)
    media_type: str = field(default=None)
    upload_url: str = field(default=None)
    upload_parameters: Dict[str, str] = field(default=None)
