#define pinMotor0 11
#define pinMotor1 10
#define pinMotor2 6
#define pinMotor3 5

#define pinEsp0 A0
#define pinEsp1 A1
#define pinEsp2 A2
#define pinEsp3 A3

float pot = 0.45;
float precisao0 = 5/100;
void setup() {
  
  //Make the voltage max reference equal to a pin external voltage
  analogReference(EXTERNAL);
  
  pinMode(pinMotor0, OUTPUT);
  pinMode(pinMotor1, OUTPUT);
  pinMode(pinMotor2, OUTPUT);
  pinMode(pinMotor3, OUTPUT);
  digitalWrite(pinMotor0, LOW);
  digitalWrite(pinMotor1, LOW);
  digitalWrite(pinMotor2, LOW);
  digitalWrite(pinMotor3, LOW);

}

void loop() {
  int p0 = analogRead(pinEsp0);
  if(p0 <= precisao0 * 255)
    p0 = 0;
  int p1 = analogRead(pinEsp0);
  if(p1 <= precisao0 * 255)
    p1 = 0;
  int p2 = analogRead(pinEsp0);
  if(p2 <= precisao0 * 255)
    p2 = 0;
  int p3 = analogRead(pinEsp0);
  if(p3 <= precisao0 * 255)
    p3 = 0;
  analogWrite(pinMotor0, p0 * pot);
  analogWrite(pinMotor1, p1 * pot);
  analogWrite(pinMotor2, p2 * pot);
  analogWrite(pinMotor3, p3 * pot);
  delay(100);
}
