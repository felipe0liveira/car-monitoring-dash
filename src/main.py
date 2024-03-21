import src.external_modules.ssd1306 as ssd1306
import calibration
import machine
import time

# Display Settings
i2c = machine.I2C(0)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Led Settings
led_pin = 25
led = machine.Pin(led_pin, machine.Pin.OUT)
led.on()  # to sinalize ON state

# PS10
ps10_map = machine.ADC(1)
ps10_oil = machine.ADC(2)
ps10_fuel = machine.ADC(3)


def get_pressures():
    # TURBO MAP
    engunity = ps10_map.read_u16()
    psi = calibration.convert_ps10_to_psi(engunity)
    pressure = 'OUTRANGE'
    unity = ''

    if psi is not None:
        pressure = calibration.convert_psi_to_kgfcm2(psi)
        unity = 'kg'

    print('\nMAP: {} {} | psi: {} | engunity: {}'.format(
        pressure, unity, psi, engunity))

    turbo_map = pressure, unity

    # OIL PRESSURE
    engunity = ps10_oil.read_u16()
    psi = calibration.convert_ps10_to_psi(engunity)
    pressure = 'OUTRANGE'
    unity = ''

    if psi is not None:
        pressure = calibration.convert_psi_to_bar(psi)
        unity = 'kg'

    print('\nMAP: {} {} | psi: {} | engunity: {}'.format(
        pressure, unity, psi, engunity))

    oil = pressure, unity

    # FUEL PRESSURE
    engunity = ps10_fuel.read_u16()
    psi = calibration.convert_ps10_to_psi(engunity)
    pressure = 'OUTRANGE'
    unity = ''

    if psi is not None:
        pressure = calibration.convert_psi_to_bar(psi)
        unity = 'kg'

    print('\nMAP: {} {} | psi: {} | engunity: {}'.format(
        pressure, unity, psi, engunity))

    fuel = pressure, unity

    return turbo_map, oil, fuel


while True:
    time.sleep_ms(100)

    turbo, oil, fuel = get_pressures()

    map_pressure, map_unity = turbo
    oil_pressure, oil_unity = oil
    fuel_pressure, fuel_unity = fuel

    warning = (map_pressure == 'OUTRANGE' or map_pressure > 1) or \
        (oil_pressure == 'OUTRANGE' or oil_pressure < 1) or \
        (fuel_pressure == 'OUTRANGE' or fuel_pressure < 1)

    color = (0, 1) if warning else (1, 0)

    oled.fill(color[1])
    oled.text('MAP:  {} {}'.format(map_pressure, map_unity), 0, 10, color[0])
    oled.text('OIL:  {} {}'.format(oil_pressure, oil_unity), 0, 30, color[0])
    oled.text('FUEL: {} {}'.format(
        fuel_pressure, fuel_unity), 0, 50, color[0])

    oled.show()
