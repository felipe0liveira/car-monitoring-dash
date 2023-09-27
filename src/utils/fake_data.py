import random

default_value_format = "{0:.2f}"


def get_lambda_data():
    second = random.randint(80, 99)
    return default_value_format.format(float("0." + str(second)))


def get_oil_pressure_data():
    first = random.randint(1, 9)
    second = random.randint(60, 99)
    return default_value_format.format(float(str(first) + "." + str(second)))


def get_fuel_pressure_data():
    first = random.randint(1, 9)
    second = random.randint(60, 99)
    return default_value_format.format(float(str(first) + "." + str(second)))


def get_map_data():
    first = random.randint(1, 5)
    second = random.randint(60, 99)
    return default_value_format.format(float(str(first) + "." + str(second)))


def get_water_temperature_data():
    return random.randint(5, 140)
