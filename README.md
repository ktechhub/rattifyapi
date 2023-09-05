# rattifyapi-python
Python plugin for [RattifApi](https://rattify.com/) View on [pypi.python.org](https://pypi.org/project/rattifyapi/)

## Installation
```sh
pip install rattifyapi
```
## Example

```python
from rattifyapi.rattify import Rattify

secret_key = "rt_test_4973"

rattify = Rattify(secret_key=secret_key)

# to use transaction class
print(rattify.user.list())

# initiate a generic
data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@email.com",
    "date_of_birth": "2000-12-24",
    "country": "Ghana",
}
print(rattify.generic.initialize(data))

# get user
print(rattify.user.verify(reference="e1b6679c5aad4bd3999953ac78e677a79d28d539085e409ebde1be640ebc27e7"))
```

## Static Use
To start using the Rattify Python API, you need to start by setting your secret key.

You can set your secret key in your environment by running:

```sh
export SECRET_KEY = 'your_secret_secret_key'
```

After exporting the keys, you can use the api like this
```python
from rattifyapi.generic import Generic
from rattifyapi.users import User

# list users
print(User.list())

# initiate a generic
data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@email.com",
    "date_of_birth": "2000-12-24",
    "country": "Ghana",
}
print(Generic.initialize(data))

# get user
print(User.verify(reference="reference"))
```

