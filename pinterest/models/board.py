"""
   Model for board.

   Refer: https://developers.pinterest.com/docs/api/v5/#tag/boards
"""

from dataclasses import dataclass, field
from typing import List, Optional

from .base import BaseModel
from .common import Owner


@dataclass
class Board(BaseModel):
    id: str = field(default=None)
    name: str = field(default=None)
    description: Optional[str] = field(default=None, repr=False)
    owner: Owner = field(default=None, repr=False)
    privacy: str = field(default=None, repr=False)


@dataclass
class BoardsResponse(BaseModel):
    items: List[Board] = field(default=None)
    bookmark: Optional[str] = field(default=None)


@dataclass
class BoardSection(BaseModel):
    id: str = field(default=None)
    name: str = field(default=None)


@dataclass
class BoardSectionsResponse(BaseModel):
    items: List[BoardSection] = field(default=None)
    bookmark: Optional[str] = field(default=None)
