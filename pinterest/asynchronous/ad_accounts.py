"""
    Ad accounts endpoints implementation.
"""

from typing import Dict, List, Optional, Union

from pinterest.base_endpoint import AsyncEndpoint
from pinterest.models import (
    AdAccountsResponse,
    CampaignsResponse,
    AdGroupsResponse,
    AdsResponse,
)
from pinterest.utils.params import enf_comma_separated


class AdAccountsAsyncEndpoint(AsyncEndpoint):
    async def list(
        self,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        include_shared_accounts: Optional[bool] = None,
        return_json: bool = False,
    ) -> Union[AdAccountsResponse, dict]:
        """
        Get a list of the ad_accounts that the "operation user_account" has access to.

        :param page_size: Maximum number of items to include in a single page of the response. [1..100]
        :param bookmark: Cursor used to fetch the next page of items.
        :param include_shared_accounts: Include shared ad accounts.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Ad Accounts Response
        """
        params = {"page_size": page_size}
        if bookmark is not None:
            params["bookmark"] = bookmark
        if include_shared_accounts is not None:
            params["include_shared_accounts"] = include_shared_accounts

        resp = await self._get(url="ad_accounts", params=params)
        data = self._parse_response(response=resp)
        return data if return_json else AdAccountsResponse.new_from_json_dict(data=data)

    async def get_analytics(
        self,
        ad_account_id: str,
        start_date: str,
        end_date: str,
        columns: Union[str, list, set],
        granularity: str,
        click_window_days: Optional[int] = None,
        engagement_window_days: Optional[int] = None,
        view_window_days: Optional[int] = None,
        conversion_report_time: Optional[str] = None,
    ) -> List[Dict]:
        """
        Get analytics for the specified ad_account_id, filtered by the specified options.

        :param ad_account_id: Unique identifier of an ad account.
        :param start_date: Metric report start date (UTC). Format: YYYY-MM-DD
        :param end_date: Metric report end date (UTC). Format: YYYY-MM-DD
        :param columns: Columns to retrieve. NOTE: Any metrics defined as MICRO_DOLLARS returns a value
            based on the advertiser profile's currency field.
            For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars.
            Otherwise, it's in microunits of the advertiser's currency.
        :param granularity: Granularity. Enum: "TOTAL","DAY","HOUR","WEEK","MONTH"
        :param click_window_days: Number of days to use as the conversion attribution window for a pin click action.
        :param engagement_window_days: Number of days to use as the conversion attribution window for an engagement action.
        :param view_window_days: Number of days to use as the conversion attribution window for a view action.
        :param conversion_report_time: The date by which the conversion metrics returned from this endpoint will be reported.
        :return: Ad Account Analytics.
        """
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "columns": enf_comma_separated(field="columns", value=columns),
            "granularity": granularity,
        }
        if click_window_days:
            data["click_window_days"] = click_window_days
        if engagement_window_days:
            data["engagement_window_days"] = engagement_window_days
        if view_window_days:
            data["view_window_days"] = view_window_days
        if conversion_report_time:
            data["conversion_report_time"] = conversion_report_time

        resp = await self._get(
            url=f"ad_accounts/{ad_account_id}/analytics",
            json=data,
        )
        data = self._parse_response(response=resp)
        return data

    async def list_campaigns(
        self,
        ad_account_id: str,
        campaign_ids: Optional[Union[str, list, set]] = None,
        entity_statuses: Optional[Union[str, list, set]] = None,
        order: Optional[str] = None,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[CampaignsResponse, dict]:
        """
        Get a list of the campaigns in the specified ad_account_id, filtered by the specified options.

        :param ad_account_id: Unique identifier of an ad account.
        :param campaign_ids: List of Campaign Ids to use to filter the results.
        :param entity_statuses: Entity status.
        :param order: The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
        :param page_size: Maximum number of items to include in a single page of the response. [1..100]
        :param bookmark: Cursor used to fetch the next page of items.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Campaigns data.
        """
        params = {"page_size": page_size}
        if bookmark is not None:
            params["bookmark"] = bookmark
        if campaign_ids is not None:
            params["campaign_ids"] = enf_comma_separated(
                field="campaign_ids", value=campaign_ids
            )
        if entity_statuses is not None:
            params["entity_statuses"] = enf_comma_separated(
                field="entity_statuses", value=entity_statuses
            )
        if order is not None:
            params["order"] = order

        resp = await self._get(
            url=f"ad_accounts/{ad_account_id}/campaigns", params=params
        )
        data = self._parse_response(response=resp)
        return data if return_json else CampaignsResponse.new_from_json_dict(data=data)

    async def get_campaign_analytics(
        self,
        ad_account_id: str,
        campaign_ids: Union[str, list, set],
        start_date: str,
        end_date: str,
        columns: Union[str, list, set],
        granularity: str,
        click_window_days: Optional[int] = None,
        engagement_window_days: Optional[int] = None,
        view_window_days: Optional[int] = None,
        conversion_report_time: Optional[str] = None,
    ) -> List[Dict]:
        """
        Get analytics for the specified campaigns in the specified ad_account_id, filtered by the specified options.

        :param ad_account_id: Unique identifier of an ad account.
        :param campaign_ids: List of Campaign Ids to use to filter the results.
        :param start_date: Metric report start date (UTC). Format: YYYY-MM-DD
        :param end_date: Metric report end date (UTC). Format: YYYY-MM-DD
        :param columns: Columns to retrieve. NOTE: Any metrics defined as MICRO_DOLLARS returns a value
            based on the advertiser profile's currency field.
            For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars.
            Otherwise, it's in microunits of the advertiser's currency.
        :param granularity: Granularity. Enum: "TOTAL","DAY","HOUR","WEEK","MONTH"
        :param click_window_days: Number of days to use as the conversion attribution window for a pin click action.
        :param engagement_window_days: Number of days to use as the conversion attribution window for an engagement action.
        :param view_window_days: Number of days to use as the conversion attribution window for a view action.
        :param conversion_report_time: The date by which the conversion metrics returned from this endpoint will be reported.
        :return: Ad Account Campaigns Analytics.
        """
        data = {
            "campaign_ids": enf_comma_separated(
                field="campaign_ids", value=campaign_ids
            ),
            "start_date": start_date,
            "end_date": end_date,
            "columns": enf_comma_separated(field="columns", value=columns),
            "granularity": granularity,
        }
        if click_window_days:
            data["click_window_days"] = click_window_days
        if engagement_window_days:
            data["engagement_window_days"] = engagement_window_days
        if view_window_days:
            data["view_window_days"] = view_window_days
        if conversion_report_time:
            data["conversion_report_time"] = conversion_report_time

        resp = await self._get(
            url=f"ad_accounts/{ad_account_id}/campaigns/analytics",
            json=data,
        )
        data = self._parse_response(response=resp)
        return data

    async def list_ad_groups(
        self,
        ad_account_id: str,
        campaign_ids: Optional[Union[str, list, set]] = None,
        ad_group_ids: Optional[Union[str, list, set]] = None,
        entity_statuses: Optional[Union[str, list, set]] = None,
        order: Optional[str] = None,
        translate_interests_to_names: Optional[str] = None,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[AdGroupsResponse, dict]:
        """
        Get a list of the ad groups in the specified ad_account_id, filtered by the specified options.

        :param ad_account_id: Unique identifier of an ad account.
        :param campaign_ids: List of Campaign Ids to use to filter the results.
        :param ad_group_ids: List of Ad group Ids to use to filter the results.
        :param entity_statuses: Entity status
        :param order: The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
            Note that higher-value IDs are associated with more-recently added items.
        :param translate_interests_to_names: Return interests as text names (if value is true) rather than topic IDs.
        :param page_size: Maximum number of items to include in a single page of the response. [1..100]
        :param bookmark: Cursor used to fetch the next page of items.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Ad groups data.
        """
        params = {"page_size": page_size}
        if bookmark is not None:
            params["bookmark"] = bookmark
        if campaign_ids is not None:
            params["campaign_ids"] = enf_comma_separated(
                field="campaign_ids", value=campaign_ids
            )
        if ad_group_ids is not None:
            params["ad_group_ids"] = enf_comma_separated(
                field="ad_group_ids", value=ad_group_ids
            )
        if entity_statuses is not None:
            params["entity_statuses"] = enf_comma_separated(
                field="entity_statuses", value=entity_statuses
            )
        if order is not None:
            params["order"] = order
        if translate_interests_to_names is not None:
            params["translate_interests_to_names"] = translate_interests_to_names

        resp = await self._get(
            url=f"ad_accounts/{ad_account_id}/ad_groups",
            params=params,
        )
        data = self._parse_response(response=resp)
        return data if return_json else AdGroupsResponse.new_from_json_dict(data=data)

    async def get_ad_group_analytics(
        self,
        ad_account_id: str,
        ad_group_ids: Union[str, list, set],
        start_date: str,
        end_date: str,
        columns: Union[str, list, set],
        granularity: str,
        click_window_days: Optional[int] = None,
        engagement_window_days: Optional[int] = None,
        view_window_days: Optional[int] = None,
        conversion_report_time: Optional[str] = None,
    ) -> List[Dict]:
        """
        Get analytics for the specified ad groups in the specified ad_account_id, filtered by the specified options.

        :param ad_account_id: Unique identifier of an ad account.
        :param ad_group_ids: List of Ad group Ids to use to filter the results.
        :param start_date: Metric report start date (UTC). Format: YYYY-MM-DD
        :param end_date: Metric report end date (UTC). Format: YYYY-MM-DD
        :param columns: Columns to retrieve. NOTE: Any metrics defined as MICRO_DOLLARS returns a value based on the advertiser profile's currency field.
        :param granularity: Granularity.
        :param click_window_days: Number of days to use as the conversion attribution window for a pin click action.
        :param engagement_window_days: Number of days to use as the conversion attribution window for an engagement action.
        :param view_window_days: Number of days to use as the conversion attribution window for a view action.
        :param conversion_report_time: The date by which the conversion metrics returned from this endpoint will be reported.
        :return: Ad group analytics.
        """
        data = {
            "ad_group_ids": enf_comma_separated(
                field="ad_group_ids", value=ad_group_ids
            ),
            "start_date": start_date,
            "end_date": end_date,
            "columns": enf_comma_separated(field="columns", value=columns),
            "granularity": granularity,
        }
        if click_window_days:
            data["click_window_days"] = click_window_days
        if engagement_window_days:
            data["engagement_window_days"] = engagement_window_days
        if view_window_days:
            data["view_window_days"] = view_window_days
        if conversion_report_time:
            data["conversion_report_time"] = conversion_report_time

        resp = await self._get(
            url=f"ad_accounts/{ad_account_id}/ad_groups/analytics",
            json=data,
        )
        data = self._parse_response(response=resp)
        return data

    async def list_ads(
        self,
        ad_account_id: str,
        campaign_ids: Optional[Union[str, list, set]] = None,
        ad_group_ids: Optional[Union[str, list, set]] = None,
        ad_ids: Optional[Union[str, list, set]] = None,
        entity_statuses: Optional[Union[str, list, set]] = None,
        order: Optional[str] = None,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[AdsResponse, dict]:
        """
        Get a list of the ads in the specified ad_account_id, filtered by the specified options.

        :param ad_account_id: Unique identifier of an ad account.
        :param campaign_ids: List of Campaign Ids to use to filter the results. [1..100]
        :param ad_group_ids: List of Ad group Ids to use to filter the results. [1..100]
        :param ad_ids: List of Ad Ids to use to filter the results. [1..100]
        :param entity_statuses: Entity status.
        :param order: The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
        :param page_size: Maximum number of items to include in a single page of the response. [1..100]
        :param bookmark: Cursor used to fetch the next page of items.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Ads data.
        """
        params = {"page_size": page_size}
        if bookmark is not None:
            params["bookmark"] = bookmark
        if campaign_ids is not None:
            params["campaign_ids"] = enf_comma_separated(
                field="campaign_ids", value=campaign_ids
            )
        if ad_group_ids is not None:
            params["ad_group_ids"] = enf_comma_separated(
                field="ad_group_ids", value=ad_group_ids
            )
        if ad_ids is not None:
            params["ad_ids"] = enf_comma_separated(field="ad_ids", value=ad_ids)
        if entity_statuses is not None:
            params["entity_statuses"] = enf_comma_separated(
                field="entity_statuses", value=entity_statuses
            )
        if order is not None:
            params["order"] = order

        resp = await self._get(
            url=f"ad_accounts/{ad_account_id}/ads",
            params=params,
        )
        data = self._parse_response(response=resp)
        return data if return_json else AdsResponse.new_from_json_dict(data=data)

    async def get_ad_analytics(
        self,
        ad_account_id: str,
        ad_ids: Union[str, list, set],
        start_date: str,
        end_date: str,
        columns: Union[str, list, set],
        granularity: str,
        click_window_days: Optional[int] = None,
        engagement_window_days: Optional[int] = None,
        view_window_days: Optional[int] = None,
        conversion_report_time: Optional[str] = None,
    ) -> List[Dict]:
        """
        Get analytics for the specified ads in the specified ad_account_id, filtered by the specified options.

        :param ad_account_id: Unique identifier of an ad account.
        :param ad_ids: List of Ad Ids to use to filter the results. [1..100]
        :param start_date: Metric report start date (UTC). Format: YYYY-MM-DD.
        :param end_date: Metric report end date (UTC). Format: YYYY-MM-DD.
        :param columns: Columns to retrieve.
            NOTE: Any metrics defined as MICRO_DOLLARS returns a value based on the advertiser profile's currency field.
        :param granularity: Granularity
        :param click_window_days: Number of days to use as the conversion attribution window for a pin click action.
        :param engagement_window_days: Number of days to use as the conversion attribution window for an engagement action.
        :param view_window_days: Number of days to use as the conversion attribution window for a view action.
        :param conversion_report_time: The date by which the conversion metrics returned from this endpoint will be reported.
        :return: Ad analytics
        """
        data = {
            "ad_ids": enf_comma_separated(field="ad_ids", value=ad_ids),
            "start_date": start_date,
            "end_date": end_date,
            "columns": enf_comma_separated(field="columns", value=columns),
            "granularity": granularity,
        }
        if click_window_days:
            data["click_window_days"] = click_window_days
        if engagement_window_days:
            data["engagement_window_days"] = engagement_window_days
        if view_window_days:
            data["view_window_days"] = view_window_days
        if conversion_report_time:
            data["conversion_report_time"] = conversion_report_time

        resp = await self._get(
            url=f"ad_accounts/{ad_account_id}/ads/analytics",
            json=data,
        )
        data = self._parse_response(response=resp)
        return data

    async def get_product_group_analytics(
        self,
        ad_account_id: str,
        product_group_ids: Union[str, list, set],
        start_date: str,
        end_date: str,
        columns: Union[str, list, set],
        granularity: str,
        click_window_days: Optional[int] = None,
        engagement_window_days: Optional[int] = None,
        view_window_days: Optional[int] = None,
        conversion_report_time: Optional[str] = None,
    ) -> List[Dict]:
        """
        Get analytics for the specified product groups in the specified ad_account_id, filtered by the specified options.

        :param ad_account_id: Unique identifier of an ad account.
        :param product_group_ids: List of Product group Ids to use to filter the results. [1..100]
        :param start_date: Metric report start date (UTC). Format: YYYY-MM-DD.
        :param end_date: Metric report end date (UTC). Format: YYYY-MM-DD.
        :param columns: Columns to retrieve.
            NOTE: Any metrics defined as MICRO_DOLLARS returns a value based on the advertiser profile's currency field.
        :param granularity: Granularity
        :param click_window_days: Number of days to use as the conversion attribution window for a pin click action.
        :param engagement_window_days: Number of days to use as the conversion attribution window for an engagement action.
        :param view_window_days: Number of days to use as the conversion attribution window for a view action.
        :param conversion_report_time: The date by which the conversion metrics returned from this endpoint will be reported.
        :return: Product group analytics
        """
        data = {
            "product_group_ids": enf_comma_separated(
                field="product_group_ids", value=product_group_ids
            ),
            "start_date": start_date,
            "end_date": end_date,
            "columns": enf_comma_separated(field="columns", value=columns),
            "granularity": granularity,
        }
        if click_window_days:
            data["click_window_days"] = click_window_days
        if engagement_window_days:
            data["engagement_window_days"] = engagement_window_days
        if view_window_days:
            data["view_window_days"] = view_window_days
        if conversion_report_time:
            data["conversion_report_time"] = conversion_report_time

        resp = await self._get(
            url=f"ad_accounts/{ad_account_id}/product_groups/analytics",
            json=data,
        )
        data = self._parse_response(response=resp)
        return data
