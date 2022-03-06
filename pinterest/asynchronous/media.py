"""
    Media endpoints implementation.
"""

from typing import Optional, Union

from pinterest.base_endpoint import AsyncEndpoint
from pinterest.models import (
    MediaUpload,
    MediaUploadsResponse,
    RegisterMediaUploadResponse,
)


class MediaAsyncEndpoint(AsyncEndpoint):
    async def list(
        self,
        page_size: int = 25,
        bookmark: Optional[str] = None,
        return_json: bool = False,
    ) -> Union[MediaUploadsResponse, dict]:
        """

        :param page_size: Maximum number of items to include in a single page of the response. [1..100]
        :param bookmark: Cursor used to fetch the next page of items.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Media Uploads data.
        """
        params = {"page_size": page_size}
        if bookmark is not None:
            params["bookmark"] = bookmark

        resp = await self._get(
            url="media",
            params=params,
        )
        data = self._parse_response(response=resp)
        return (
            data if return_json else MediaUploadsResponse.new_from_json_dict(data=data)
        )

    async def register(
        self, media_type: str, return_json: bool = False
    ) -> Union[RegisterMediaUploadResponse, dict]:
        """
        Register your intent to upload media

        The response includes all the information needed to upload the media to Pinterest.

        :param media_type: Type for media
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Response for register.
        """
        data = {"media_type": media_type}
        resp = await self._post(url="media", json=data)
        data = self._parse_response(response=resp)
        return (
            data
            if return_json
            else RegisterMediaUploadResponse.new_from_json_dict(data=data)
        )

    async def get(
        self, media_id: str, return_json: bool = False
    ) -> Union[MediaUpload, dict]:
        """
        Get details for a registered media upload, including its current status.

        :param media_id: Media identifier.
        :param return_json: Type for returned data. If you set True JSON data will be returned.
        :return: Media Upload data.
        """
        resp = await self._post(url=f"media/{media_id}")
        data = self._parse_response(response=resp)
        return (
            data
            if return_json
            else RegisterMediaUploadResponse.new_from_json_dict(data=data)
        )
