String serialData;
int serialDataToInt;

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
    
    serialData = Serial.readString();
    serialDataToInt = serialData.toInt();

    myservo.write(serialDataToInt);
    delay(3);
  }
}
