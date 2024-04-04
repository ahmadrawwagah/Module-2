# this code will read the touch values from the ESP32 and echo them on the command line
# you could do something else more interesting with these values (e.g. visualize/sonify)
import sys
import spotipy
import spotipy.util as util
import serial

ser = serial.Serial('/dev/ttyS8', 115200)
scope = 'user-modify-playback-state'
username = "ahmadrawwagah"
token = util.prompt_for_user_token(username,scope,client_id='d5a7d3ad4ce9477e90cb48e781b9dd29',client_secret='adceb38738a84fb2bacdb2a7a17e5353',redirect_uri='http://localhost/:8080')
if token:
    print("Got Token")
else:
    print("Can't get token for", username)
    sys.exit(1)

sp = spotipy.Spotify(auth=token)
while(True):
  volume = int(ser.readline().strip(), 'ascii')
  sp.volume(volume, device_id=None)
