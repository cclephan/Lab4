# Lab 4 RC Step Response
## Christian Clephan, Kyle McGrath

This lab involved creating an RC circuit to test an interrupt callback function which put recorded ADC values into a queue.
A timer was used with a frequency of 1000Hz to toggle the interrupt callback function so our queue should be recording about
1000 values for a 1 second step response. Once the queue has been filled, each value is printed and read. Below are our ADC values for a 1 second step response:

<img src="https://github.com/cclephan/Lab4/blob/main/Images/RC.png" width="600" height="400" />

Figure 1: Step Response RC Circuit Outputting ADC Values

Figure 1 shows the response as collected by our user interface file. Using Excel we found the time constant by finding the time at which the ADC value = 0.63*ADC<sub>max</sub>
By doing this we found the time constant to be 304ms, Figure 2 shows our annotated graph.

<img src="https://github.com/cclephan/Lab4/blob/main/Images/Annotated.png" width="600" height="400" />

Figure 2: Annotated RC Step Response

Our experimental time constant of 304ms was extremely close to the measured resistor and capacitor used in our circuit. Our resistor and capacitor were found to be
103 kΩ and 33.5 μF, which comes to a time constant of 345ms. This makes the percent error = 13.5%. This fits within the tolerances of our capacitor and resistor, which
can be between 5% to 25%.
