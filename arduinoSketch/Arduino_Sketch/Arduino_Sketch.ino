#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;  // variable to store the servo position

const int buzzer1Pin = 4;
const int buzzer2Pin = 3;
const int buzzer3Pin = 2;


void setup() {
  pinMode(buzzer1Pin, OUTPUT);
  pinMode(buzzer2Pin, OUTPUT);
  pinMode(buzzer3Pin, OUTPUT);
  myservo.attach(9);

  // set servo to mid position
  myservo.write(pos);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();

    if (receivedChar == '1') {
      alarm();
      Serial.println("0");
    } else if (receivedChar == '2') {
      chirpy();
      Serial.println("0");
    } else if (receivedChar == '3') {
      
      curious();
      Serial.println("0");
    }
  }
}

void curious() {
  // random small swipes

  // number of times repeating gesture
  int repeat = 8;
  for (int i = 0; i < repeat; i++) {
    
    // FRONT SWIPE CHANGE VARIABLES HERE FOR EACH SWIPE!
    int degrees = random(30, 180); // number of degrees of the swipe front 
    int interval_f = 1; // interval step time of the swipe, the higher the faster it goes
    int interval_b = 1; // interval back
    float delay_back = random(500, 1200); // delay before back swipe starts
    float delay_front = random(1500, 5000); // delay before front swipe starts again


    for (pos = 0; pos <= degrees; pos += interval_f) {  // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos);  // tell servo to go to position in variable 'pos'
      delay(0.01);         // waits 15ms for the servo to reach the position
    }
    delay(delay_back);

    // BACK SWIPE
    for (pos = degrees; pos >= 0; pos -= interval_b) {  // goes from 180 degrees to 0 degrees
      myservo.write(pos);                  // tell servo to go to position in variable 'pos'
      delay(0.01);                         // waits 15ms for the servo to reach the position
    }
    delay(delay_front);
  }
}



void chirpy() {
  // small bursts swipes with a pause in between

  // number of times repeating gesture
  int repeat = 10;
  for (int i = 0; i < repeat; i++) {
    
    // FRONT SWIPE CHANGE VARIABLES HERE FOR EACH SWIPE!
    int degrees = random(70, 90); // number of degrees of the swipe front 
    int interval_f = 1; // interval step time of the swipe, the higher the faster it goes
    int interval_b = 1; // interval back
    float delay_back = 200; // delay before back swipe starts
    float delay_front = random(1000, 3000); // delay before front swipe starts again


    for (pos = 0; pos <= degrees; pos += interval_f) {  // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos);  // tell servo to go to position in variable 'pos'
      delay(0.01);         // waits 15ms for the servo to reach the position
    }
    delay(delay_back);

    // BACK SWIPE
    for (pos = degrees; pos >= 0; pos -= interval_b) {  // goes from 180 degrees to 0 degrees
      myservo.write(pos);                  // tell servo to go to position in variable 'pos'
      delay(0.01);                         // waits 15ms for the servo to reach the position
    }
    delay(delay_front);
  }
}

void alarm() {

  // number of times repeating gesture
  int repeat = 5;
  for (int i = 0; i < repeat; i++) {
    
    // FRONT SWIPE CHANGE VARIABLES HERE FOR EACH SWIPE!
    int degrees = random(140, 156); // number of degrees of the swipe front 
    int interval_f = 1; // interval step time of the swipe, the higher the faster it goes
    int interval_b = 1; // interval back
    float delay_back = 500; // delay before back swipe starts
    float delay_front = 500; // delay before front swipe starts again


    for (pos = 0; pos <= degrees; pos += interval_f) {  // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos);  // tell servo to go to position in variable 'pos'
      delay(0.01);         // waits 15ms for the servo to reach the position
    }
    delay(delay_back);

    // BACK SWIPE
    for (pos = degrees; pos >= 0; pos -= interval_b) {  // goes from 180 degrees to 0 degrees
      myservo.write(pos);                  // tell servo to go to position in variable 'pos'
      delay(0.01);                         // waits 15ms for the servo to reach the position
    }
    delay(delay_front);
  }


  


}



