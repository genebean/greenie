# Greenie

This repo is a work in progress. Its goal is to provide some automation realted
to a greenhouse. Currently, greenie reads the temperature and humidity from an
SHT31-D and alternates showing the readings and the current network info on a
16x2 LCD.

The [utils/relay_test.py](utils/relay_test.py) shows how a set of
relays can be controled. This will be expanded on in a later version of the
code. To use relay_test.py as written you will need to install
[pigpio](http://abyz.me.uk/rpi/pigpio/). On Raspbian this can be done like so:

```
sudo apt-get update
sudo apt-get install pigpio python-pigpio python3-pigpio
```

## Parts used with this code

- 1 x Raspberry Pi Zero W
- 1 x Adafruit SHT31-D temperature and humidity sensor
- 1 x SainSmart 4-channel relay module
- 1 x Adafruit DS1307 real time clock
- 1 x CR1220 battery
- 1 x 16GB MicroSD card
- 1 x Adafruit Perma-Proto Bonnet
- 1 x 16x2 LCD with I2C backpack
- 1 x 2 gang outlet box
- 2 x 110v power outlets
- 1 x faceplate for dual outlets
- 1 x double row four position terminal block
- 1 x power tool cord


## Licensing

My code is licensed under the BSD 3-clause license. Files authored by others have license included in them.

- [lib/I2C_LCD_driver.py](lib/I2C_LCD_driver.py) has a GNU General Public License
- [lib/SHT31_driver.py](lib/SHT31_driver.py) has a MIT License
- [utils/conds.py](utils/conds.py) has a free-will license
- [utils/gpio_status.py](utils/gpio_status.py) is from the author of [pigpio](http://abyz.me.uk/rpi/pigpio/) and is unlicensed

