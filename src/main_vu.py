import src.external_modules.ssd1306 as ssd1306
import src.utils.fake_data as faker
import src.utils.math as math
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


def main():
    display_selector = 1

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

            # time.sleep(1)

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
            oled.text("WIDEBAND", alignment.centered_x("WIDEBAND"), 0, 1)
            oled.rect(0, 12, 128, 40, 1)
            oled.text(str(lambda_value),
                      alignment.centered_x(lambda_value), 56, 1)
            print(lambda_value)
            barWidth = math.remap_value(float(lambda_value), 0, 1.5, 0, 128)
            oled.fill_rect(0, 12, int(barWidth), 40, 1)
            oled.fill_rect(63, 13, 2, 39, 0 if barWidth > 63 else 1)

            led.off()

            if float(lambda_value) > targets_const.LAMBDA_TARGET_LIMIT:
                led.on()

        # time.sleep_ms(10)

        oled.show()


main()
