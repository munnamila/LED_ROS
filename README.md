# LED_ROS

this program is used to that turn on, turn off and blink LED.
For this you need a Raspberry Pi3, LEDs, resistences, jumpwires, a breadboard.

## Electric circuit
Use jumpwires and tesistences to conect Raspberry Pi3 and LED. 

Pins used this time is GPIO 2, GPIO 24 and Ground.

## Usage
```bash
roscore
rosrun mypkg count.py
rosrun mypkg twice.py
```
Input 1, red LED will light for 2s, and than be off.
```bash
please input:1
output is:1
```
Input 2, yellow LED will light for 2s, and than be off.
```bash
please input:2
output is:2
```
Input 3, red led and yellow LED will light alternately light 5 times.
```bash
please input:3
output is:3
```
## License
BSD

## Reference
About twice.py, referenced from Kenta Nakano and got his license.

## Demo video
https://www.youtube.com/watch?v=tzzqxj41YzA
