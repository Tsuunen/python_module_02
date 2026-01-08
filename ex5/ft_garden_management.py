class GardenError(Exception):
    """Generic Garden Erorr"""

    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    """Plant related Garden Erorr"""

    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    """Water related Garden Erorr"""

    def __init__(self, message):
        super().__init__(message)


class GardenManager:
    """GardenManager helps with managing multiple plants"""

    def __init__(self):
        self.plant_list: list(str) = []

    def add_plant(self, plant_name: str):
        """Add plant to manager"""
        if (plant_name == "" or plant_name is None):
            raise PlantError(
                "Error adding plant: Plant name cannot be empty!")
        self.plant_list.append(str(plant_name))
        print(f"Added {plant_name} successfully")

    def water_plants(self):
        """water all plants from self.plant_list"""
        print("Opening watering system")
        try:
            for i in self.plant_list:
                print("watering", i)
        except Exception:
            raise WaterError("Error: Cannot water None - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")

    def check_water_level(self):
        """Raise an error to test catching it"""
        raise WaterError("Not enough water in tank")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        """Check if plants are healthy"""
        if (plant_name == ""):
            raise PlantError(
                "Error checking {plant_name}: Plant name cannot be empty!")
        elif (water_level < 1):
            raise WaterError(
                f"Error checking {plant_name}: Water level {water_level} \
is too low (min 1)")
        elif (water_level > 10):
            raise WaterError(
                f"Error checking {plant_name}: Water level {water_level} \
is too high (max 10)")
        elif (sunlight_hours < 2):
            raise PlantError(
                f"Error checking {plant_name}: Sunlight hours \
{sunlight_hours} is too low (min 2)")
        elif (sunlight_hours > 12):
            raise PlantError(
                f"Error checking {plant_name}: Sunlight hours \
{sunlight_hours} is too high (max 12)")
        print(
            f"{plant_name}: healthy (water: {water_level}, \
sun: {sunlight_hours})")


if (__name__ == "__main__"):
    garden: GardenManager = GardenManager()
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato")
        garden.add_plant("lettuce")
        garden.add_plant("")
    except GardenError as e:
        print(e)
    print("\nWatering plants...")
    garden.water_plants()
    print("\nChecking plant health...")
    garden.check_plant_health("tomato", 5, 8)
    try:
        garden.check_plant_health("lettuce", 15, 2)
    except GardenError as e:
        print(e)
    try:
        print("\nTesting error recovery...")
        garden.check_water_level()
    except GardenError as e:
        print("Caught GardenError:", e)
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")
