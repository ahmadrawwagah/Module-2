# Module-2
This is the code and technical documentation for my ESPotify project as a part of CES

# Materials
- TTGO T1
- USB C cable
- A cardboard box or other enclosure
- Potentiometer
- Button

# Code
There are two codebases for this project (the Arduino code and the Python code). The Arduino code is very simple and just relays the data taken from the potentiometer and button over serial to the Python program.
The Python program is also fairly simple. You must register with the [spotify API](https://developer.spotify.com/documentation/web-api) to get the required client ID and secret to access the API. You must also set the redirect URL on the Spotify web API dashboard to be localhost. After running the Python program, you will be prompted to log in to Spotify. The Python program will read the data from the serial connection with the ESP32 and then call the Spotify API accordingly. 
The code was loaded onto the TTGO T1 using the Arduino IDE

# Installation
First, wire up the button as follows, NO and - should both connect to the sensor pin, in this case 27. C should be connected to GND and + should be connected to 5V. The potentiometer should be connected as follows. Left leg (with the legs facing you) should be connected to GND. The middle leg should be connected to the sensor pin, in this case 12. Finally, the right leg should be connected to 3V. After wiring and connecting everything, place the esp 32 in the enclosure and the potentiometer and button should be mounted to the wall as seen in the picture below. Wire the usb c cable out of a hole in the enclosure so it can be connected to the laptop.

![IMG_4165](https://github.com/ahmadrawwagah/Module-2/assets/96959925/7b04ed14-6f32-459e-a1f8-88a13b633e29)


