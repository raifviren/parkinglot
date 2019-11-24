from unittest import TestCase

from parkinglot.models import ParkingLot
from parkinglot.tests.stub_methods import create_car


class ParkingLotTestCase(TestCase):
    """
    Testcases to create ParkingLot model object creation
    """

    def setUp(self):
        """
        Make test database ready to run each test
        """
        ParkingLot.flush()

    def test_creation(self):
        """
        Create a ParkingLot object
        """
        parkinglot = ParkingLot(6)
        self.assertNotEqual(None, parkinglot)
        self.assertIsInstance(parkinglot, ParkingLot)
        self.assertEqual(6, parkinglot.get_capacity())

    def test_park_unpark(self):
        """
        Create a ParkingLot object and check park and unpark function
        """
        parkinglot = ParkingLot(6)
        self.assertNotEqual(None, parkinglot)
        self.assertIsInstance(parkinglot, ParkingLot)
        self.assertEqual(6, parkinglot.get_capacity())
        self.assertEqual(True, parkinglot.is_empty())
        car = create_car()
        parkinglot.park(car)
        self.assertEqual(parkinglot.is_full(), False)
        self.assertEqual(parkinglot.is_empty(), False)
        self.assertEqual(parkinglot.get_availability(), parkinglot.get_capacity() - 1)
        self.assertNotEqual({}, parkinglot.get_slot_vehicle_map())
        self.assertEqual(True, parkinglot.unpark(1))
        self.assertEqual(parkinglot.get_availability(), parkinglot.get_capacity())
        self.assertEqual(False, parkinglot.is_full())
        self.assertEqual(True, parkinglot.is_empty())

    def test_from_color(self):
        """
        Create a ParkingLot object and check color combination function
        """
        parkinglot = ParkingLot(6)
        self.assertNotEqual(None, parkinglot)
        self.assertIsInstance(parkinglot, ParkingLot)
        self.assertEqual(6, parkinglot.get_capacity())
        self.assertEqual(True, parkinglot.is_empty())
        parkinglot.park(create_car("KA-01-HH-2701", "Blue"))
        parkinglot.park(create_car("KA-01-HH-2702", "Blue"))
        parkinglot.park(create_car("KA-01-HH-2703", "Black"))
        parkinglot.park(create_car("KA-01-HH-2704", "Red"))
        self.assertEqual(["KA-01-HH-2701", "KA-01-HH-2702"], parkinglot.get_reg_num_from_color("Blue"))
        self.assertEqual(3, parkinglot.get_slot_no_from_reg_no("KA-01-HH-2703"))
        self.assertEqual([4], parkinglot.get_slot_nums_from_color("Red"))
