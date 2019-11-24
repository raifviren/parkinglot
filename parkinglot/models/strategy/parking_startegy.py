from abc import ABCMeta, abstractmethod


class ParkingStrategy(metaclass=ABCMeta):
    """
        Generic Interface for Strategies for Parking System
    """

    @abstractmethod
    def add_slot(self, slot_no: int):
        """
        Add a parking slot
        """
        pass

    @abstractmethod
    def get_next_available_slot(self) -> int:
        """
        Get next available parking slot for parking
        """
        pass

    @abstractmethod
    def remove_slot(self, slot_no: int):
        """
        Remove a parking slot from Parking Lot
        """
        pass
