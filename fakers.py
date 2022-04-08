"""Fake generators for ZohoCRMFaker"""
from faker import Faker


fake = Faker()


class FakeCustomer:
    """Class to represent a fake customer."""
    def __init__(self):
        """Initialize a fake customer"""
        self.name: str = fake.name()
        self.address: str = fake.address()
        self.phone: str = fake.phone_number()
        self.email: str = fake.email()

    # These methods should not be used on real people!
    # See https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/  # noqa
    @property
    def first_name(self):
        """Extract first name from full name."""
        return self.name.split()[0]

    @property
    def last_name(self):
        """Extract last name from full name."""
        return self.name.split()[-1]

    def __str__(self):
        return '\n'.join((self.name, self.address, self.phone, self.email))
