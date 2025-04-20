class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is now running \n")


my_car = Car("AUDI", "BENZ")
my_car.start_engine()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name}={self.salary}\n")

    def update(self, name2, salary2):
        self.salary = salary2
        self.name = name2


emp = Employee("Manas", 30000)
emp.display()
emp.update("Manas", 25000)
print("UPDATED:")
emp.display()


def readfile():
    try:
        with open("test.txt", "r") as file:
            content = file.readlines()
            print(
                content,
            )
    except FileNotFoundError:
        print("File not found")
    finally:
        print("File Handling done.\n")


readfile()


def convertToInt(value):
    try:
        num = int(value)
        print(f"Converted value={num}")
    except ValueError:
        print(f"ERROR: {value} could not be converted")
    finally:
        print("Conversion attempted.\n")


convertToInt("abc")


class DeviceError(Exception):
    pass


def checkStatus(status):
    try:
        if status != "y":
            raise DeviceError("NOT ONLINE !!!")
        print("Okay !")
    except DeviceError as e:
        print(e)
    finally:
        print("Status Checked.\n")


st = input("Are you online? (y/n) :")
checkStatus(st)
