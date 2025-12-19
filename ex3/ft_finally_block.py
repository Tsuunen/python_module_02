def water_plants(plant_list: list):
    print("Opening watering system")
    try:
        for i in plant_list:
            if (i is None):
                0 / 0
            print("watering", i)
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")
    water_plants(["tomato", None, "carrots"])
    print("\nCleanup always happens, even with errors!")


if (__name__ == "__main__"):
    test_watering_system()
