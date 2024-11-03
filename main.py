from machine import Pin, PWM, ADC
import time

# Define PWM parameters
FREQUENCY = 38000    # 38kHz frequency
DUTY_CYCLE = 32768   # 50% duty cycle (32768 / 65535)

# Initialize PWM on three different pins (GPIO15, GPIO16, and GPIO17)
pwm1 = PWM(Pin(15))
pwm2 = PWM(Pin(16))
pwm3 = PWM(Pin(17))

try:
    # Set the PWM frequency and duty cycle for each pin
    for pwm in [pwm1, pwm2, pwm3]:
        pwm.freq(FREQUENCY)
        pwm.duty_u16(DUTY_CYCLE)

except KeyboardInterrupt:
    # Cleanup: stop PWM signals on each pin
    pwm1.deinit()
    pwm2.deinit()
    pwm3.deinit()

