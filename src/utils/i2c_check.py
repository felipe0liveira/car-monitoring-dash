import machine

i2c = machine.I2C(0)
print(i2c)

print("Available i2c Devices: " + str(i2c.scan()))
