from parkinglot.models import Car


def create_car(reg_no=None, color=None):
    if reg_no and color:
        return Car(reg_no, color)
    else:
        return Car("KA-01-HH-1234", "White")


class DummyCommand:
    """
    Dummy Commands for test cases
    """
    CREATE_PARKING_LOT = "create_parking_lot 6"
    PARK = "park KA-01-HH-1234 White"
    LEAVE = "leave 4"
    STATUS = "status"
    REG_NUMBER_FOR_CARS_WITH_COLOR = "registration_numbers_for_cars_with_colour White"
    SLOT_NUMBERS_FOR_CARS_WITH_COLOR = "slot_numbers_for_cars_with_colour White"
    SLOT_NUMBER_FOR_REG_NUMBER = "slot_number_for_registration_number KA-01-HH-1234"
