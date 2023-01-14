"""Entry point defined here."""
from rattifyapi.base import RatiffyBase
from rattifyapi.generic import Generic
from rattifyapi.users import User


class Rattify(RatiffyBase):
    """Base class defined for Rattify Instance Method."""

    def __init__(self, secret_key=None):
        RatiffyBase.__init__(self, secret_key=secret_key)

        self.generic = Generic
        self.user = User
