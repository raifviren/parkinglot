from unittest import TestCase

from parkinglot.exception import InvalidCommandError
from parkinglot.handlers import ParkingHandler
from parkinglot.models import ParkingLot
from parkinglot.service import ParkingServiceImpl
from parkinglot.tests.stub_methods import DummyCommand


class ParkingHandlerTestCase(TestCase):
    """
    Test cases to for handler ParkingHandler
    """

    def setUp(self):
        """
        Make test database ready to run each test
        """
        ParkingLot.flush()

    def test_set_service(self):
        """
        Test case for set_service function
        """
        handler = ParkingHandler()
        handler.set_service(ParkingServiceImpl())
        self.assertIsNotNone(handler.parkingService)

    def test_validate(self):
        """
        Test case for validate function for positive cases
        """
        handler = ParkingHandler()
        handler.set_service(ParkingServiceImpl())
        self.assertIsNotNone(handler.parkingService)
        self.assertEqual(handler.validate(DummyCommand.CREATE_PARKING_LOT), True)
        self.assertEqual(handler.validate(DummyCommand.PARK), True)
        self.assertEqual(handler.validate(DummyCommand.LEAVE), True)
        self.assertEqual(handler.validate(DummyCommand.STATUS), True)
        self.assertEqual(handler.validate(DummyCommand.REG_NUMBER_FOR_CARS_WITH_COLOR), True)
        self.assertEqual(handler.validate(DummyCommand.SLOT_NUMBERS_FOR_CARS_WITH_COLOR), True)
        self.assertEqual(handler.validate(DummyCommand.SLOT_NUMBER_FOR_REG_NUMBER), True)

    def test_validate_false(self):
        """
        Test case for validate function for negative cases
        """
        handler = ParkingHandler()
        handler.set_service(ParkingServiceImpl())
        self.assertIsNotNone(handler.parkingService)
        self.assertEqual(handler.validate(""), False)
        self.assertEqual(handler.validate("5"), False)
        self.assertEqual(handler.validate(DummyCommand.CREATE_PARKING_LOT + " 5"), False)
        self.assertEqual(handler.validate(DummyCommand.PARK + " Black"), False)
        self.assertEqual(handler.validate(DummyCommand.LEAVE + " 666"), False)
        self.assertEqual(handler.validate(DummyCommand.STATUS + " 111"), False)
        self.assertEqual(handler.validate(DummyCommand.REG_NUMBER_FOR_CARS_WITH_COLOR + " 33"), False)
        self.assertEqual(handler.validate(DummyCommand.SLOT_NUMBERS_FOR_CARS_WITH_COLOR + " 55"), False)
        self.assertEqual(handler.validate(DummyCommand.SLOT_NUMBER_FOR_REG_NUMBER + " White"), False)

    def test_execute(self):
        """
        Test case for execute function
        """
        handler = ParkingHandler()
        handler.set_service(ParkingServiceImpl())
        self.assertIsNotNone(handler.parkingService)
        try:
            handler.execute(DummyCommand.CREATE_PARKING_LOT)
            handler.execute(DummyCommand.PARK)
            handler.execute(DummyCommand.LEAVE)
            handler.execute(DummyCommand.STATUS)
            handler.execute(DummyCommand.REG_NUMBER_FOR_CARS_WITH_COLOR)
            handler.execute(DummyCommand.SLOT_NUMBERS_FOR_CARS_WITH_COLOR)
            handler.execute(DummyCommand.SLOT_NUMBER_FOR_REG_NUMBER)
        except InvalidCommandError:
            self.fail("execute() raised InvalidCommandError unexpectedly!")
