from abc import ABCMeta, abstractmethod

from parkinglot.constants import Command, COMMAND_PARAM_MAP
from parkinglot.exception import ParkingException, InvalidCommandError
from parkinglot.logger import logger
from parkinglot.models import Car
from parkinglot.service import AbstractService, ParkingService


class AbstractHandler(metaclass=ABCMeta):
    """
        Interface for generic Service Handler
    """

    @abstractmethod
    def set_service(self, service: AbstractService):
        """
            setter for service
        """
        pass

    @abstractmethod
    def execute(self, action: str):
        """
            business logic implementation for handler
        """
        pass

    @abstractmethod
    def validate(self, input_string: str) -> bool:
        """
        Validation before execution
        """
        pass


class ParkingHandler(AbstractHandler):
    """
    Handler implementation for Parking Service
    """
    parkingService = None

    def set_service(self, service: ParkingService):
        self.parkingService = service

    def execute(self, action: str):
        try:
            action_arr = action.split(" ")
            cmd = action_arr[0]
            if cmd == Command.CREATE_PARKING_LOT:
                capacity = int(action_arr[1])
                self.parkingService.create_parking_lot(capacity)

            elif cmd == Command.PARK:
                self.parkingService.park(Car(action_arr[1], action_arr[2]))
            elif cmd == Command.LEAVE:
                self.parkingService.unpark(int(action_arr[1]))
            elif cmd == Command.STATUS:
                self.parkingService.get_status()
            elif cmd == Command.REG_NUMBER_FOR_CARS_WITH_COLOR:
                self.parkingService.get_reg_num_from_color(action_arr[1])
            elif cmd == Command.SLOT_NUMBERS_FOR_CARS_WITH_COLOR:
                self.parkingService.get_slot_nums_from_color(action_arr[1])
            elif cmd == Command.SLOT_NUMBER_FOR_REG_NUMBER:
                self.parkingService.get_slot_no_from_reg_no(action_arr[1])
            else:
                logger.error("Command Not Supported: {}".format(cmd))
        except ValueError as e:
            raise InvalidCommandError(e)
        except Exception as e:
            logger.exception(e)
            raise ParkingException(e)

    def validate(self, input_string: str) -> bool:
        try:
            args = input_string.split(" ")
            param = COMMAND_PARAM_MAP[args[0]]
            return param + 1 == len(args)
        except KeyError:
            return False
        except Exception as e:
            logger.exception(e)
            return False
