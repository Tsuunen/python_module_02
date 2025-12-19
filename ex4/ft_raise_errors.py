def check_plant_health(plant_name, water_level, sunlight_hours):
    if (plant_name == ""):
        print("Error: Plant name cannot be empty!")
        raise ValueError
    elif (water_level < 1):
        print(f"Error: Water level {water_level} is too low (min 1)")
        raise ValueError
    elif (water_level > 10):
        print(f"Error: Water level {water_level} is too high (max 10)")
        raise ValueError
    elif (sunlight_hours < 2):
        print(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
        raise ValueError
    elif (sunlight_hours > 12):
        print(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
        raise ValueError
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 1, 2)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 1, 2)
    except ValueError:
        pass
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 2)
    except ValueError:
        pass
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 1, 0)
    except ValueError:
        pass
    print("\nAll error raising tests completed!")
