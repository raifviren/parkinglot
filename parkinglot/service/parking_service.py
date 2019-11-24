from abc import ABCMeta, abstractmethod

from parkinglot.constants import Status, ResultString
from parkinglot.exception import ParkingLotDoesNotExistError, ParkingException, AlreadyFreeError, AlreadyParkedError, \
    InvalidSlotError
from parkinglot.logger import logger
from parkinglot.models import ParkingLot
from parkinglot.models import Vehicle


class AbstractService(metaclass=ABCMeta):
    """
    Interface for any service of the System
    """
    pass


class ParkingService(AbstractService):
    """
    Generic Interface for Parking Service
    """

    @abstractmethod
    def create_parking_lot(self, capacity: int):
        """
        create a parking lot of given capacity
        """
        pass

    @abstractmethod
    def park(self, vehicle: Vehicle) -> int:
        """
        park given vehicle in Parkin Lot
        """
        pass

    @abstractmethod
    def unpark(self, slot_number: int):
        """
        Unpark Vehicle at given slot
        """
        pass

    @abstractmethod
    def get_status(self):
        """
        Get current status of Parking Lot
        """
        pass

    @abstractmethod
    def get_reg_num_from_color(self, color: str):
        """
        Get registration Number of cars of given color
        """
        pass

    @abstractmethod
    def get_slot_nums_from_color(self, color: str):
        """
        Get slot Number of cars of given color
        """
        pass

    @abstractmethod
    def get_slot_no_from_reg_no(self, reg_no: str) -> int:
        """
        Get slot number from registration Number
        """
        pass

    @abstractmethod
    def flush(self):
        pass


class ParkingServiceImpl(ParkingService):
    """
    Implementation of Parking Service
    """
    parking_lot = None

    def create_parking_lot(self, capacity: int):
        self.parking_lot = ParkingLot(capacity)
        print(ResultString.PARKING_LOT_CREATED.format(self.parking_lot.get_capacity()))

    def park(self, vehicle: Vehicle) -> int:
        try:
            if self.validate_parking_lot():
                slot_no = self.parking_lot.park(vehicle)
                if slot_no == Status.PARKING_FULL:
                    print(ResultString.PARKING_FULL)
                elif slot_no == Status.ALREADY_PARKED:
                    print(AlreadyParkedError(ResultString.ALREADY_PARKED.format(slot_no)))
                else:
                    print(ResultString.SLOT_ALLOTTED.format(slot_no))
                return slot_no
        except Exception as e:
            logger.exception(e)
            raise ParkingException(e)

    def unpark(self, slot_number: int):
        try:
            if self.validate_parking_lot():
                if self.parking_lot.unpark(slot_number):
                    print(ResultString.SLOT_FREED.format(slot_number))
                else:
                    print(AlreadyFreeError(ResultString.ALREADY_FREE.format(slot_number)))
        except KeyError:
            print(InvalidSlotError("You are trying to unpark an invalid slot. Please Try again!"))
        except Exception as e:
            raise ParkingException(e)

    def get_status(self):
        if self.validate_parking_lot():
            print("Slot No.".ljust(12) + "Registration No".ljust(19) + "Colour")
            for slot, vehicle in self.parking_lot.get_slot_vehicle_map().items():
                print(str(slot).ljust(12) + str(vehicle.get_reg_no()).ljust(19) + str(vehicle.get_color()))

    def get_available_slots_count(self) -> int:
        if self.validate_parking_lot():
            return self.parking_lot.get_availability()
        return -1

    def get_reg_num_from_color(self, color: str) -> list:
        if self.validate_parking_lot():
            reg_no = self.parking_lot.get_reg_num_from_color(color)
            print(", ".join(reg_no))
            return reg_no

    def get_slot_nums_from_color(self, color: str) -> list:
        if self.validate_parking_lot():
            slot_nums = self.parking_lot.get_slot_nums_from_color(color)
            print(", ".join([str(slot) for slot in slot_nums]))
            return slot_nums

    def get_slot_no_from_reg_no(self, reg_no: str) -> int:
        if self.validate_parking_lot():
            slot = self.parking_lot.get_slot_no_from_reg_no(reg_no)
            if slot == Status.NOT_FOUND:
                print(ResultString.NOT_FOUND)
            else:
                print(slot)
            return slot

    def flush(self):
        self.parking_lot.flush()

    def validate_parking_lot(self) -> bool:
        if self.parking_lot is None:
            print(ParkingLotDoesNotExistError("Parking Lot does not Exist. Please create Parking lot first"))
            return False
        return True
