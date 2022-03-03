"""
   Model for board.

   Refer: https://developers.pinterest.com/docs/api/v5/#tag/boards
"""

from dataclasses import dataclass, field
from typing import List

from .base import BaseModel


@dataclass
class Owner(BaseModel):
    username: str = field(default=None)


@dataclass
class Board(BaseModel):
    id: str = field(default=None)
    name: str = field(default=None)
    description: str = field(default=None, repr=False)
    owner: Owner = field(default=None, repr=False)
    privacy: str = field(default=None, repr=False)


@dataclass
class BoardsResponse(BaseModel):
    items: List[Board] = field(default=None)
    bookmark: str = field(default=None)
