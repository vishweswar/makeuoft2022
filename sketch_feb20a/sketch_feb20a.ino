#define TOO_CLOSE 50
#define echoPin 2 
#define trigPin 3 
#define gasSensor A3
#define piezo 5

long duration; 
int distance; 

void setup() {
  pinMode(piezo, OUTPUT);
  pinMode(gasSensor, INPUT);
  pinMode(trigPin, OUTPUT);
 
  pinMode(echoPin, INPUT); 
  Serial.begin(9600); 
}
void loop() {
 
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
 
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  duration = pulseIn(echoPin, HIGH);
 
  distance = duration * 0.034 / 2;
  
 
   
  if(distance < TOO_CLOSE)
  {
   Serial.write("1");
   tone(piezo,750);
   delay(1000);
  }
  else
  {
    noTone(piezo);
    Serial.write("2");
  }

  if(analogRead(gasSensor > 320)) //from experiments 
  {
   Serial.write("3");
   //tone(piezo,1000);
  }
  else
  {    
    Serial.write("0");
    noTone(piezo);
  }
  
  delay(1000);
}
