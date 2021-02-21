char serialData;

#include <Servo.h>

Servo myservo;

void setup() {
  // put your setup code here, to run once:
 myservo.attach(9);
 Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    serialData = Serial.read();

    switch (serialData) {
      case '0':
        myservo.write(0);
        break;
      case '1':
        myservo.write(10);
        break;
      case '2':
        myservo.write(20);
        break;
      case '3':
        myservo.write(30);
        break;
      case '4':
        myservo.write(40);
        break;
      case '5':
        myservo.write(50);
        break;
      case '6':
        myservo.write(60);
        break;
      case '7':
        myservo.write(70);
        break;
      case '8':
        myservo.write(80);
        break;
      case '9':
        myservo.write(90);
        break;
      case 'a':
        myservo.write(100);
        break;
      case 'b':
        myservo.write(110);
        break;
      case 'c':
        myservo.write(120);
        break;
     case 'd':
        myservo.write(130);
        break;
     case 'e':
        myservo.write(140);
        break;
     case 'f':
        myservo.write(150);
        break;
     case 'g':
        myservo.write(160);
        break;
     case 'h':
        myservo.write(170);
        break;
     case 'i':
        myservo.write(180);
        break;
    }
  }
}
