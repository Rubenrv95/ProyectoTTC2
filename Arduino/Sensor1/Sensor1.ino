#define sensor1 3
#define sensor2 7

void setup(){
 Serial.begin (9600);
  pinMode (sensor1 , INPUT);
  pinMode (sensor2 , INPUT);
}

void loop(){
  int rain = digitalRead(sensor1);
  int rain2 = digitalRead(sensor2);

  if(rain==1) {
    Serial.println("Esta lloviendo en Curico");
    delay(500);
  }
  else if(rain==0) {
    Serial.println("No llueve en Curico");
    delay(500);
  }

  if(rain2==1) {
    Serial.println("Esta lloviendo en Talca");
    delay(500);
  }
  else if(rain2==0) {
    Serial.println("No llueve en Talca");
    delay(500);
  }

}
