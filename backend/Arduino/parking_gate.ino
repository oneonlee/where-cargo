#include<Servo.h>

Servo servo;
Servo servo1;
int servoPin =3;
int servoPin1 =11;
int trig = 5;
int echo = 6;
int trig1 = 9;
int echo1 = 10;

int angle = 0;
int angle1 = 0;

void setup(){
  servo.attach(3);
  servo1.attach(11);
  Serial.begin(9600);
  pinMode(5, OUTPUT);
  pinMode(6, INPUT);
  pinMode(9, OUTPUT);
  pinMode(10, INPUT);
  Serial.begin(9600);
  
  }

void loop(){
  long duration;
  long distance;

  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  delay(500);
  digitalWrite(5, HIGH);
  delay(1000);
  digitalWrite(5, LOW);

  duration = pulseIn(echo, HIGH);
  distance = ((float)(340*duration)/10000)/2;

  Serial.print("거리: ");
  Serial.print(distance);
  Serial.println("cm");
  servo.write(0);

 
  if (distance<10){
   
   angle = 80;
    servo.write(angle);
    delay(500);
    }
  else{
    angle = 170;
     servo.write(angle);
    delay(500);
    }

 long duration1;
 long distance1;

  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  delay(500);
  digitalWrite(9, HIGH);
  delay(1000);
  digitalWrite(9, LOW);

  duration1 = pulseIn(echo1, HIGH);
  distance1 = ((float)(340*duration1)/10000)/2;

  Serial.print("거리1: ");
  Serial.print(distance1);
  Serial.println("cm");

  if (distance1<10){
    angle1 =180;
    servo1.write(angle1);
    delay(500);
    }
  else{
    angle1 = 90;
     servo1.write(angle1);
    delay(500);
    }
  
  }
