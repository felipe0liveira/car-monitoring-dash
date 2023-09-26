import ssd1306
import machine
import machine

WIDTH = 128
HEIGHT = 64

i2c = machine.I2C(0)

oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

digit_initial_x_px = [0, 0, 52, 93]

digit_max_width = 35
digit_max_height = 64
digit_thicknes = 10

# oled.fill_rect(38, 53, 11, 11, 1)  # point

# NUMBER 0

# Number 0 at position 1
# oled.fill_rect(0, 0, 35, digit_thicknes, 1) # up
# oled.fill_rect(25, 0, digit_thicknes, 64, 1) # right
# oled.fill_rect(0, 54, 35, digit_thicknes, 1) # bottom
# oled.fill_rect(0, 0, digit_thicknes, 64, 1) # left

# Number 0 at position 2
# oled.fill_rect(52, 0, 35, digit_thicknes, 1) # up
# oled.fill_rect(77, 0, digit_thicknes, 64, 1) # right
# oled.fill_rect(52, 54, 35, digit_thicknes, 1) # bottom
# oled.fill_rect(52, 0, digit_thicknes, 64, 1) # left

# Number 0 at position 3
# oled.fill_rect(93, 0, 35, digit_thicknes, 1) # up
# oled.fill_rect(118, 0, digit_thicknes, 64, 1) # right
# oled.fill_rect(93, 54, 35, digit_thicknes, 1) # bottom
# oled.fill_rect(93, 0, digit_thicknes, 64, 1) # left

# NUMBER 1

# Number 1 at position 1
# oled.fill_rect(25, 0, digit_thicknes, 64, 1)

# Number 1 at position 2
# oled.fill_rect(77, 0, digit_thicknes, 64, 1)

# Number 1 at position 3
# oled.fill_rect(118, 0, digit_thicknes, 64, 1)

# NUMBER 2

# Number 2 at position 2
# oled.fill_rect(52, 0, 35, digit_thicknes, 1)
# oled.fill_rect(87 - digit_thicknes, 0, digit_thicknes, int(HEIGHT/2), 1)
# oled.fill_rect(52, int(HEIGHT/2) - int(digit_thicknes/2), 35, digit_thicknes, 1)
# oled.fill_rect(52, int(HEIGHT/2) - int(digit_thicknes/2),
#                digit_thicknes, int(HEIGHT/2), 1)
# oled.fill_rect(52, HEIGHT - digit_thicknes, 35, digit_thicknes, 1)

# Number 2 at position 3
# oled.fill_rect(93, 0, 35, digit_thicknes, 1)
# oled.fill_rect(128 - digit_thicknes, 0, digit_thicknes, int(HEIGHT/2), 1)
# oled.fill_rect(93, int(HEIGHT/2) - int(digit_thicknes/2), 35, digit_thicknes, 1)
# oled.fill_rect(93, int(HEIGHT/2) - int(digit_thicknes/2),
#                digit_thicknes, int(HEIGHT/2), 1)
# oled.fill_rect(93, HEIGHT - digit_thicknes, 35, digit_thicknes, 1)


def draw_single_number(num, position=1):
    if num == "0":
        # Number 0 at position 1
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
                       0, digit_thicknes, int(digit_max_height/2), 1)
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_max_width, digit_thicknes, 1)
        oled.fill_rect(digit_initial_x_px[position], int(digit_max_height/2) - int(digit_thicknes/2),
                       digit_thicknes, int(digit_max_height/2), 1)
        oled.fill_rect(digit_initial_x_px[position], digit_max_height -
                       digit_thicknes, digit_max_width, digit_thicknes, 1)


def draw_float(float_num=0.00, starting_x=0):
    my_formatter = "{0:.2f}"
    output = my_formatter.format(float_num)

    num1 = output[0]
    num2 = output[2]
    num3 = output[3]

    print([num1, num2, num3])

    # Draw a point
    oled.fill_rect(38, 53, 11, 11, 1)
    # draw_single_number(num1, 1)
    # draw_single_number(num2, 2)
    draw_single_number(num3, 3)
    oled.show()


draw_float(2.22)
