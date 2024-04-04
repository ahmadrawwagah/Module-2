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
First, wire up the button as follows, 


![image](https://github.com/ahmadrawwagah/Ahmad_Scroll/assets/96959925/cee83359-cb2a-46fb-ac80-88dbd85ce5b9)
