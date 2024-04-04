# this code will read the touch values from the ESP32 and echo them on the command line
# you could do something else more interesting with these values (e.g. visualize/sonify)
import sys
import spotipy
import spotipy.util as util
import serial

ser = serial.Serial('/dev/ttyS8', 115200)
scope = 'user-modify-playback-state'
username = "ahmadrawwagah"
token = util.prompt_for_user_token(username,scope,client_id='<INSERT_CLIENT_ID>',client_secret='<INSERT_CLIENT_SECRET>',redirect_uri='http://localhost/:8080')
if token:
    print("Got Token")
else:
    print("Can't get token for", username)
    sys.exit(1)

sp = spotipy.Spotify(auth=token)
while(True):
  volume = int(ser.readline().strip(), 'ascii')
  sp.volume(volume, device_id=None)
