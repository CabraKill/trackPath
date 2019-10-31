#define pinMotor0 11
#define pinMotor1 10
#define pinMotor2 6
#define pinMotor3 5

#define pinEsp0 A0
#define pinEsp1 A1
#define pinEsp2 A2
#define pinEsp3 A3

float pot = 0.35;
float precisao0 = 5/100;
void setup() {
  //Serial.begin(9600);
  //Make the voltage max reference equal to a pin external voltage
  analogReference(EXTERNAL);
  
  pinMode(pinMotor0, OUTPUT);
  pinMode(pinMotor1, OUTPUT);
  pinMode(pinMotor2, OUTPUT);
  pinMode(pinMotor3, OUTPUT);
  pinMode(pinEsp0, INPUT);
  pinMode(pinEsp1, INPUT);
  pinMode(pinEsp2, INPUT);
  pinMode(pinEsp3, INPUT);
  digitalWrite(pinMotor0, LOW);
  digitalWrite(pinMotor1, LOW);
  digitalWrite(pinMotor2, LOW);
  digitalWrite(pinMotor3, LOW);
  

}

void loop() {
  int p0 = analogRead(pinEsp0);
  //Serial.print("p0:");
  //Serial.print(p0);
  //Serial.print(":");
  //Serial.println(p0*pot / 4.02);
  if(p0 <= precisao0 * 1023)
    p0 = 0;
  int p1 = analogRead(pinEsp1);
  //Serial.print("p1:");
  //Serial.println(p1*pot);
  if(p1 <= precisao0 * 1023)
    p1 = 0;
  int p2 = analogRead(pinEsp2);
  //Serial.print("p2:");
  //Serial.println(p2*pot);
  if(p2 <= precisao0 * 1023)
    p2 = 0;
  int p3 = analogRead(pinEsp3);
  //Serial.print("p3:");
  //Serial.println(p3*pot);
  if(p3 <= precisao0 * 1023)
    p3 = 0;
  
  analogWrite(pinMotor0, p0 * pot / 4.02);
  analogWrite(pinMotor1, p1 * pot / 4.02);
  analogWrite(pinMotor2, p2 * pot / 4.02);
  analogWrite(pinMotor3, p3 * pot / 4.02);
  delay(300);
  delay(100);
}
