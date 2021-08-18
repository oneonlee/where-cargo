#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define SERVER_IP "165.246.241.112:8000"

#ifndef STASSID
#define STASSID "Galaxy S20 Ultra 5G1662"
#define STAPSK  "SM-G988Ncc6"
#endif

#include <Arduino.h>
#include <U8g2lib.h>

#ifdef U8X8_HAVE_HW_SPI
#include <SPI.h>
#endif
#ifdef U8X8_HAVE_HW_I2C
#include <Wire.h>
#endif

U8G2_SSD1306_128X64_NONAME_1_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);

int distance0 = 0; 
int distance1 = 0;
int distance2 = 0;
int volt0 = 0;
int volt1 = 0;
int volt2 = 0;
int analogPin0 = 0;
int analogPin1 = 1;
int analogPin2 = 2;

int result[3];
 
void setup(){
// Serial.begin(115200);
Serial.begin(9600);

  Serial.println();
  Serial.println();
  Serial.println();

  WiFi.begin(STASSID, STAPSK);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());
}

void loop(){
  volt0 = map(analogRead(analogPin0), 0, 1023, 0, 5000); 
  distance0 = (27.61 / (volt0 - 0.1696)) * 1000; 
//  Serial.print("0: ");
//  Serial.print(distance0);  //거리값을 시리얼모니터로 출력해줍니다.
//  Serial.println(" cm");
//  Serial.println(" ");
  delay(500);

  volt1 = map(analogRead(analogPin1), 0, 1023, 0, 5000); 
  distance1 = (27.61 / (volt1 - 0.1696)) * 1000; 
//  Serial.print("1: ");
//  Serial.print(distance1);  //거리값을 시리얼모니터로 출력해줍니다.
//  Serial.println(" cm");
//  Serial.println(" ");
  delay(500);

  volt2 = map(analogRead(analogPin2), 0, 1023, 0, 5000); 
  distance2 = (27.61 / (volt2 - 0.1696)) * 1000; 
//  Serial.print("2: ");
//  Serial.print(distance2);  //거리값을 시리얼모니터로 출력해줍니다.
//  Serial.println(" cm");
//  Serial.println(" ");
  delay(500);
  
  
  if (distance0 < 10){
    result[0] = 1;
    }
  else {
    result[0] = 0;
    }

   if (distance1 < 10){
    result[1] = 1;
    }
  else {
    result[1] = 0;
    }
   if (distance2 < 10){
    result[2] = 1;
    }
  else {
    result[2] = 0;
    }
//  for (int i=0; i<3; i++){
//    Serial.println(result[i]);
//    delay(500);
//  }






  // wait for WiFi connection
  if ((WiFi.status() == WL_CONNECTED)) {

    WiFiClient client;
    HTTPClient http;

    Serial.print("[HTTP] begin...\n");
    // configure traged server and url
    http.begin(client, "http://" SERVER_IP "/result/"); //HTTP
    http.addHeader("Content-Type", "application/json");

    Serial.print("[HTTP] POST...\n");
    // start connection and send HTTP header and body

    char buffer[26];
    sprintf(buffer , "{\"4\":%d, \"5\":%d, \"6\":%d}", result[0], result[1], result[2]);
    int httpCode = http.POST(buffer);

    // httpCode will be negative on error
    if (httpCode > 0) {
      // HTTP header has been send and Server response header has been handled
      Serial.printf("[HTTP] POST... code: %d\n", httpCode);

      // file found at server
      if (httpCode == HTTP_CODE_OK) {
        const String& payload = http.getString();
        Serial.println("received payload:\n<<");
        Serial.println(payload);
        Serial.println(">>");
      }
    } else {
      Serial.printf("[HTTP] POST... failed, error: %s\n", http.errorToString(httpCode).c_str());
    }

    http.end();
  }

  delay(10000);
} 