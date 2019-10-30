#define pinMotor0 11
#define pinMotor1 10
#define pinMotor2 6
#define pinMotor3 5
int pot = 255 * 0.45;
void setup() {
  
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
  /*digitalWrite(pinMotor0, LOW);
  digitalWrite(pinMotor1, HIGH);
  digitalWrite(pinMotor2, LOW);
  digitalWrite(pinMotor3, HIGH);*/
  analogWrite(pinMotor0, pot);
  analogWrite(pinMotor1, 0);
  analogWrite(pinMotor2, pot);
  analogWrite(pinMotor3, 0);
  delay(2000);
  analogWrite(pinMotor0, 0);
  analogWrite(pinMotor1, pot);
  analogWrite(pinMotor2, 0);
  analogWrite(pinMotor3, pot);
  /*digitalWrite(pinMotor0, HIGH);
  digitalWrite(pinMotor1, LOW);
  digitalWrite(pinMotor2, HIGH);
  digitalWrite(pinMotor3, LOW);*/
  delay(2000);
}
