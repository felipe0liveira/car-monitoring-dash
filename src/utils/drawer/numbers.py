_x_start = [0, 0, 52, 93]
_y_start = 12
_width = 35
_height = 52
_thicknes = 10


def draw_single_number(draw_cb, num, position=1, color=1):
    setup = []
    if num == "0":
        setup = [(_x_start[position], _y_start, _width, _thicknes, color),
                 (_x_start[position] + _width - _thicknes,
                 _y_start, _thicknes, _height, color),
                 (_x_start[position], _y_start + _height -
                 _thicknes, _width, _thicknes, color),
                 (_x_start[position], _y_start, _thicknes, _height, color)]

    elif num == "1":
        setup = [(
            _x_start[position] + _width - _thicknes, _y_start, _thicknes, _height, color)]

    elif num == "2":
        setup = [(_x_start[position], _y_start, _width, _thicknes, color),
                 (_x_start[position] + _width - _thicknes,
                 _y_start, _thicknes, int(_height/2), color),
                 (_x_start[position], _y_start + int(_height/2) - int(_thicknes/2),
                 _width, _thicknes, color),
                 (_x_start[position], _y_start + int(_height/2) - int(_thicknes/2),
                 _thicknes, int(_height/2), color),
                 (_x_start[position], _y_start + _height -
                 _thicknes, _width, _thicknes, color)]

    elif num == "3":
        setup = [(
            _x_start[position], _y_start, _width, _thicknes, color),
            (_x_start[position] + _width - _thicknes, _y_start,
             _thicknes, _height, color),
            (_x_start[position], _y_start + int(_height/2) - int(_thicknes/2),
             _width, _thicknes, color),
            (_x_start[position], _y_start+_height -
             _thicknes, _width, _thicknes, color)]

    elif num == "4":
        setup = [(_x_start[position], _y_start,
                 _thicknes, int(_height/2) - int(_thicknes/2), color),
                 (_x_start[position] + _width - _thicknes, _y_start,
                 _thicknes, _height, color),
                 (_x_start[position], _y_start + int(_height/2) - int(_thicknes/2),
                 _width, _thicknes, color)]

    elif num == "5":
        setup = [(
            _x_start[position], _y_start, _width, _thicknes, color),
            (_x_start[position], _y_start,
             _thicknes, int(_height/2) - int(_thicknes/2), color),
            (_x_start[position], _y_start+int(_height/2) - int(_thicknes/2),
             _width, _thicknes, color),
            (_x_start[position] + _width - _thicknes,
             _y_start + int(_height/2), _thicknes, _height, color),
            (_x_start[position], _y_start + _height -
             _thicknes, _width, _thicknes, color)]

    elif num == "6":
        setup = [(
            _x_start[position], _y_start, _width, _thicknes, color),
            (_x_start[position], _y_start,
             _thicknes, _height, color),
            (_x_start[position], _y_start + int(_height/2) - int(_thicknes/2),
             _width, _thicknes, color),
            (_x_start[position] + _width - _thicknes,
             _y_start + int(_height/2), _thicknes, _height, color),
            (_x_start[position], _y_start + _height -
             _thicknes, _width, _thicknes, color)]

    elif num == "7":
        setup = [(
            _x_start[position], _y_start, _width, _thicknes, color),
            (
            _x_start[position] + _width - _thicknes, _y_start, _thicknes, _height, color)]

    elif num == "8":
        setup = [(_x_start[position], _y_start,
                 _width, _thicknes, color),
                 (_x_start[position] + _width - _thicknes, _y_start,
                 _thicknes, _height, color),
                 (_x_start[position],
                 _y_start + _height - _thicknes, _width, _thicknes, color),
                 (
            _x_start[position], _y_start, _thicknes, _height, color),
            (_x_start[position], _y_start + int(_height/2) - int(_thicknes/2),
             _width, _thicknes, color)]

    elif num == "9":
        setup = [(
            _x_start[position], _y_start, _width, _thicknes, color),
            (_x_start[position] + _width - _thicknes, _y_start,
             _thicknes, _height, color),
            (_x_start[position], _y_start,
             _thicknes, int(_height/2) - int(_thicknes/2), color),
            (_x_start[position], _y_start + int(_height/2) - int(_thicknes/2),
             _width, _thicknes, color)]

    for config in setup:
        draw_cb(*config)
