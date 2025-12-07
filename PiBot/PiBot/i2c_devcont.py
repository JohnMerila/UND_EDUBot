import smbus2
import time

# Define I2C address and bus
AS5600_ADDR = 0x36
ANGLE_REG = 0x0E


bus = smbus2.SMBus(1)

def read_angle():
    # Read two bytes from the angle register
    raw_data = bus.read_i2c_block_data(AS5600_ADDR, ANGLE_REG, 2)
    angle = (raw_data[0] << 8) | raw_data[1]  # Combine MSB and LSB
    angle = angle & 0x0FFF  # Mask to 12 bits
    return (angle / 4096.0) * 360.0  # Convert to degrees

try:
    while True:
        angle = read_angle()
        print(f"Angle: {angle:.2f} degrees")
        time.sleep(0.05)
except KeyboardInterrupt:
    print("Exiting...")