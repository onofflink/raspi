bool sensorState = 0;
bool preSensorState = 0;
int loopCouter = 0;
int detectCounter = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(PD2, INPUT);
  delay(10);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if (switchCheck() == 1)
  {
    detectCounter++;
  }
  if (loopCouter > 100)
  {
    Serial.print("Detected count = ");
    Serial.println(detectCounter);
    detectCounter = 0;
    loopCouter = 0;
  }
  loopCouter++;
  delay(10);
}

bool switchCheck()
{
  sensorState = digitalRead(PD2);
  if ((sensorState == 1) && (preSensorState == 0))
  {
    delay(10);
    sensorState = digitalRead(PD2);
    if (sensorState == 1)
    {
      preSensorState = sensorState;
      return 1;
    }
  }
  else if ((sensorState == 0) && (preSensorState == 1))
  {
    delay(10);
    sensorState = digitalRead(PD2);
    if (sensorState == 0)
    {
      preSensorState = sensorState;
    }
  }
  return 1;
}
