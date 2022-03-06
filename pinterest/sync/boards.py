"""
    Boards endpoints implementation.
"""
from typing import Optional, Union

from pinterest.base_endpoint import Endpoint
from pinterest.exceptions import PinterestException
from pinterest.models import (
    Board,
    BoardsResponse,
    BoardSection,
    BoardSectionsResponse,
    PinsResponse,
)


class BoardsEndpoint(Endpoint):
    def list(
        self,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        privacy: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[BoardsResponse, dict]:
        """
        Get a list of the boards owned by the "operation user_account" + group boards where this account is a collaborator

        :param page_size: Maximum number of items to include in a single page of the response. [1..100]
        :param bookmark: Cursor used to fetch the next page of items
        :param privacy: Privacy setting for a board.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Boards Response
        """

        params = {"page_size": page_size}
        if bookmark is not None:
            params["bookmark"] = bookmark
        if privacy is not None:
            params["privacy"] = privacy

        resp = self._get(url=f"boards", params=params)
        data = self._parse_response(response=resp)
        return data if return_json else BoardsResponse.new_from_json_dict(data=data)

    def get(self, board_id: str, return_json: bool = False) -> Union[Board, dict]:
        """
        Get a board owned by the operation user_account - or a group board that has been shared with this account.

        :param board_id: Unique identifier of a board.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Board data.
        """

        resp = self._get(url=f"boards/{board_id}")
        data = self._parse_response(response=resp)
        return data if return_json else Board.new_from_json_dict(data=data)

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
        resp = self._post(url="boards", json=data)
        data = self._parse_response(response=resp)
        return data if return_json else Board.new_from_json_dict(data=data)

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

        resp = self._patch(url=f"boards/{board_id}", json=data)
        data = self._parse_response(response=resp)
        return data if return_json else Board.new_from_json_dict(data=data)

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

    def list_pins(
        self,
        board_id: str,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[PinsResponse, dict]:
        """
        Get a list of the Pins on a board owned by the "operation user_account" -
        or on a group board that has been shared with this account.

        :param board_id: Unique identifier of a board.
        :param page_size: Maximum number of items to include in a single page of the response. [1..100]
        :param bookmark: Cursor used to fetch the next page of items.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Pins data.
        """
        params = {"page_size": page_size}
        if bookmark is not None:
            params["bookmark"] = bookmark

        resp = self._get(url=f"boards/{board_id}/pins", params=params)
        data = self._parse_response(response=resp)
        return data if return_json else PinsResponse.new_from_json_dict(data=data)

    def list_sections(
        self,
        board_id: str,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[BoardSectionsResponse, dict]:
        """
        Get a list of all board sections from a board owned by the "operation user_account" -
        or a group board that has been shared with this account.

        :param board_id: Unique identifier of a board.
        :param page_size: Maximum number of items to include in a single page of the response. [1~100].
        :param bookmark: Cursor used to fetch the next page of items
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Board sections
        """
        params = {"page_size": page_size}
        if bookmark is not None:
            params["bookmark"] = bookmark

        resp = self._get(
            url=f"boards/{board_id}/sections",
            params=params,
        )
        data = self._parse_response(response=resp)
        return (
            data if return_json else BoardSectionsResponse.new_from_json_dict(data=data)
        )

    def create_section(
        self, board_id, name: str, return_json: bool = False
    ) -> Union[BoardSection, dict]:
        """
        Create a board section on a board owned by the "operation user_account" -
        or on a group board that has been shared with this account.

        :param board_id: Unique identifier of a board.
        :param name: Name for section, length [1...180]
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Board Section data.
        """

        resp = self._post(url=f"boards/{board_id}/sections", json={"name": name})
        data = self._parse_response(response=resp)
        return data if return_json else BoardSection.new_from_json_dict(data=data)

    def update_section(
        self, board_id, section_id, name: str, return_json: bool = False
    ) -> Union[BoardSection, dict]:
        """
        Update a board section on a board owned by the "operation user_account" -
        or on a group board that has been shared with this account.

        :param board_id: Unique identifier of a board.
        :param section_id: Unique identifier of a board section.
        :param name: New name for section, length [1...180]
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Board Section data.
        """
        resp = self._patch(
            url=f"boards/{board_id}/sections/{section_id}", json={"name": name}
        )
        data = self._parse_response(response=resp)
        return data if return_json else BoardSection.new_from_json_dict(data=data)

    def delete_section(self, board_id, section_id: str) -> bool:
        """
        Delete a board section on a board owned by the "operation user_account" -
        or on a group board that has been shared with this account.

        :param board_id: Unique identifier of a board.
        :param section_id: Unique identifier of a board section.
        :return: delete status
        """
        resp = self._delete(url=f"boards/{board_id}/sections/{section_id}")
        if resp.is_success:
            return True
        self._parse_response(response=resp)

    def list_section_pins(
        self,
        board_id,
        section_id: str,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[PinsResponse, dict]:
        """
        Get a list of the Pins on a board section of a board owned by the "operation user_account" -
        or on a group board that has been shared with this account.

        :param board_id: Unique identifier of a board.
        :param section_id: Unique identifier of a board section.
        :param page_size: Maximum number of items to include in a single page of the response. [1..100].
        :param bookmark: Cursor used to fetch the next page of items.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Pins data.
        """
        params = {"page_size": page_size}
        if bookmark is not None:
            params["bookmark"] = bookmark

        resp = self._get(
            url=f"boards/{board_id}/sections/{section_id}/pins",
            params=params,
        )
        data = self._parse_response(response=resp)
        return data if return_json else PinsResponse.new_from_json_dict(data=data)
