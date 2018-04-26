import time
import pigpio

gpio = pigpio.pi()
RELAY_OFF = 1
RELAY_ON = 0
pins = [ 17, 18, 27, 22 ]
for pin in pins:
    print("Setting pin %d to output" % pin)
    gpio.set_mode(pin, pigpio.OUTPUT)

    print("Clearing pull up/down resisitor on pin %d" % pin)
    gpio.set_pull_up_down(pin, pigpio.PUD_OFF)

    print("Reading and toggling pin %d" % pin)
    current_state = gpio.read(pin)
    if current_state == RELAY_OFF:
        print("Pin %d is currently off" % pin)
        time.sleep(2)
        print("Turning pin %d on (%d)" % (pin, gpio.read(pin)))
        gpio.write(pin, RELAY_ON)
    else:
        print("Pin %d is currently on" % pin)
    time.sleep(2)

    print("Turning pin %d off (%d)" % (pin, gpio.read(pin)))
    gpio.write(pin, RELAY_OFF)
    time.sleep(2)
    print

