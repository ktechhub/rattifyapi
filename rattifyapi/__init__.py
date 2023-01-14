import os

"""Script used to define constants used across codebase."""

SECRET_KEY = os.getenv("SECRET_KEY", None)
API_URL = "https://users.staging.rattify.com/api/v1/users/"
