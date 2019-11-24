"""
This file contains all constants used in code base
"""
from enum import Enum

MAX_PARKING_LEVELS = 1


class VehicleType(Enum):
    """
    Vehicle Types Supported in system
    """
    CAR = 1
    MOTORBIKE = 2


class ParkingSpotType(Enum):
    """
        Parking Slot Types Supported in system
    """
    COMPACT = 1
    MOTORBIKE = 2


class Command:
    """
    Commands Supported in system
    """
    CREATE_PARKING_LOT = "create_parking_lot"
    PARK = "park"
    LEAVE = "leave"
    STATUS = "status"
    REG_NUMBER_FOR_CARS_WITH_COLOR = "registration_numbers_for_cars_with_colour"
    SLOT_NUMBERS_FOR_CARS_WITH_COLOR = "slot_numbers_for_cars_with_colour"
    SLOT_NUMBER_FOR_REG_NUMBER = "slot_number_for_registration_number"


COMMAND_PARAM_MAP = {
    Command.CREATE_PARKING_LOT: 1,
    Command.PARK: 2,
    Command.LEAVE: 1,
    Command.STATUS: 0,
    Command.REG_NUMBER_FOR_CARS_WITH_COLOR: 1,
    Command.SLOT_NUMBERS_FOR_CARS_WITH_COLOR: 1,
    Command.SLOT_NUMBER_FOR_REG_NUMBER: 1,
}


class Status:
    """
    Status for code flow tracking
    """
    PARKING_FULL = -1
    ALREADY_PARKED = -2
    NOT_FOUND = -3
    PARKING_EMPTY = -4


class ResultString:
    """
    Output String to be shown to user
    """
    PARKING_LOT_CREATED = "Created a parking lot with {} slots"
    SLOT_ALLOTTED = "Allocated slot number: {}"
    SLOT_FREED = "Slot number {} is free"
    PARKING_FULL = "Sorry, parking lot is full"
    NOT_FOUND = "Not found"
    ALREADY_PARKED = "Already parked at slot number: {}"
    ALREADY_FREE = "Slot number {} is already empty"
