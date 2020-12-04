
int maxSense = 0;
int minSense = 1025;
float offset = 0;
bool calibrate;

int ledValue = LOW;

int ledPin = 13;
int lightSensorPin = A0;

bool drawerClosed = true;
int lightSense = 0;



void setup() {
  
  Serial.begin(9600); 
  pinMode(lightSensorPin, INPUT);
  pinMode(ledPin, OUTPUT);  
  while(millis() <= 5000){
    maxSense = max(maxSense, analogRead(lightSensorPin));
    minSense = min(minSense, analogRead(lightSensorPin));
    offset = .1 * (maxSense - minSense);
  }
  maxSense = maxSense - offset;
  minSense = minSense + offset;
  Serial.flush();
  Serial.println("FINISHED SETUP");
}

void loop() {
  // put your main code here, to run repeatedly:
  // Occurs only once you have callibrated
  lightSense = analogRead(lightSensorPin);
  if(lightSense >= maxSense && drawerClosed){
    drawerClosed = false;
  }
  if(lightSense <= minSense && !drawerClosed){
    drawerClosed = true;
    Serial.println(1);
    Serial.flush();
  } 
  

}
