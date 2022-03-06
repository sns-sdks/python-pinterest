"""
    Some common models.
"""

from dataclasses import dataclass, field
from typing import Optional

from .base import BaseModel


@dataclass
class Owner(BaseModel):
    username: Optional[str] = field(default=None)
