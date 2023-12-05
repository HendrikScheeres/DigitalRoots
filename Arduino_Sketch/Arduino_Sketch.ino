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
      digitalWrite(ledPin, HIGH);
    } else if (receivedChar == '2') {
      digitalWrite(ledPin, LOW);
    }
  }
}


