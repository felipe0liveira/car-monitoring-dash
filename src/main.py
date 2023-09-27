import external_modules.ssd1306 as ssd1306
import machine
import random
import time

# Constants
LAMBDA_TARGET_LIMIT = 0.97
OIL_PRESSURE_TARGET_LIMIT = 1
FUEL_PRESSURE_TARGET_LIMIT = 3

# Display Settings
WIDTH = 128
HEIGHT = 64

i2c = machine.I2C(0)

oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

digit_initial_x_px = [0, 0, 52, 93]

digit_y_start = 0
digit_max_width = 35
digit_max_height = 64
digit_thicknes = 10

# Led Settings
led_pin = 13
led = machine.Pin(led_pin, machine.Pin.OUT)

# Button Settings
button_pin = 24
button = machine.Pin(button_pin, machine.Pin.IN)

# Display Mode
DISPLAY_MODES = ["COMBINED", "LAMBDA", "OIL PRESSURE", "FUEL PRESSURE"]

default_value_format = "{0:.2f}"


def draw_single_number(num, position=1, color=1):
    if num == "0":
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_max_width, digit_thicknes, color)  # up
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0,
                       digit_thicknes, digit_max_height, color)  # right
        oled.fill_rect(digit_initial_x_px[position],
                       digit_max_height - digit_thicknes, digit_max_width, digit_thicknes, color)  # bottom
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_thicknes, digit_max_height, color)  # left

    elif num == "1":
        oled.fill_rect(
            digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0, digit_thicknes, digit_max_height, color)

    elif num == "2":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes,
                       0, digit_thicknes, int(digit_max_height/2), color)  # half up right
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_thicknes, int(digit_max_height/2), color)
        oled.fill_rect(digit_initial_x_px[position], digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, color)

    elif num == "3":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0,
                       digit_thicknes, digit_max_height, color)  # right
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position], digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, color)

    elif num == "4":
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_thicknes, int(digit_max_height/2) - int(digit_thicknes/2), color)  # half up left
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0,
                       digit_thicknes, digit_max_height, color)  # right
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)

    elif num == "5":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_thicknes, int(digit_max_height/2) - int(digit_thicknes/2), color)  # half up left
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes,
                       int(digit_max_height/2), digit_thicknes, digit_max_height, color)  # half bottom right
        oled.fill_rect(digit_initial_x_px[position], digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, color)

    elif num == "6":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_thicknes, digit_max_height, color)
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes,
                       int(digit_max_height/2), digit_thicknes, digit_max_height, color)  # half bottom right
        oled.fill_rect(digit_initial_x_px[position], digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, color)

    elif num == "7":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, color)
        oled.fill_rect(
            digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0, digit_thicknes, digit_max_height, color)

    elif num == "8":
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_max_width, digit_thicknes, color)  # up
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0,
                       digit_thicknes, digit_max_height, color)  # right
        oled.fill_rect(digit_initial_x_px[position],
                       digit_max_height - digit_thicknes, digit_max_width, digit_thicknes, color)  # bottom
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_thicknes, digit_max_height, color)  # left
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)  # mid full width

    elif num == "9":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0,
                       digit_thicknes, digit_max_height, color)  # right
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_thicknes, int(digit_max_height/2) - int(digit_thicknes/2), color)  # half up left
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)


def draw_float(float_num=0.00, color=1):
    output = default_value_format.format(float_num)

    num1 = output[0]
    num2 = output[2]
    num3 = output[3]

    oled.fill_rect(38, 53, 11, 11, color)  # floating point

    draw_single_number(num1, 1, color)
    draw_single_number(num2, 2, color)
    draw_single_number(num3, 3, color)


def get_lambda_data():
    second = random.randint(60, 99)
    return default_value_format.format(float("0." + str(second)))


def get_oil_pressure_data():
    first = random.randint(6, 9)
    second = random.randint(60, 99)
    return default_value_format.format(float(str(first) + "." + str(second)))


def get_fuel_pressure_data():
    first = random.randint(1, 9)
    second = random.randint(60, 99)
    return default_value_format.format(float(str(first) + "." + str(second)))


def centered_x(text):
    return int((WIDTH/2) - (len(text)/2*8))


def main():
    display_selector = 0

    oled.fill(1)
    first_line = "SANJATUNING"
    second_line = "Monitor v1.0"
    oled.text(first_line, centered_x(first_line), 22, 0)
    oled.text(second_line, centered_x(second_line), 32, 0)

    oled.show()
    time.sleep(1)

    while True:
        print(display_selector)
        print(DISPLAY_MODES[display_selector])

        if button.value() == 1:
            next_display_selector = display_selector + 1

            if next_display_selector == len(DISPLAY_MODES):
                next_display_selector = 0

            display_selector = next_display_selector

            current_title = DISPLAY_MODES[display_selector]
            oled.fill(1)
            oled.text(current_title, centered_x(current_title), 28, 0)
            oled.show()

            time.sleep(1)

        oled.fill(0)

        if display_selector == 0:
            lambda_value = get_lambda_data()
            oled.text("Wideband", 0, 0, 1)
            oled.text(lambda_value, WIDTH - (len(lambda_value)*8), 0, 1)

            oil_pressure_value = get_oil_pressure_data()
            oled.text("Oil", 0, 28, 1)
            oled.text(oil_pressure_value, WIDTH -
                      (len(oil_pressure_value)*8), 28, 1)

            fuel_pressure_value = get_fuel_pressure_data()
            oled.text("Fuel", 0, 56, 1)
            oled.text(fuel_pressure_value, WIDTH -
                      (len(fuel_pressure_value)*8), 56, 1)

        if display_selector == 1:
            lambda_value = get_lambda_data()
            draw_float(float(lambda_value), 1)

            led.off()

            if float(lambda_value) > LAMBDA_TARGET_LIMIT:
                led.on()

        if display_selector == 2:
            oil_pressure_value = get_oil_pressure_data()
            draw_float(float(oil_pressure_value), 1)

            led.off()

            if float(oil_pressure_value) < OIL_PRESSURE_TARGET_LIMIT:
                led.on()

        if display_selector == 3:
            fuel_pressure_value = get_fuel_pressure_data()
            draw_float(float(fuel_pressure_value), 1)

            led.off()

            if float(fuel_pressure_value) < OIL_PRESSURE_TARGET_LIMIT:
                led.on()

        time.sleep_ms(100)

        oled.show()


main()
