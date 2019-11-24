import sys

from parkinglot.handlers import ParkingHandler
from parkinglot.logger import logger
from parkinglot.service import ParkingServiceImpl


def command_mode(handler: ParkingHandler):
    """
    Handler fot command mode
    """
    while True:
        try:
            input_cmd = input()
            if input_cmd == "exit":
                break
            if handler.validate(input_cmd):
                handler.execute(input_cmd)
            else:
                print("Invalid Input. Please Try Again!!!")
        except Exception as e:
            logger.exception(e)
            break


def file_reader_mode(handler: ParkingHandler, file_name: str):
    """
    Handler for file mode
    """
    with open(file_name) as file:
        commands = file.readlines()
        for input_cmd in commands:
            input_cmd = input_cmd.strip()
            if handler.validate(input_cmd):
                handler.execute(input_cmd)


def main(args):
    """
    Main function: entry point of the application
    """
    handler = ParkingHandler()
    handler.set_service(ParkingServiceImpl())
    try:
        if len(args) == 1:
            command_mode(handler)
            return 0
        elif len(args) == 2:
            file_reader_mode(handler, args[1])
            return 0
        else:
            print("Invalid Input. Please refer README.md for usage")
        print("Program Exited!!!!!!")
    except Exception as e:
        logger.exception(e)
        return -1


if __name__ == '__main__':
    args = sys.argv
    main(args)
