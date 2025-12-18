def garden_operations(action: str):
    dic: dict = dict()

    if (action == "value"):
        int("sdfs")
    elif (action == "zero"):
        3 / 0
    elif (action == "file"):
        open("missing.txt")
    elif (action == "key"):
        dic["missing/_plant"]
    else:
        int("sdfs")
        3 / 0
        open("missing.txt")
        dic["missing/_plant"]


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        garden_operations("value")
    except ValueError as e:
        print("Caught ValueError:", e)
    print()
    try:
        print("Testing ZeroDivisionError...")
        garden_operations("zero")
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    print()
    try:
        print("Testing FileNotFoundError...")
        garden_operations("file")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
    print()
    try:
        print("Testing KeyError...")
        garden_operations("key")
    except KeyError as e:
        print("Caught KeyError:", e)
    print()
    try:
        print("Testing multiple errors together...")
        garden_operations("")
    except Exception:
        print("Caught an error but program continues!")
    print()
    print("All error types tested successfully!")
