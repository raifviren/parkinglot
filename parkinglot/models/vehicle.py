from abc import ABC

from parkinglot.constants import VehicleType


class Vehicle(ABC):
    def __init__(self, reg_no: str, color: str, vehicle_type: VehicleType):
        self.__reg_no = reg_no
        self.__color = color
        self.__type = vehicle_type

    def get_reg_no(self):
        return self.__reg_no

    def get_color(self):
        return self.__color


class Car(Vehicle):
    def __init__(self, reg_no: str, color: str):
        super().__init__(reg_no, color, VehicleType.CAR)


class MOTORBIKE(Vehicle):
    def __init__(self, reg_no: str, color: str):
        super().__init__(reg_no, color, VehicleType.MOTORBIKE)
