def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check if water_level and sunlight_hours are correct"""
    if (plant_name == ""):
        print("Error: Plant name cannot be empty!")
        raise ValueError
    elif (water_level < 1):
        raise ValueError(f"Error: Water level {water_level} is too low \
(min 1)")
    elif (water_level > 10):
        raise ValueError(
            f"Error: Water level {water_level} is too high (max 10)")
    elif (sunlight_hours < 2):
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    elif (sunlight_hours > 12):
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """test the check_plant_health() function"""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    print(check_plant_health("tomato", 1, 2))
    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 1, 2))
    except ValueError as e:
        print(e)
    print("Testing bad water level...")
    try:
        print(check_plant_health("tomato", 15, 2))
    except ValueError as e:
        print(e)
    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 1, 0))
    except ValueError as e:
        print(e)
    print("\nAll error raising tests completed!")


test_plant_checks()
