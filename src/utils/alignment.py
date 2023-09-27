import src.constants.display as display_const


def centered_x(text):
    return int((display_const.WIDTH/2) - (len(text)/2*display_const.CHAR_SIZE))
