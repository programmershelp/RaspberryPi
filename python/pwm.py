import RPi.GPIO as GPIO

#pin 12 on GPIO header
led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

while True:
	brightness = raw_input("Enter Brightness value (0 to 100):")
	duty_value = int(brightness)
	pwm_led.ChangeDutyCycle(duty_value)