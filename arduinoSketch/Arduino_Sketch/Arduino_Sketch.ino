const int buzzer1Pin = 2;
const int buzzer2Pin = 3;
const int buzzer3Pin = 4;

void setup() {
  pinMode(buzzer1Pin, OUTPUT);
  pinMode(buzzer2Pin, OUTPUT);
  pinMode(buzzer3Pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();
    
    if (receivedChar == '1') {
      alarmActivation();
      Serial.println("0");
    } else if (receivedChar == '2') {
      chirpyActivation();
      Serial.println("0");
    } else if (receivedChar == '3') {
      mellowActivation();
      Serial.println("0");
    }
  }
}

void mellowActivation() {
  for (int i = 0; i < 3; i++) {
    analogWrite(buzzer1Pin, 150); // Vary duty cycle for mellow sound
    analogWrite(buzzer2Pin, 100);
    analogWrite(buzzer3Pin, 200);
    delay(300);
    analogWrite(buzzer1Pin, 0); // Turn off the buzzers
    analogWrite(buzzer2Pin, 0);
    analogWrite(buzzer3Pin, 0);
    delay(300);
  }
  delay(500);

  // More elaborate mellowActivation pattern here...
}

void chirpyActivation() {
  for (int i = 0; i < 5; i++) {
    analogWrite(buzzer1Pin, 200); // Vary duty cycle for chirpy sound
    analogWrite(buzzer2Pin, 180);
    analogWrite(buzzer3Pin, 220);
    delay(100);
    analogWrite(buzzer1Pin, 0); // Turn off the buzzers
    analogWrite(buzzer2Pin, 0);
    analogWrite(buzzer3Pin, 0);
    delay(100);
  }
  delay(500);

  // More elaborate chirpyActivation pattern here...
}

void alarmActivation() {
  for (int i = 0; i < 10; i++) {
    analogWrite(buzzer1Pin, 255); // Vary duty cycle for alarm sound
    analogWrite(buzzer2Pin, 255);
    analogWrite(buzzer3Pin, 255);
    delay(70);
    analogWrite(buzzer1Pin, 0); // Turn off the buzzers
    analogWrite(buzzer2Pin, 0);
    analogWrite(buzzer3Pin, 0);
    delay(70);
  }
  delay(500);

  // More elaborate alarmActivation pattern here...
}
