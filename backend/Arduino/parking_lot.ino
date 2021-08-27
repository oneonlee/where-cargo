#include "U8glib.h"
int distance0 = 0; 
int distance1 = 0;
int distance2 = 0;
int distance3 = 0;
int volt0 = 0;
int volt1 = 0;
int volt2 = 0;
int volt3 = 0;
int analogPin0 = 0;
int analogPin1 = 1;
int analogPin2 = 2;
int analogPin3 = 3;
int count = 0;

U8GLIB_SSD1306_128X64 u8g(U8G_I2C_OPT_DEV_0|U8G_I2C_OPT_NO_ACK|U8G_I2C_OPT_FAST);  // Fast I2C / TWI 

void setup() {
Serial.begin(9600);
}

void loop() {
  bool result[4]; 
  volt0 = map(analogRead(analogPin0), 0, 1023, 0, 5000); 
  distance0 = (27.61 / (volt0 - 0.1696)) * 1000; 
  Serial.print("distance0:");
  Serial.println(distance0);
  delay(100);

  volt1 = map(analogRead(analogPin1), 0, 1023, 0, 5000); 
  distance1 = (27.61 / (volt1 - 0.1696)) * 1000; 
   Serial.print("distance1:");
  Serial.println(distance1);
  delay(100);

  volt2 = map(analogRead(analogPin2), 0, 1023, 0, 5000); 
  distance2 = (27.61 / (volt2 - 0.1696)) * 1000; 
   Serial.print("distance2:");
  Serial.println(distance2);
  delay(100);

  volt3 = map(analogRead(analogPin3), 0, 1023, 0, 5000); 
  distance3 = (27.61 / (volt3 - 0.1696)) * 1000; 
   Serial.print("distance3:");
  Serial.println(distance3);
  delay(100);
  
  
  if (distance0 < 10){
    result[0] = true;
    }
  else {
    result[0] = false;
    }

   if (distance1 < 10){
    result[1] = true;
    }
  else {
    result[1] = false;
    }
   if ((distance2 < 16)&&(distance2 >0)){
    result[2] = true;
    }
  else {
    result[2] = false;
    }
  if ((distance3 < 14)&&(distance3 > 0)) {
    result[3] = true;
    }
  else {
    result[3] = false;
    }
    
 for (int i=0; i<4; i++){
  Serial.print(result[i]);
  Serial.println(" ");
  delay(500);
 }

 count = 0;
 for(int j=0; j<4; j++){
  if (result[j]==1){count = count +1;}
  }

  
  u8g.firstPage();
  do{
    // u8g.setFont(u8g_font_unifont);
    u8g.setFont(u8g_font_fur14);
    u8g.setPrintPos(0,30);
    u8g.print(count);
    u8g.print("/4");
    u8g.setPrintPos(0,50);
    
    u8g.print("Parked : ");
    for (int i =0; i<4; i++){
      if (result[i]==1) {
          
          u8g.print(i);
          u8g.print(" ");
        }
    }
    
    }while(u8g.nextPage());
}
