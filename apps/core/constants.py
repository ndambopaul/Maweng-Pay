from enum import Enum


class UserRole(Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"

    @classmethod
    def choices(cls):
        return [(role.value, role.name) for role in cls]


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

    @classmethod
    def choices(cls):
        return [(role.value, role.name) for role in cls]
