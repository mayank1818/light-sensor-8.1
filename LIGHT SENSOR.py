import smbus
import time
from bh1750 import BH1750

# Initialize the I2C bus (Make sure the correct bus number is used, e.g., 'smbus.SMBus(1)' or 'smbus.SMBus(0)')
bus = smbus.SMBus(1)
light_data = BH1750()

def convert_to_lux(data):
    lux = (data[1] + (256 * data[0])) / 1.2
    return lux

try:
    while True:
        light_level = light_data.measure()
        if light_level < 10:
            intensity = "Too dark"
        elif light_level < 100:
            intensity = "Dark"
        elif light_level < 1000:
            intensity = "Medium"
        elif light_level < 5000:
            intensity = "Bright"
        else:
            intensity = "Too bright"

        print('Light Intensity: {:.2f} lux ({})'.format(light_level, intensity))

        time.sleep(2)

except KeyboardInterrupt:
    print("HELLOWORLD")
