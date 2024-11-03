# IR-beam-break
This circuit will pulse an IR (940nm) LED at a frequency of 38kHz and then use an IR reciever (such as the TSOP38238) to detect when it can see the LED and when the LED is no longer in view this is then passed through an op-amp acting as a comparator to produce a binary output. The output signal will be binary (logic 1 or logic 0), allowing for easy integration with microcontrollers.

Components Used:
 - 1x IR (940nm) LED
 - 1x LM359 Op-Amp
 - 1x TSOP38238 Infrarared Reciever {can be sourced at https://thepihut.com/products/ir-infrared-receiver-tsop38238}
 - 1x Diode
 - 1x 10 ohm resistor
 - 1x PWM capable microcontroller
 - Breadboard + wire or equivalent (or just solder it)

Circuit Diagram:

<img width="886" alt="image" src="https://github.com/user-attachments/assets/2949fab4-ac55-4210-bb0d-f8e80a1377c7">





