from machine import Pin, PWM, ADC
import time

# Define PWM parameters
FREQUENCY = 38000    # 38kHz frequency
DUTY_CYCLE = 32768   # 50% duty cycle (32768 / 65535)

# Initialize PWM on pin 15
pwm1 = PWM(Pin(15))

# Set the PWM frequency and duty cycle for each pin
try:
    for pwm in [pwm1, pwm2, pwm3]:
    pwm.freq(FREQUENCY)
    pwm.duty_u16(DUTY_CYCLE)


except KeyboardInterrupt:
    # Cleanup: stop PWM signals on each pin
    pwm1.deinit()
    pwm2.deinit()
    pwm3.deinit()

