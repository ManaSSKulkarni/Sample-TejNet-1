"""SAMPLE 1"""

n = int(input("Enter a number="))
for i in range(1, 11):
    print(n, "*", i, "=", n * i)


def parse_logs(logfile):
    """Parse a log file and return lines containing ERROR messages."""

    with open(logfile, "r", encoding="utf-8") as file:
        logs = file.readlines()

    error_logs = [log for log in logs if "ERROR" in log]
    return error_logs


inventory = {"Switch1": {"id": 102, "status": "inactive", "location": "Building A"}}


def add_equipment(name, id1, status, location):
    """Adding equipment"""
    inventory[name] = {"id": id1, "status": status, "location": location}
    printinventory()


def printinventory():
    """Printing Details"""
    for device, details in inventory.items():
        print(f"{device}:{details}")


add_equipment("Switch2", 104, "active", "Building B")
