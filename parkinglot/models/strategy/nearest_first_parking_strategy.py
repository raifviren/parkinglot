from collections import OrderedDict

from parkinglot.exception import SlotNotAvailableError
from .parking_startegy import ParkingStrategy


class NearestFirstParkingStrategy(ParkingStrategy):
    """
    Implementation of NearestFirstParkingStrategy
    As per this strategy, we park the vehicle at parking slot
    which is nearest to the entrance.
    We use in Memory OrderedDict to get all available parking slots
    sorted in order of closeness to entrance in asc order
    """

    def __init__(self):
        self.available_slots = OrderedDict()

    def add_slot(self, slot_no: int):
        if slot_no not in self.available_slots:
            self.available_slots[slot_no] = slot_no

    def get_next_available_slot(self) -> int:
        return next(iter(self.available_slots))

    def remove_slot(self, slot_no: int):
        try:
            del self.available_slots[slot_no]
        except KeyError:
            raise SlotNotAvailableError("Slot {} is not available".format(slot_no))

    def is_slot_empty(self, slot_no) -> bool:
        if slot_no in self.available_slots:
            return True
        return False
