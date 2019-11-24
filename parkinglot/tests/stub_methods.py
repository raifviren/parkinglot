from parkinglot.models import Car

def create_car(reg_no=None,color=None):
    if reg_no and color:
        return Car(reg_no, color)
    else:
        return Car("KA-01-HH-1234", "White")


def create_car_black():
    return Car("KA-01-HH-9999" ,"Black")


def create_car_red():
    return Car("KA-01-HH-7777", "Red")
