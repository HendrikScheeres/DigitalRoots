const int ledPin = 13;
int blinkDelay = 1000;  // Default blink delay

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(6, OUTPUT);
  Serial.begin(9600);  // Set the baud rate to match the Python script
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();
    
    if (receivedChar == '1') {
      // perform this gesture after the gesture is done send back that its done

      Serial.println("Done");
    } else if (receivedChar == '2') {
      // perform this gesture after the gesture is done send back that its done

      digitalWrite(2, HIGH);
      delay(1000);
      digitalWrite(2, LOW);
      delay(1000);
      digitalWrite(2, HIGH);
      delay(1000);
      digitalWrite(2, LOW);
      delay(1000);
      digitalWrite(2, HIGH);
      delay(1000);
      digitalWrite(2, LOW);
      delay(1000);

      Serial.println("Done");
    } else if (receivedChar == '3') {
      // perform this gesture after the gesture is done send back that its done

      digitalWrite(3, HIGH);
      delay(1000);
      digitalWrite(3, LOW);
      delay(1000);
      digitalWrite(3, HIGH);
      delay(1000);
      digitalWrite(3, LOW);
      delay(1000);
      digitalWrite(3, HIGH);
      delay(1000);
      digitalWrite(3, LOW);
      delay(1000);

      Serial.println("Done");
    }else if (receivedChar == '4') {
      // perform this gesture after the gesture is done send back that its done

      analogWrite(4, 50);
      delay(1000);
      digitalWrite(4, LOW);
      delay(1000);
      analogWrite(4, 100);
      delay(1000);
      digitalWrite(4, LOW);
      delay(1000);
      analogWrite(4, 150);
      delay(1000);
      digitalWrite(4, LOW);
      delay(1000);
      analogWrite(4, 200);
      delay(1000);
      digitalWrite(4, LOW);
      delay(1000);
      analogWrite(4, 255);
      delay(1000);
      

      Serial.println("Done");
    }
  }
}



