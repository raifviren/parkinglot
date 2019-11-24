"""
A file to create user-defined exception
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BaseAppException(BaseException):
    """
    BaseAppException is the base class to inherite among app's exceptions
    """
    pass


class BaseServerError(BaseAppException):
    """
    ServerError is the base class for exceptions written mainly for server side errors.
    """
    pass


class BaseInputError(BaseAppException):
    """
    InputError is the base class for exceptions written mainly for user side errors.
    """
    pass


class SlotNotAvailableError(BaseInputError):
    """
    When we try to free an unavailable slot
    """
    pass


class ParkingLotDoesNotExistError(BaseInputError):
    """
    When we try to take action but parking lot is not created
    """
    pass


class AlreadyParkedError(BaseInputError):
    """
    When we try to park on already part slot
    """
    pass


class AlreadyFreeError(BaseInputError):
    """
    When we try to free already empty slot
    """
    pass


class InvalidCommandError(BaseInputError):
    """
    When we try to enter invalid Command
    """
    pass


class InvalidSlotError(BaseInputError):
    """
    When we try to enter invalid Parking Slot
    """
    pass


class ParkingException(BaseServerError):
    """
    When we encounter an unpredicted exception
    """
    pass
