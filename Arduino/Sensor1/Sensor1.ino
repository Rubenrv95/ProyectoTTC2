#define sensor1 3
#define sensor2 7

int sensor1Anterior = -1;
int sensor2Anterior = -1;

void setup(){
 Serial.begin (9600);
  pinMode (sensor1 , INPUT);
  pinMode (sensor2 , INPUT);
}

void loop(){
  int rain = digitalRead(sensor1);
  int rain2 = digitalRead(sensor2);

  if(rain != sensor1Anterior){
    Serial.print("Curico ");
    Serial.println(rain);
    sensor1Anterior = rain;
  }
  delay(500);
  if(rain2 != sensor2Anterior){
    Serial.print("Talca ");
    Serial.println(rain2);
    sensor2Anterior = rain2;
  }
  delay(500);

}
