"""
    Exceptions for library
"""


class PinterestException(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, code, message, **kwargs):
        """
        :param code: Error code
        :param message: Error message
        """
        self.code = code
        self.message = message

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return f"Error code: {self.code}, Message: {self.message}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.code}, {self.message})"
