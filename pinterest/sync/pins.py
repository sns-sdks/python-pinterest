"""
    Pins endpoints implementation.
"""
from pinterest.base_endpoint import Endpoint


class PinsEndpoint(Endpoint):
    def get(self, pin_id: str, ad_account_id: str = None) -> dict:
        """
        Get a Pin owned by the "operation user_account" - or on a group board that has been shared with this account.

        :param pin_id: Unique identifier of a Pin.
        :param ad_account_id: Unique identifier of an ad account.
        :return: Pin data.
        """
        params = {"ad_account_id": ad_account_id} if ad_account_id else None
        return self._get(
            url=f"pins/{pin_id}",
            params=params,
        )
