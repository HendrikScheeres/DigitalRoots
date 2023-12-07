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
      mellowActivation();
      Serial.println("Done");
    } else if (receivedChar == '2') {
      chirpyActivation();
      Serial.println("Done");
    } else if (receivedChar == '3') {
      alarmActivation();
      Serial.println("Done");
    }
  }
}

void mellowActivation() {
  for (int i = 0; i < 3; i++) {
    tone(buzzer1Pin, 150, 500);
    delay(600);
  }
  noTone(buzzer1Pin);
  delay(500);

  for (int i = 0; i < 2; i++) {
    tone(buzzer2Pin, 200, 600);
    delay(700);
  }
  noTone(buzzer2Pin);
  delay(500);

  tone(buzzer3Pin, 250, 800);
  delay(1000);
  noTone(buzzer3Pin);
}

void chirpyActivation() {
  for (int i = 0; i < 5; i++) {
    tone(buzzer1Pin, 1000, 100);
    delay(150);
  }
  noTone(buzzer1Pin);
  delay(500);

  for (int i = 0; i < 8; i++) {
    tone(buzzer2Pin, 1200, 50);
    delay(70);
  }
  noTone(buzzer2Pin);
  delay(500);

  for (int i = 0; i < 10; i++) {
    tone(buzzer3Pin, 1500, 30);
    delay(40);
  }
  noTone(buzzer3Pin);
}

void alarmActivation() {
  for (int i = 0; i < 10; i++) {
    tone(buzzer1Pin, 2000, 200);
    delay(250);
  }
  noTone(buzzer1Pin);
  delay(500);

  for (int i = 0; i < 15; i++) {
    tone(buzzer2Pin, 1800, 100);
    delay(120);
  }
  noTone(buzzer2Pin);
  delay(500);

  for (int i = 0; i < 20; i++) {
    tone(buzzer3Pin, 2200, 50);
    delay(60);
  }
  noTone(buzzer3Pin);
}
