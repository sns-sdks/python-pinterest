"""
    Pins endpoints implementation.
"""
from typing import Optional, Union

from pinterest.base_endpoint import AsyncEndpoint
from pinterest.models import Pin, Analytics
from pinterest.utils.params import enf_comma_separated


class PinsAsyncEndpoint(AsyncEndpoint):
    async def create(
        self,
        board_id: str,
        media_source: dict,
        link: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        dominant_color: Optional[str] = None,
        alt_text: Optional[str] = None,
        board_section_id: Optional[str] = None,
        parent_pin_id: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[Pin, dict]:
        """
        Create a Pin on a board or board section owned by the "operation user_account".

        :param board_id: The board to which this Pin belongs.
        :param media_source: Pin media source.
            Params detail refer: https://developers.pinterest.com/docs/api/v5/#operation/pins/create
        :param link: Link for the pin.
        :param title: Title for the pin.
        :param description: Description for the pin.
        :param dominant_color: Dominant pin color. Hex number, e.g. "#6E7874".
        :param alt_text: Alt_text for the pin.
        :param board_section_id: The board section to which this Pin belongs.
        :param parent_pin_id: The source pin id if this pin was saved from another pin.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Pin data
        """
        data = {
            "board_id": board_id,
            "media_source": media_source,
            "link": link,
            "title": title,
            "dominant_color": dominant_color,
            "alt_text": alt_text,
            "board_section_id": board_section_id,
            "parent_pin_id": parent_pin_id,
        }
        resp = await self._post(url=f"pins", json=data)
        data = self._parse_response(response=resp)
        return data if return_json else Pin.new_from_json_dict(data=data)

    async def get(
        self,
        pin_id: str,
        ad_account_id: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[Pin, dict]:
        """
        Get a Pin owned by the "operation user_account" - or on a group board that has been shared with this account.

        :param pin_id: Unique identifier of a Pin.
        :param ad_account_id: Unique identifier of an ad account.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Pin data.
        """
        params = {"ad_account_id": ad_account_id} if ad_account_id else None
        resp = await self._get(
            url=f"pins/{pin_id}",
            params=params,
        )
        data = self._parse_response(response=resp)
        return data if return_json else Pin.new_from_json_dict(data=data)

    async def delete(self, pin_id: str) -> bool:
        """
        Delete a Pins owned by the "operation user_account" -
        or on a group board that has been shared with this account.

        :param pin_id: Unique identifier of a Pin.
        :return: delete status
        """
        resp = await self._delete(url=f"pins/{pin_id}")
        if resp.is_success:
            return True
        self._parse_response(response=resp)

    async def save(
        self, pin_id: str, board_id: Optional[str] = None, return_json: bool = False
    ) -> Union[Pin, dict]:
        """
        Save a pin on a board owned by the "operation user_account".

        :param pin_id: Unique identifier of a Pin.
        :param board_id: Unique identifier of the board to which the pin will be saved.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Pin data.
        """
        params = {"board_id": board_id} if board_id else None
        resp = await self._post(url=f"pins/{pin_id}/save", json=params)
        data = self._parse_response(response=resp)
        return data if return_json else Pin.new_from_json_dict(data=data)

    async def get_analytics(
        self,
        pin_id: str,
        start_date: str,
        end_date: str,
        metric_types: Union[str, list, tuple],
        app_types: Optional[str] = None,
        split_field: Optional[str] = None,
        ad_account_id: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[Analytics, dict]:
        """
        Get analytics for a Pin owned by the "operation user_account" -
        or on a group board that has been shared with this account.

        :param pin_id: Unique identifier of a Pin.
        :param start_date: Metric report start date (UTC). Format: YYYY-MM-DD
        :param end_date: Metric report end date (UTC). Format: YYYY-MM-DD
        :param metric_types: Pin metric types to get data for..
        :param app_types: Apps or devices to get data for, default is all.
        :param split_field: How to split the data into groups. Not including this param means data won't be split.
        :param ad_account_id: Unique identifier of an ad account.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Pin analytics data.
        """

        params = {
            "start_date": start_date,
            "end_date": end_date,
            "metric_types": enf_comma_separated(
                field="metric_types", value=metric_types
            ),
        }
        if app_types is not None:
            params["app_types"] = app_types
        if split_field is not None:
            params["split_field"] = split_field
        if ad_account_id is not None:
            params["ad_account_id"] = ad_account_id

        resp = await self._get(
            url=f"pins/{pin_id}/analytics",
            params=params,
        )
        data = self._parse_response(response=resp)
        return data if return_json else Analytics.new_from_json_dict(data=data)
