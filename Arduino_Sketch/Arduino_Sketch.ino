const int ledPin = 13;
int blinkDelay = 1000;  // Default blink delay

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);  // Set the baud rate to match the Python script
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();
    
    if (receivedChar == '1') {
      blinkDelay = 1000;  // Set blink delay to 1 second
      blinkLED();
    } else if (receivedChar == '2') {
      blinkDelay = 500;  // Set blink delay to 0.5 seconds (twice per second)
      blinkLED();
    }
  }
}

void blinkLED() {
  digitalWrite(ledPin, HIGH);
  delay(blinkDelay);
  digitalWrite(ledPin, LOW);
  delay(blinkDelay);
}
