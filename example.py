from rattifyapi.rattify import Rattify

secret_key = "rt_test_4973"

rattify = Rattify(secret_key=secret_key)

# list users
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
print(rattify.user.verify(reference="reference"))
