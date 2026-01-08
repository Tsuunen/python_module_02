def water_plants(plant_list: list):
    """Water all the plants from plant_list"""
    print("Opening watering system")
    try:
        for i in plant_list:
            if (i is None):
                0 / 0
            print("watering", i)
        print("Watering completed successfully!")
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test if the watering system works"""
    print("=== Garden Watering System ===\n")
    water_plants(["tomato", "lettuce", "carrots"])
    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])
    print("\nCleanup always happens, even with errors!")


test_watering_system()
