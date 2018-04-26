import subprocess
import time

import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd(1)

import SHT31_driver
temp_rh_sensor = SHT31_driver.SHT31(1)

NIC = 'wlan0'
DEGREE = chr(223)

def get_ip_address(ifname):
    cmd = "ifconfig %s |grep 'inet ' |awk '{print $2}'" % ifname
    return subprocess.check_output(cmd, shell = True)

def get_ssid(ifname):
    cmd = "iwconfig %s |grep ESSID |rev |cut -d '\"' -f2 |rev" % ifname
    return subprocess.check_output(cmd, shell = True)

def display_network_info(ssid, ip, display_seconds):
    mylcd.lcd_clear()
    if len(ssid) > 16:
        str_pad = " " * 16
        ssid = str_pad + ssid
        mylcd.lcd_display_string(ip, 1)
        for i in range (0, len(ssid)):
            lcd_text = ssid[i:(i+16)]
            mylcd.lcd_display_string(lcd_text,2)
            sleep(0.4)
            mylcd.lcd_display_string(str_pad,2)
    else:
        mylcd.lcd_display_string(IP, 1)
        mylcd.lcd_display_string(SSID, 2)
    time.sleep(display_seconds)

def display_temp_rh(readings):
    mylcd.lcd_clear()
    temperature, humidity = temp_rh_sensor.get_temp_and_humidity(unit = 'F')
    temp = int(round(temperature))
    rh = int(round(humidity))
    mylcd.lcd_display_string("Temp: %d%sF" % (temp, DEGREE), 1)
    mylcd.lcd_display_string("RH: %d %%" % rh, 2)
    time.sleep(1)

    for reading in range(1, readings):
        temperature, humidity = temp_rh_sensor.get_temp_and_humidity(unit = 'F')
        new_temp = int(round(temperature))
        new_rh = int(round(humidity))
        if new_temp != temp:
            mylcd.lcd_display_string("%d%sF" % (new_temp, DEGREE), 1, 6)
        if new_rh != rh:
            mylcd.lcd_display_string("%d %%" % new_rh, 2, 4)
        time.sleep(1)

# Start with a clean display
mylcd.lcd_clear()

while True:
    SSID = get_ssid(NIC).rstrip()
    IP = get_ip_address(NIC).rstrip()
    display_network_info(SSID, IP, 3)
    display_temp_rh(7)

