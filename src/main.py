import external_modules.ssd1306 as ssd1306
import machine
import random
import time

WIDTH = 128
HEIGHT = 64

i2c = machine.I2C(0)

oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

digit_initial_x_px = [0, 0, 52, 93]

digit_max_width = 35
digit_max_height = 64
digit_thicknes = 10


def draw_single_number(num, position=1):
    if num == "0":
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_max_width, digit_thicknes, 1)  # up
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0,
                       digit_thicknes, digit_max_height, 1)  # right
        oled.fill_rect(digit_initial_x_px[position],
                       digit_max_height - digit_thicknes, digit_max_width, digit_thicknes, 1)  # bottom
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_thicknes, digit_max_height, 1)  # left

    elif num == "1":
        oled.fill_rect(
            digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0, digit_thicknes, digit_max_height, 1)

    elif num == "2":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, 1)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes,
                       0, digit_thicknes, int(digit_max_height/2), 1)  # half up right
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, 1)
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_thicknes, int(digit_max_height/2), 1)
        oled.fill_rect(digit_initial_x_px[position], digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, 1)

    elif num == "3":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, 1)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0,
                       digit_thicknes, digit_max_height, 1)  # right
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, 1)
        oled.fill_rect(digit_initial_x_px[position], digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, 1)

    elif num == "4":
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_thicknes, int(digit_max_height/2) - int(digit_thicknes/2), 1)  # half up left
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0,
                       digit_thicknes, digit_max_height, 1)  # right
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, 1)

    elif num == "5":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, 1)
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_thicknes, int(digit_max_height/2) - int(digit_thicknes/2), 1)  # half up left
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, 1)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes,
                       int(digit_max_height/2), digit_thicknes, digit_max_height, 1)  # half bottom right
        oled.fill_rect(digit_initial_x_px[position], digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, 1)

    elif num == "6":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, 1)
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_thicknes, digit_max_height, 1)
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, 1)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes,
                       int(digit_max_height/2), digit_thicknes, digit_max_height, 1)  # half bottom right
        oled.fill_rect(digit_initial_x_px[position], digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, 1)

    elif num == "7":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, 1)
        oled.fill_rect(
            digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0, digit_thicknes, digit_max_height, 1)

    elif num == "8":
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_max_width, digit_thicknes, 1)  # up
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0,
                       digit_thicknes, digit_max_height, 1)  # right
        oled.fill_rect(digit_initial_x_px[position],
                       digit_max_height - digit_thicknes, digit_max_width, digit_thicknes, 1)  # bottom
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_thicknes, digit_max_height, 1)  # left
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, 1)  # mid full width

    elif num == "9":
        oled.fill_rect(
            digit_initial_x_px[position], 0, digit_max_width, digit_thicknes, 1)
        oled.fill_rect(digit_initial_x_px[position] + digit_max_width - digit_thicknes, 0,
                       digit_thicknes, digit_max_height, 1)  # right
        oled.fill_rect(digit_initial_x_px[position], 0,
                       digit_thicknes, int(digit_max_height/2) - int(digit_thicknes/2), 1)  # half up left
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, 1)


def draw_float(float_num=0.00, starting_x=0):
    my_formatter = "{0:.2f}"
    output = my_formatter.format(float_num)

    num1 = output[0]
    num2 = output[2]
    num3 = output[3]

    oled.fill_rect(38, 53, 11, 11, 1)  # floating point

    draw_single_number(num1, 1)
    draw_single_number(num2, 2)
    draw_single_number(num3, 3)


def main():
    oled.fill(1)
    first_line = "SANJATUNING"
    second_line = "Monitor v1.0"
    oled.text(first_line, int((WIDTH/2) - (len(first_line)/2*8)), 22, 0)
    oled.text(second_line, int((WIDTH/2) - (len(second_line)/2*8)), 32, 0)

    oled.show()
    time.sleep(3)
    while True:
        second = random.randint(70, 98)
        float_number = float("0." + str(second))
        oled.fill(0)
        draw_float(float_number)
        oled.show()
        time.sleep_ms(100)


main()
