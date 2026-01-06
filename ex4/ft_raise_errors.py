def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check if water_level and sunlight_hours are correct"""
    if (plant_name == ""):
        return ("Error: Plant name cannot be empty!")
        raise ValueError
    elif (water_level < 1):
        return (f"Error: Water level {water_level} is too low (min 1)")
        raise ValueError
    elif (water_level > 10):
        return (f"Error: Water level {water_level} is too high (max 10)")
        raise ValueError
    elif (sunlight_hours < 2):
        return (f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
        raise ValueError
    elif (sunlight_hours > 12):
        return (f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
        raise ValueError
    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """test the check_plant_health() function"""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    print(check_plant_health("tomato", 1, 2))
    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 1, 2))
    except ValueError:
        pass
    print("\nTesting bad water level...")
    try:
        print(check_plant_health("tomato", 15, 2))
    except ValueError:
        pass
    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 1, 0))
    except ValueError:
        pass
    print("\nAll error raising tests completed!")
