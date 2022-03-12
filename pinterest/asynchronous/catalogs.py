"""
    Catalogs endpoint implementation.
"""

from typing import Optional, Union

from pinterest.base_endpoint import AsyncEndpoint
from pinterest.exceptions import PinterestException
from pinterest.models import (
    CatalogFeed,
    CatalogFeedsResponse,
    CatalogFeedProcessResultsResponse,
)


class CatalogsEndpoint(AsyncEndpoint):
    async def list_feeds(
        self,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[CatalogFeedsResponse, dict]:
        """
        Fetch feeds owned by the "operating user_account".

        :param page_size: Maximum number of items to include in a single page of the response. [1..100]
        :param bookmark: Cursor used to fetch the next page of items
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Catalogs Response
        """
        params = {"page_size": page_size}
        if bookmark is not None:
            params["bookmark"] = bookmark
        resp = await self._get(url="catalogs/feeds", params=params)
        data = self._parse_response(response=resp)
        return (
            data if return_json else CatalogFeedsResponse.new_from_json_dict(data=data)
        )

    async def create_feed(
        self,
        country: str,
        format: str,
        locale: str,
        location: str,
        default_availability: Optional[str] = None,
        default_currency: Optional[str] = None,
        name: Optional[str] = None,
        credentials: Optional[dict] = None,
        preferred_processing_schedule: Optional[dict] = None,
        return_json: bool = False,
    ) -> Union[CatalogFeed, dict]:
        """
        Create a new feed owned by the "operating user_account".

        :param country: Country ID from ISO 3166-1 alpha-2.
        :param format: The file format of a feed. Enum: "TSV" "CSV" "XML"
        :param locale: The locale used within a feed for product descriptions.
        :param location: The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing.
        :param default_availability: Default availability for products in a feed.
        :param default_currency: Currency Codes from ISO 4217.
        :param name: A human-friendly name associated to a given feed.
        :param credentials: Use this if your feed file requires username and password.
        :param preferred_processing_schedule:
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: CatalogFeed data.
        """
        data = {
            "country": country,
            "format": format,
            "locale": locale,
            "location": location,
        }
        if credentials is not None:
            data["credentials"] = credentials
        if preferred_processing_schedule is not None:
            data["preferred_processing_schedule"] = preferred_processing_schedule
        if default_availability is not None:
            data["default_availability"] = default_availability
        if default_currency is not None:
            data["default_currency"] = default_currency
        if name is not None:
            data["name"] = name
        resp = await self._post(url="boards", json=data)
        data = self._parse_response(response=resp)
        return data if return_json else CatalogFeed.new_from_json_dict(data=data)

    async def get_feed(
        self, feed_id: str, return_json: bool = False
    ) -> Union[CatalogFeed, dict]:
        """
        Get a single feed owned by the "operating user_account".

        :param feed_id: Unique identifier of a feed.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Catalog Feed data.
        """
        resp = await self._get(url=f"catalogs/feeds/{feed_id}")
        data = self._parse_response(response=resp)
        return data if return_json else CatalogFeed.new_from_json_dict(data=data)

    async def update_feed(
        self,
        feed_id: str,
        default_availability: Optional[str] = None,
        default_currency: Optional[str] = None,
        name: Optional[str] = None,
        format: Optional[str] = None,
        location: Optional[str] = None,
        credentials: Optional[dict] = None,
        preferred_processing_schedule: Optional[dict] = None,
        return_json: bool = False,
    ) -> Union[CatalogFeed, dict]:
        """
        Update a feed owned by the "operating user_account".

        :param feed_id: Unique identifier of a feed.
        :param default_availability: Default availability for products in a feed.
        :param default_currency: Currency Codes from ISO 4217.
        :param name: A human-friendly name associated to a given feed.
        :param format: The file format of a feed. Enum: "TSV" "CSV" "XML"
        :param location: The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing.
        :param credentials: Use this if your feed file requires username and password.
        :param preferred_processing_schedule: Optional daily processing schedule. Use this to configure the preferred time for processing a feed (otherwise random).
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Catalog Feed data.
        """

        data = {}
        if default_availability is not None:
            data["default_availability"] = default_availability
        if default_currency is not None:
            data["default_currency"] = default_currency
        if name is not None:
            data["name"] = name
        if format is not None:
            data["format"] = format
        if location is not None:
            data["location"] = location
        if credentials is not None:
            data["credentials"] = credentials
        if preferred_processing_schedule is not None:
            data["preferred_processing_schedule"] = preferred_processing_schedule
        if not data:
            raise PinterestException(
                code=-1,
                message="Update catalog feed need not less than one parameters.",
            )
        resp = await self._patch(url=f"catalogs/feeds/{feed_id}", json=data)
        data = self._parse_response(response=resp)
        return data if return_json else CatalogFeed.new_from_json_dict(data=data)

    async def delete(self, feed_id: str) -> bool:
        """
        Delete a feed owned by the "operating user_account".

        :param feed_id: Unique identifier of a feed.
        :return: delete status
        """
        resp = await self._delete(url=f"catalogs/feeds/{feed_id}")
        if resp.is_success:
            return True
        self._parse_response(response=resp)

    async def list_feed_processing_results(
        self,
        feed_id: str,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[CatalogFeedProcessResultsResponse, dict]:
        """
        Fetch a feed processing results owned by the owner user account.

        :param feed_id: Unique identifier of a feed.
        :param page_size: Maximum number of items to include in a single page of the response. [1..100]
        :param bookmark: Cursor used to fetch the next page of items.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Catalogs feed process results data.
        """
        params = {"page_size": page_size}
        if bookmark is not None:
            params["bookmark"] = bookmark
        resp = await self._get(
            url=f"catalogs/feeds/{feed_id}/processing_results", params=params
        )
        data = self._parse_response(response=resp)
        return (
            data
            if return_json
            else CatalogFeedProcessResultsResponse.new_from_json_dict(data=data)
        )
