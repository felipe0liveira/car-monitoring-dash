import src.external_modules.ssd1306 as ssd1306
import src.utils.fake_data as faker
import src.constants.targets as targets_const
import src.constants.display as display_const
import src.constants.formating as formating_const
import src.utils.alignment as alignment
import machine
import time

# Display Settings
i2c = machine.I2C(0)

oled = ssd1306.SSD1306_I2C(display_const.WIDTH, display_const.HEIGHT, i2c)

digit_initial_x_px = [0, 0, 52, 93]
digit_y_start = 12
digit_max_width = 35
digit_max_height = 52
digit_thicknes = 10

# Led Settings
led_pin = 13
led = machine.Pin(led_pin, machine.Pin.OUT)

# Button Settings
button_pin = 24
button = machine.Pin(button_pin, machine.Pin.IN)

# Display Mode
DISPLAY_MODES = ["COMBINED", "WIDEBAND", "OIL PRESSURE",
                 "FUEL PRESSURE", "MAP", "WATER TEMP",]


def draw_single_number(num, position=1, color=1):
    if num == "0":
        oled.fill_rect(digit_initial_x_px[position], digit_y_start,
                       digit_max_width, digit_thicknes, color)  # up
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, digit_y_start,
                       digit_thicknes, digit_max_height, color)  # right
        oled.fill_rect(digit_initial_x_px[position],
                       digit_y_start + digit_max_height - digit_thicknes, digit_max_width, digit_thicknes, color)  # bottom
        oled.fill_rect(
            digit_initial_x_px[position], digit_y_start, digit_thicknes, digit_max_height, color)  # left

    elif num == "1":
        oled.fill_rect(
            digit_initial_x_px[position] + digit_max_width - digit_thicknes, digit_y_start, digit_thicknes, digit_max_height, color)

    elif num == "2":
        oled.fill_rect(
            digit_initial_x_px[position], digit_y_start, digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes,
                       digit_y_start, digit_thicknes, int(digit_max_height/2), color)  # half up right
        oled.fill_rect(digit_initial_x_px[position], digit_y_start + int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position], digit_y_start + int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_thicknes, int(digit_max_height/2), color)
        oled.fill_rect(digit_initial_x_px[position], digit_y_start + digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, color)

    elif num == "3":
        oled.fill_rect(
            digit_initial_x_px[position], digit_y_start, digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, digit_y_start,
                       digit_thicknes, digit_max_height, color)  # right
        oled.fill_rect(digit_initial_x_px[position], digit_y_start + int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position], digit_y_start+digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, color)

    elif num == "4":
        oled.fill_rect(digit_initial_x_px[position], digit_y_start,
                       digit_thicknes, int(digit_max_height/2) - int(digit_thicknes/2), color)  # half up left
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, digit_y_start,
                       digit_thicknes, digit_max_height, color)  # right
        oled.fill_rect(digit_initial_x_px[position], digit_y_start + int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)

    elif num == "5":
        oled.fill_rect(
            digit_initial_x_px[position], digit_y_start, digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position], digit_y_start,
                       digit_thicknes, int(digit_max_height/2) - int(digit_thicknes/2), color)  # half up left
        oled.fill_rect(digit_initial_x_px[position], digit_y_start+int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes,
                       digit_y_start + int(digit_max_height/2), digit_thicknes, digit_max_height, color)  # half bottom right
        oled.fill_rect(digit_initial_x_px[position], digit_y_start + digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, color)

    elif num == "6":
        oled.fill_rect(
            digit_initial_x_px[position], digit_y_start, digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position], digit_y_start,
                       digit_thicknes, digit_max_height, color)
        oled.fill_rect(digit_initial_x_px[position], digit_y_start + int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes,
                       digit_y_start + int(digit_max_height/2), digit_thicknes, digit_max_height, color)  # half bottom right
        oled.fill_rect(digit_initial_x_px[position], digit_y_start + digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, color)

    elif num == "7":
        oled.fill_rect(
            digit_initial_x_px[position], digit_y_start, digit_max_width, digit_thicknes, color)
        oled.fill_rect(
            digit_initial_x_px[position] + digit_max_width - digit_thicknes, digit_y_start, digit_thicknes, digit_max_height, color)

    elif num == "8":
        oled.fill_rect(digit_initial_x_px[position], digit_y_start,
                       digit_max_width, digit_thicknes, color)  # up
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, digit_y_start,
                       digit_thicknes, digit_max_height, color)  # right
        oled.fill_rect(digit_initial_x_px[position],
                       digit_y_start + digit_max_height - digit_thicknes, digit_max_width, digit_thicknes, color)  # bottom
        oled.fill_rect(
            digit_initial_x_px[position], digit_y_start, digit_thicknes, digit_max_height, color)  # left
        oled.fill_rect(digit_initial_x_px[position], digit_y_start + int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)  # mid full width

    elif num == "9":
        oled.fill_rect(
            digit_initial_x_px[position], digit_y_start, digit_max_width, digit_thicknes, color)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, digit_y_start,
                       digit_thicknes, digit_max_height, color)  # right
        oled.fill_rect(digit_initial_x_px[position], digit_y_start,
                       digit_thicknes, int(digit_max_height/2) - int(digit_thicknes/2), color)  # half up left
        oled.fill_rect(digit_initial_x_px[position], digit_y_start + int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, color)


def draw_float(float_num=0.00, title=""):
    output = formating_const.default_value_format.format(float_num)

    num1 = output[0]
    num2 = output[2]
    num3 = output[3]

    oled.fill_rect(38, 53, 11, 11, 1)  # floating point

    draw_single_number(num1, 1, 1)
    draw_single_number(num2, 2, 1)
    draw_single_number(num3, 3, 1)

    if title != "":
        oled.fill_rect(0, 0, 128, 10, 1)
        oled.text(title, alignment.centered_x(title), 1, 0)


def draw_three_digit_int(number=100, title=""):
    output = str(number)
    if len(output) == 1:
        draw_single_number(output[0], 3, 1)

    if len(output) == 2:
        draw_single_number(output[1], 3, 1)
        draw_single_number(output[0], 2, 1)

    if len(output) == 3:
        draw_single_number(output[2], 3, 1)
        draw_single_number(output[1], 2, 1)
        draw_single_number(output[0], 1, 1)

    if title != "":
        oled.fill_rect(0, 0, 128, 10, 1)
        oled.text(title, alignment.centered_x(title), 1, 0)


def main():
    display_selector = 0

    oled.fill(1)
    first_line = "SANJATUNING"
    second_line = "Monitor v1.0"
    oled.text(first_line, alignment.centered_x(first_line), 22, 0)
    oled.text(second_line, alignment.centered_x(second_line), 32, 0)

    oled.show()
    time.sleep(3)

    while True:
        if button.value() == 1:
            led.off()
            next_display_selector = display_selector + 1

            if next_display_selector == len(DISPLAY_MODES):
                next_display_selector = 0

            display_selector = next_display_selector

            current_title = DISPLAY_MODES[display_selector]
            oled.fill(1)
            oled.text(current_title, alignment.centered_x(
                current_title), 28, 0)

            oled.show()

            time.sleep(1)

        oled.fill(0)

        if display_selector == 0:
            oled.fill_rect(0, 0, 128, 10, 1)
            oled.text("COMBINED VIEW", alignment.centered_x(
                "COMBINED VIEW"), 1, 0)

            lambda_value = faker.get_lambda_data()
            oled.text("Wideband", 0, 20, 1)
            oled.text(lambda_value, display_const.WIDTH -
                      (len(lambda_value)*8), 20, 1)

            oil_pressure_value = faker.get_oil_pressure_data()
            oled.text("Oil", 0, 35, 1)
            oled.text(oil_pressure_value, display_const.WIDTH -
                      (len(oil_pressure_value)*8), 35, 1)

            fuel_pressure_value = faker.get_fuel_pressure_data()
            oled.text("Fuel", 0, 50, 1)
            oled.text(fuel_pressure_value, display_const.WIDTH -
                      (len(fuel_pressure_value)*8), 50, 1)

        if display_selector == 1:
            lambda_value = faker.get_lambda_data()
            draw_float(float(lambda_value), "WIDEBAND")

            led.off()

            if float(lambda_value) > targets_const.LAMBDA_TARGET_LIMIT:
                led.on()

        if display_selector == 2:
            oil_pressure_value = faker.get_oil_pressure_data()
            draw_float(float(oil_pressure_value), "OIL PRESSURE")

            led.off()

            if float(oil_pressure_value) < targets_const.OIL_PRESSURE_TARGET_LIMIT:
                led.on()

        if display_selector == 3:
            fuel_pressure_value = faker.get_fuel_pressure_data()
            draw_float(float(fuel_pressure_value), "FUEL PRESSURE")

            led.off()

            if float(fuel_pressure_value) < targets_const.FUEL_PRESSURE_TARGET_LIMIT:
                led.on()

        if display_selector == 4:
            map_value = faker.get_map_data()
            draw_float(float(map_value), "MAP SUTUTU")

            led.off()

            if float(map_value) > targets_const.MAP_TARGET_LIMIT:
                led.on()

        if display_selector == 5:
            water_temp = faker.get_water_temperature_data()
            draw_three_digit_int(water_temp, "WATER TEMP.")

            led.off()

            if float(water_temp) > targets_const.WATER_TEMPERATURE_TARGET_LIMIT:
                led.on()

        time.sleep_ms(100)

        oled.show()


main()
