# IR-beam-break
This circuit will pulse an IR (940nm) LED at a frequency of 38kHz and then use an IR reciever (such as the TSOP38238) to detect when it can see the LED and when the LED is no longer in view this is then passed through an op-amp acting as a comparator to produce a binary output. The output signal will be binary (logic 1 or logic 0), allowing for easy integration with microcontrollers.

Components Used:
 - 1x IR (~940nm wavelength) 5mm LED
 - 1x LM359 Op-Amp
 - 1x TSOP38238 Infrarared Reciever {can be sourced at https://thepihut.com/products/ir-infrared-receiver-tsop38238}
 - 1x Diode
 - 1x 10 ohm resistor
 - 1x PWM capable microcontroller or a timing circuit that outputs a frequency of 38kHz with a 50% duty cycle (I just used a Raspberry Pi Pico 2 because I didn't have the correct resistor combinations to make a 38kHz timing circuit)
 - Breadboard + wire or equivalent (or just solder it)

Circuit Diagram:

<img width="886" alt="image" src="https://github.com/user-attachments/assets/2949fab4-ac55-4210-bb0d-f8e80a1377c7">

Diagram Notes -- Vcc can be anywhere from 3-5V DC 
Diagram Notes -- The TSOP38238's pins are in the incorrect order when compared to the physical component, see the datasheet for more info: https://www.vishay.com/docs/82491/tsop382.pdf
Diagram Notes -- Pi Pico pin numbers are physical pin numbers and not GPIO pin numbers, Pi Pico Pinout: https://pico.pinout.xyz/
Diagram Notes -- Pi Pico can be substituted for another timing circuit so long as it outputs roughly 38kHz at 3-5v DC with a 50% duty cycle
Diagram Notes -- The opamp only digitises the output signal from the IR Reciever to make it easier to input into logic systems or microcontrollers and can be omitted if you would like an analogue output





