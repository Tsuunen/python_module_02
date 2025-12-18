class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self):
        super().__init__("The tomato plant is wilting!")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


def test():
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError()
    except PlantError as e:
        print("Caught PlantError:", e)
    print()
    try:
        print("Testing WaterError...")
        raise WaterError()
    except WaterError as e:
        print("Caught WaterError:", e)
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as e:
        print("Caught a garden error:", e)
    try:
        raise WaterError()
    except GardenError as e:
        print("Caught a garden error:", e)
    print("\nAll custom error types work correctly!")


if (__name__ == "__main__"):
    test()
