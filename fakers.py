"""Fake generators for ZohoCRMFaker"""
from faker import Faker


fake = Faker()


class FakeCustomer:
    """Class to represent a fake customer"""
    def __init__(self):
        """Initialize a fake customer"""
        self.name: str = fake.name()
        self.address: str = fake.address()
        self.phone: str = fake.phone_number()

    def __str__(self):
        return '\n'.join((self.name, self.address, self.phone))
