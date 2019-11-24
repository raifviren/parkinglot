import threading

from parkinglot.constants import Status
from .strategy import ParkingStrategy, NearestFirstParkingStrategy
from .vehicle import Vehicle


class ParkingLot:
    # singleton ParkingLot to ensure only one object of ParkingLot in the system,
    instance = None

    class __OnlyOne:
        def __init__(self, capacity: int, parking_strategy: ParkingStrategy = None):
            self.__capacity = capacity
            self.__availability = capacity
            if parking_strategy:
                self.__parking_strategy = parking_strategy
            else:
                self.__parking_strategy = NearestFirstParkingStrategy()
            self.__slot_vehicle_map = {}
            for i in range(1, capacity + 1):
                self.__parking_strategy.add_slot(i)
            self.__lock = threading.Lock()

        def __repr__(self):
            return "{capacity:" + str(self.__capacity) + "," + \
                   "availability:" + str(self.__availability) + "," + \
                   "slot_vehicle_map:" + str(self.__slot_vehicle_map) + "," \
                                                                        "free: " + str(
                self.__parking_strategy.get_slots()) + ""

        @property
        def capacity(self):
            return self.__capacity

        @property
        def slot_vehicle_map(self):
            return self.__slot_vehicle_map

        @property
        def availability(self):
            return self.__availability

        @property
        def parking_strategy(self):
            return self.__parking_strategy

        @property
        def lock(self):
            return self.__lock

        def decr_availability(self):
            self.__availability -= 1

        def incr_availability(self):
            self.__availability += 1

        def flush(self):
            self.__capacity = 0
            self.__availability = 0
            self.__slot_vehicle_map = {}
            self.__parking_strategy = None
            self.__lock = None

    def __init__(self, capacity: int):
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot.__OnlyOne(capacity)
        else:
            ParkingLot.instance.__capacity = capacity

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def park(self, vehicle: Vehicle) -> int:
        if self.is_full():
            return Status.PARKING_FULL
        if vehicle in self.slot_vehicle_map.values():
            return Status.ALREADY_PARKED
        # synchronizing to allow parking via multiple entrances panels
        # without interfering with each other
        self.lock.acquire()
        slot_no = self.parking_strategy.get_next_available_slot()
        self.slot_vehicle_map[slot_no] = vehicle
        self.decr_availability()
        self.parking_strategy.remove_slot(slot_no)
        self.lock.release()
        return slot_no

    def unpark(self, slot_no: int) -> bool:
        if self.is_empty():
            return False
        if self.parking_strategy.is_slot_empty(slot_no):
            return False
        self.incr_availability()
        self.parking_strategy.add_slot(slot_no)
        del self.slot_vehicle_map[slot_no]
        return True

    def is_full(self) -> bool:
        return self.availability == 0

    def is_empty(self) -> bool:
        return self.availability == self.capacity

    def get_capacity(self) -> int:
        return self.capacity

    def get_availability(self) -> int:
        return self.availability

    def get_slot_vehicle_map(self) -> int:
        return self.slot_vehicle_map

    def get_reg_num_from_color(self, color: str) -> list:
        res = []
        for slot, vehicle in self.slot_vehicle_map.items():
            if vehicle.get_color() == color:
                res.append(vehicle.get_reg_no())
        return res

    def get_slot_nums_from_color(self, color: str) -> list:
        res = []
        for slot, vehicle in self.slot_vehicle_map.items():
            if vehicle.get_color() == color:
                res.append(slot)
        return res

    def get_slot_no_from_reg_no(self, reg_no: str) -> int:
        for slot, vehicle in self.slot_vehicle_map.items():
            if vehicle.get_reg_no() == reg_no:
                return slot
        return Status.NOT_FOUND

    @staticmethod
    def flush():
        ParkingLot.instance = None
