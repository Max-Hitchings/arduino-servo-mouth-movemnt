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
    Serial.print(serialData);

    if (serialData == '1') {
      myservo.write(180);}
    else if (serialData == '0') {
      myservo.write(20);}
  }
}
