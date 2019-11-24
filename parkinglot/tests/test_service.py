from unittest import TestCase

from parkinglot.models import ParkingLot
from parkinglot.service import ParkingServiceImpl
from parkinglot.tests.stub_methods import create_car


class ParkingServiceImplTestCase(TestCase):
    """
    Test cases to for service function ParkingServiceImpl
    """

    def setUp(self):
        """
        Make test database ready to run each test
        """
        ParkingLot.flush()

    def test_create_parking_lot(self):
        """
        Test case for create_parking_lot function
        """
        service = ParkingServiceImpl()
        service.create_parking_lot(6)
        self.assertEqual(service.validate_parking_lot(), True)

    def test_park_unpark(self):
        """
        Test case for park and unpark function
        """
        service = ParkingServiceImpl()
        service.create_parking_lot(6)
        self.assertEqual(service.validate_parking_lot(), True)
        slot_no = service.park(create_car())
        self.assertGreater(slot_no, 0)
        service.unpark(slot_no)
        self.assertEqual(6, service.get_available_slots_count())
        service.get_status()

    def test_count_functions(self):
        """
        Test case for get_reg_num_from_color, get_slot_nums_from_color and get_slot_no_from_reg_no function
        """
        service = ParkingServiceImpl()
        service.create_parking_lot(6)
        self.assertEqual(service.validate_parking_lot(), True)
        service.park(create_car("KA-01-HH-2701", "Blue"))
        service.park(create_car("KA-01-HH-2702", "Blue"))
        service.park(create_car("KA-01-HH-2703", "Black"))
        service.park(create_car("KA-01-HH-2704", "Red"))
        self.assertEqual(["KA-01-HH-2701", "KA-01-HH-2702"], service.get_reg_num_from_color("Blue"))
        self.assertEqual(3, service.get_slot_no_from_reg_no("KA-01-HH-2703"))
        self.assertEqual([4], service.get_slot_nums_from_color("Red"))
