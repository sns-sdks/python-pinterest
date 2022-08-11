"""
    User Account endpoints implementation.
"""
from typing import Optional, Union

from pinterest.base_endpoint import Endpoint
from pinterest.models import UserAccount, Analytics, TopPinsAnalytics
from pinterest.utils.params import enf_comma_separated


class UserAccountEndpoint(Endpoint):
    def get(
        self, ad_account_id: Optional[str] = None, return_json: bool = False
    ) -> Union[UserAccount, dict]:
        """
        Get account information for the "operation user_account"

        :param ad_account_id: Unique identifier of an ad account.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: User Account data.
        """

        params = {"ad_account_id": ad_account_id} if ad_account_id else None
        resp = self._get(
            url="user_account",
            params=params,
        )
        data = self._parse_response(response=resp)
        return data if return_json else UserAccount.new_from_json_dict(data=data)

    def get_analytics(
        self,
        start_date: str,
        end_date: str,
        from_claimed_content: str = "BOTH",
        pin_format: str = "ALL",
        app_types: str = "ALL",
        metric_types: Optional[Union[str, list, tuple]] = None,
        split_field: str = "NO_SPLIT",
        ad_account_id: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[Analytics, dict]:
        """
        Get analytics for the "operation user_account"

        :param start_date: Metric report start date (UTC). Format: YYYY-MM-DD
        :param end_date: Metric report end date (UTC). Format: YYYY-MM-DD
        :param from_claimed_content: Filter on Pins that match your claimed domain.
        :param pin_format: Pin formats to get data for, default is all.
        :param app_types: Apps or devices to get data for, default is all.
        :param metric_types: Metric types to get data for, default is all.
        :param split_field: How to split the data into groups. Not including this param means data won't be split.
        :param ad_account_id: Unique identifier of an ad account.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: User Account Analytics data.
        """

        params = {
            "start_date": start_date,
            "end_date": end_date,
            "from_claimed_content": from_claimed_content,
            "pin_format": pin_format,
            "app_types": app_types,
            "split_field": split_field,
        }
        if metric_types:
            params["metric_types"] = enf_comma_separated(
                field="metric_types", value=metric_types
            )
        if ad_account_id:
            params["ad_account_id"] = ad_account_id
        resp = self._get(
            url=f"user_account/analytics",
            params=params,
        )
        data = self._parse_response(response=resp)
        return data if return_json else Analytics.new_from_json_dict(data=data)

    def _get_top_analytics(
        self,
        url: str,
        start_date: str,
        end_date: str,
        sort_by: str,
        from_claimed_content: str = "BOTH",
        pin_format: str = "ALL",
        app_types: str = "ALL",
        metric_types: Optional[Union[str, list, tuple]] = None,
        num_of_pins: int = 10,
        created_in_last_n_days: Optional[int] = None,
        ad_account_id: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[TopPinsAnalytics, dict]:
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "sort_by": sort_by,
            "from_claimed_content": from_claimed_content,
            "pin_format": pin_format,
            "app_types": app_types,
            "num_of_pins": num_of_pins,
        }
        if metric_types:
            params["metric_types"] = enf_comma_separated(
                field="metric_types", value=metric_types
            )
        if created_in_last_n_days:
            params["created_in_last_n_days"] = created_in_last_n_days
        if ad_account_id:
            params["ad_account_id"] = ad_account_id

        resp = self._get(
            url=url,
            params=params,
        )
        data = self._parse_response(response=resp)
        return data if return_json else TopPinsAnalytics.new_from_json_dict(data=data)

    def get_top_pins_analytics(
        self,
        start_date: str,
        end_date: str,
        sort_by: str,
        from_claimed_content: str = "BOTH",
        pin_format: str = "ALL",
        app_types: str = "ALL",
        metric_types: Optional[Union[str, list, tuple]] = None,
        num_of_pins: int = 10,
        created_in_last_n_days: Optional[int] = None,
        ad_account_id: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[dict]:
        """
        Gets analytics data about a user's top pins (limited to the top 50).

        :param start_date: Metric report start date (UTC). Format: YYYY-MM-DD
        :param end_date: Metric report end date (UTC). Format: YYYY-MM-DD
        :param sort_by: Specify sorting order for metrics.
            Accepted params: "ENGAGEMENT","IMPRESSION","OUTBOUND_CLICK","PIN_CLICK","SAVE".
        :param from_claimed_content: Filter on Pins that match your claimed domain.
        :param pin_format: Pin formats to get data for, default is all.
        :param app_types: Apps or devices to get data for, default is all.
        :param metric_types: Metric types to get data for, default is all.
        :param num_of_pins: Number of pins to include, default is 10. Max is 50.
        :param created_in_last_n_days: Get metrics for pins created in the last "n" days. Example: 30.
        :param ad_account_id: Unique identifier of an ad account.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: User Account top pins analytics data.
        """

        return self._get_top_analytics(
            url="user_account/analytics/top_pins",
            start_date=start_date,
            end_date=end_date,
            sort_by=sort_by,
            from_claimed_content=from_claimed_content,
            pin_format=pin_format,
            app_types=app_types,
            metric_types=metric_types,
            num_of_pins=num_of_pins,
            created_in_last_n_days=created_in_last_n_days,
            ad_account_id=ad_account_id,
            return_json=return_json,
        )

    def get_top_video_pins_analytics(
        self,
        start_date: str,
        end_date: str,
        sort_by: str,
        from_claimed_content: str = "BOTH",
        pin_format: str = "ALL",
        app_types: str = "ALL",
        metric_types: Optional[Union[str, list, tuple]] = None,
        num_of_pins: int = 10,
        created_in_last_n_days: Optional[int] = None,
        ad_account_id: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[TopPinsAnalytics, dict]:
        """
        Gets analytics data about a user's top video pins (limited to the top 50).

        :param start_date: Metric report start date (UTC). Format: YYYY-MM-DD
        :param end_date: Metric report end date (UTC). Format: YYYY-MM-DD
        :param sort_by: Specify sorting order for metrics.
            Accepted params: "IMPRESSION","SAVE","OUTBOUND_CLICK","VIDEO_MRC_VIEW","VIDEO_AVG_WATCH_TIME",
            "VIDEO_V50_WATCH_TIME","QUARTILE_95_PERCENT_VIEW","VIDEO_10S_VIEW","VIDEO_START".
        :param from_claimed_content: Filter on Pins that match your claimed domain.
        :param pin_format: Pin formats to get data for, default is all.
        :param app_types: Apps or devices to get data for, default is all.
        :param metric_types: Metric types to get data for, default is all.
        :param num_of_pins: Number of pins to include, default is 10. Max is 50.
        :param created_in_last_n_days: Get metrics for pins created in the last "n" days. Example: 30.
        :param ad_account_id: Unique identifier of an ad account.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: User Account top video pins analytics data.
        """
        return self._get_top_analytics(
            url="user_account/analytics/top_video_pins",
            start_date=start_date,
            end_date=end_date,
            sort_by=sort_by,
            from_claimed_content=from_claimed_content,
            pin_format=pin_format,
            app_types=app_types,
            metric_types=metric_types,
            num_of_pins=num_of_pins,
            created_in_last_n_days=created_in_last_n_days,
            ad_account_id=ad_account_id,
            return_json=return_json,
        )
