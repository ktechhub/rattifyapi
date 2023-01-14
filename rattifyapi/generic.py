"""Script used to define the rattify Generic class."""

from rattifyapi.base import RatiffyBase


class Generic(RatiffyBase):
    """docstring for generic users."""

    @classmethod
    def initialize(cls, **kwargs):
        """
        Initialize a generic user.

        Args:
            first_name: First name
            last_name: Last name
            email: email address
            date_of_birth: Date of Birth

        Returns:
            Json data from rattify API.
        """

        return cls().requests.post("get-info/", data=kwargs)
