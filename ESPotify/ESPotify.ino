void setup() {
  Serial.begin(115200);
  pinMode(27, INPUT_PULLUP);
  delay(1000);
  
}

void loop(){
  int analogValue = analogRead(12);
  int volume = map(analogValue, 0, 4095, 1, 99);
  int butt = digitalRead(27);
  Serial.println(volume);
  if (butt == 0){
    Serial.println(0);
  }
  delay(250);
}