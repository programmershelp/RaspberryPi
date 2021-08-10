from sense_hat import SenseHat
sense = SenseHat()

while True:
    temp = sense.get_temperature()
    pres = sense.get_pressure()
    humi = sense.get_humidity()

    temp = round(temp, 1)
    pres = round(pres, 1)
    humi = round(humi, 1)

    msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(temp,pres,humi)

    sense.show_message(msg, scroll_speed=0.05)