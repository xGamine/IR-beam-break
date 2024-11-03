from machine import Pin, PWM, ADC
import time

# Define PWM parameters
FREQUENCY = 38000    # 38kHz frequency
DUTY_CYCLE = 32768   # 50% duty cycle (32768 / 65535)

# Initialize PWM on three different pins (GPIO15, GPIO16, and GPIO17)
pwm1 = PWM(Pin(15))
pwm2 = PWM(Pin(16))
pwm3 = PWM(Pin(17))

# Set the PWM frequency and duty cycle for each pin
for pwm in [pwm1, pwm2, pwm3]:
    pwm.freq(FREQUENCY)
    pwm.duty_u16(DUTY_CYCLE)

# Initialize ADC on GPIO26, GPIO27, and GPIO28 (ADC channels 0, 1, and 2)
adc0 = ADC(Pin(26))  # ADC channel 0
adc1 = ADC(Pin(27))  # ADC channel 1
adc2 = ADC(Pin(28))  # ADC channel 2

# Function to read the voltage from an ADC pin
def read_voltage(adc):
    # Read raw ADC value (0-65535 for 3.3V range)
    raw_value = adc.read_u16()
    # Convert to voltage: Pico's ADC has a 3.3V reference voltage
    voltage = (raw_value / 65535) * 3.3
    return voltage  # Return the calculated voltage

try:
    # Main loop to read and print voltages continuously
    while True:
        # Read and print voltage from each ADC pin
        voltage0 = read_voltage(adc0)
        voltage1 = read_voltage(adc1)
        voltage2 = read_voltage(adc2)
        
        print(f"Voltage on GPIO26: {voltage0:.2f} V")
        print(f"Voltage on GPIO27: {voltage1:.2f} V")
        print(f"Voltage on GPIO28: {voltage2:.2f} V")
        print("-" * 30)
        
        time.sleep(1)  # Wait 1 second before the next reading

except KeyboardInterrupt:
    # Cleanup: stop PWM signals on each pin
    pwm1.deinit()
    pwm2.deinit()
    pwm3.deinit()
    print("PWM signals stopped.")

