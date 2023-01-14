"""Script used to define the rattify User class."""

from rattifyapi.base import RatiffyBase


class User(RatiffyBase):
    """docstring for all users."""

    @classmethod
    def list(cls):
        """
        List users.

        Args:
            No argument required.

        Returns:
            Json data from rattify API.
        """
        return cls().requests.get("list/")

    @classmethod
    def verify(cls, reference):
        """
        Verify user data.

        Args:
            reference: a unique value needed for a user.

        Returns:
            Json data from rattify API.
        """
        return cls().requests.get(f"{reference}")
