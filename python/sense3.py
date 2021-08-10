from sense_hat import SenseHat
sense = SenseHat()

while True:
    temp = sense.get_temperature()
    temp = round(temp, 1)

    if temp < 35:
        bg = (0, 100, 0)  # green
    else:
        bg = (100, 0, 0)  # red

    msg = "Temperature = {0}".format(temp)
    sense.show_message(msg, scroll_speed=0.05, back_colour=bg)
