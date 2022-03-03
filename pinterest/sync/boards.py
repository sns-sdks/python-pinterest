"""
    Boards endpoints implementation.
"""
from typing import Optional, Union

from pinterest.base_endpoint import Endpoint
from pinterest.models import Board, BoardsResponse
from pinterest.exceptions import PinterestException


class BoardsEndpoint(Endpoint):
    def list(
        self,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        privacy: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[BoardsResponse, dict]:
        """
        :param page_size:
        :param bookmark:
        :param privacy:
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Boards Response
        """

        params = {"page_size": page_size}
        if bookmark:
            params["bookmark"] = bookmark
        if privacy:
            params["privacy"] = privacy

        resp = self._get(
            url=f"boards",
            params=params,
        )
        data = self._parse_response(response=resp)
        if return_json:
            return data
        else:
            return BoardsResponse.new_from_json_dict(data=data)

    def get(self, board_id: str, return_json: bool = False) -> Union[Board, dict]:
        """
        :param board_id: Unique identifier of a board.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Board data.
        """

        resp = self._get(url=f"boards/{board_id}")
        data = self._parse_response(response=resp)
        if return_json:
            return data
        else:
            return Board.new_from_json_dict(data=data)

    def create(
        self,
        name: str,
        description: Optional[str] = None,
        privacy: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[Board, dict]:
        """
        Create a board owned by the "operation user_account".

        :param name: Name for the board.
        :param description: Description for the board.
        :param privacy: Privacy setting for a board. Learn more about secret boards and protected boards
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Board data.
        """
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if privacy is not None:
            data["privacy"] = privacy
        resp = self._post(
            url="boards",
            json=data,
        )
        data = self._parse_response(response=resp)
        if return_json:
            return data
        else:
            return Board.new_from_json_dict(data=data)

    def update(
        self,
        board_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        privacy: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[Board, dict]:
        """
        Update a board owned by the "operating user_account".

        :param board_id: Unique identifier of a board.
        :param name: New name for board.
        :param description: New description for board.
        :param privacy: New privacy for board.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Board data.
        """

        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if privacy is not None:
            data["privacy"] = privacy

        if not data:
            raise PinterestException(
                code=-1, message="Update board need one of name,description,privacy"
            )

        resp = self._patch(
            url=f"boards/{board_id}",
            json=data,
        )
        data = self._parse_response(response=resp)
        if return_json:
            return data
        else:
            return Board.new_from_json_dict(data=data)

    def delete(self, board_id: str) -> bool:
        """
        Delete a board owned by the "operation user_account".

        :param board_id: Unique identifier of a board.
        :return: delete status
        """
        resp = self._delete(url=f"boards/{board_id}")
        if resp.is_success:
            return True
        self._parse_response(response=resp)
