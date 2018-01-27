#include "rgb_lcd.h"

rgb_lcd lcd;

void setup() {
Serial.begin(9600);
Serial.println("Ready");
lcd.begin(16, 1);
}
void loop() {
char inByte = ' ';
lcd.autoscroll();
if(Serial.available()){
char inByte = Serial.read();
lcd.print(inByte);
delay(200);
}
}
