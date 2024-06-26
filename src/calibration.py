calibration_table = sorted(set(
    (value_ps10, psi) for value_ps10, psi in [
        (0, 0),
        (10200, 0),

        # 5 psi
        (15139, 5),
        (15139, 5),
        (15043, 5),
        (15203, 5),
        (15059, 5),
        (15091, 5),
        (15155, 5),
        (15043, 5),
        (15187, 5),
        (15107, 5),
        (15027, 5),
        (15059, 5),

        # 10 psi
        (17076, 10),
        (17108, 10),
        (17156, 10),
        (17156, 10),
        (17204, 10),
        (17140, 10),
        (17220, 10),
        (17236, 10),
        (17172, 10),
        (17188, 10),
        (17092, 10),

        # 20 psi
        (22725, 20),
        (22773, 20),
        (22661, 20),
        (22789, 20),
        (22693, 20),
        (22709, 20),
        (22757, 20),
        (22693, 20),
        (22805, 20),
        (22725, 20),
        (22677, 20),
        (22757, 20),
        (22725, 20),
        (22805, 20),
        (22725, 20),

        # 30 psi
        (27846, 30),
        (28006, 30),
        (27958, 30),
        (27910, 30),
        (27990, 30),
        (27942, 30),
        (27862, 30),
        (27862, 30),
        (27910, 30),
        (27846, 30),
        (27910, 30),
        (27974, 30),

        # 40 psi
        (32904, 40),
        (32776, 40),
        (32840, 40),
        (32727, 40),
        (32792, 40),
        (32695, 40),
        (32759, 40),
        (32776, 40),
        (32840, 40),
        (32808, 40),
        (32711, 40),
        (32840, 40),
        (32840, 40),
        (32808, 40),
        (32808, 40),
        (32824, 40),
        (32840, 40),

        # 50 psi
        (38425, 50),
        (38297, 50),
        (38409, 50),
        (38409, 50),
        (38425, 50),
        (38425, 50),
        (38377, 50),
        (38393, 50),
        (38425, 50),
        (38489, 50),
        (38441, 50),
        (38425, 50),
        (38345, 50),
        (38409, 50),
        (38329, 50),
        (38329, 50),
        (38377, 50),

        # 60 psi
        (43082, 60),
        (43114, 60),
        (43162, 60),
        (43130, 60),
        (43146, 60),
        (43034, 60),
        (43258, 60),
        (43082, 60),
        (43050, 60),
        (43050, 60),
        (43098, 60),
        (43098, 60),
        (43130, 60),
        (43194, 60),
        (43098, 60),
        (43066, 60),
        (43130, 60),
        (43082, 60),

        # 70 psi
        (48107, 70),
        (48155, 70),
        (48203, 70),
        (48155, 70),
        (48107, 70),
        (48075, 70),
        (48139, 70),
        (48155, 70),
        (48139, 70),
        (48107, 70),
        (48171, 70),
        (48043, 70),
        (48107, 70),
        (48155, 70),
        (48043, 70),
        (48091, 70),
        (48091, 70),
        (48091, 70),

        # 79 psi
        (52236, 79),
        (52172, 79),
        (52140, 79),
        (52108, 79),
        (52060, 79),
        (52140, 79),
        (52220, 79),
        (52172, 79),
        (52220, 79),
        (52060, 79),
        (52076, 79),
        (51724, 79),
        (51740, 79),
        (52140, 79),
        (52060, 79),
        (52076, 79),
        (52124, 79),
    ]
))


def convert_ps10_to_psi(ps10_value):
    low_point = None
    high_point = None

    for value_ps10, psi in calibration_table:
        if value_ps10 <= ps10_value:
            low_point = (value_ps10, psi)
        else:
            high_point = (value_ps10, psi)
            break

    if low_point is None or high_point is None:
        return None

    x0, y0 = low_point
    x1, y1 = high_point
    psi = y0 + (y1 - y0) * (ps10_value - x0) / (x1 - x0)
    return psi


def convert_psi_to_kgfcm2(psi_value):
    return round((psi_value*0.070307), 2)


def convert_psi_to_bar(psi_value):
    return round((psi_value*0.0689476), 2)
