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
