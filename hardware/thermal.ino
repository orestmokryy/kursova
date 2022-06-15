#define sensorPin A8
float calibration = 0.1039;
void setup() {
  Serial.begin(9600);
  analogReference(INTERNAL1V1);
}

void loop() {
  int reading = analogRead(sensorPin);
  Serial.print(reading*calibration, 1);
  delay(100);
}
