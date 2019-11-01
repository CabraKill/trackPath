#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

#define pinMotor0 16
#define pinMotor1 5
#define pinMotor2 4
#define pinMotor3 0
 
IPAddress staticIP(192, 168, 0, 69);
IPAddress gateway(192, 168, 0, 1);   //IP Address of your WiFi Router (Gateway)
IPAddress subnet(255, 255, 255, 0);  //Subnet mask
IPAddress dns(8, 8, 8, 8);  //DNS
const char* deviceName = "esp'Ael";
ESP8266WebServer server(80); //Server on port 80
void setup() {

  
  pinMode(pinMotor0, OUTPUT);
  pinMode(pinMotor1, OUTPUT);
  pinMode(pinMotor2, OUTPUT);
  pinMode(pinMotor3, OUTPUT);
  digitalWrite(pinMotor0, LOW);
  digitalWrite(pinMotor1, LOW);
  digitalWrite(pinMotor2, LOW);
  digitalWrite(pinMotor3, LOW);
  //Serial.begin(115200);
  delay(1);
  
  WiFi.begin("Ric Net", "jrspcmcs03"); //Connect to the WiFi network
  WiFi.disconnect();
  WiFi.config(staticIP, subnet, gateway, dns);
  WiFi.hostname(deviceName);
  WiFi.begin("Ric Net", "jrspcmcs03");
  while (WiFi.status() != WL_CONNECTED) { //Wait for connection
    delay(500);
    //Serial.println("Waiting to connect…");
  }
  //Serial.print("IP address: ");
  //Serial.println(WiFi.localIP()); //Print the local IP
  
  server.on("/run", run);
  server.on("/hi", hi);
  server.begin(); //Start the server
  Serial.begin(9600);
  Serial.println("Server listening");
  Serial.println(WiFi.localIP());

}
void run(){
  String w0 = server.arg("w0");
  String w1 = server.arg("w1");
  String w2 = server.arg("w2");
  String w3 = server.arg("w3");
  /*digitalWrite(pinMotor0,w0.toInt());
  digitalWrite(pinMotor1,w1.toInt());
  digitalWrite(pinMotor2,w2.toInt());
  digitalWrite(pinMotor3,w3.toInt());*/
  digitalWrite(pinMotor0,w0.toInt());
  digitalWrite(pinMotor1,w1.toInt());
  digitalWrite(pinMotor2,w2.toInt());
  digitalWrite(pinMotor3,w3.toInt());
  
  //Serial.print(w0.toInt());
  //Serial.print(w1.toInt());
  //Serial.print(w2.toInt());
  //Serial.println(w3.toInt());
  String t = "Estados das entradas: ";

  t+= w0.toInt();
  t+= w1.toInt();
  t+= w2.toInt();
  t+= w3.toInt();

  server.send(200, "text", t);
}

void hi(){
  String a = "<h1>Ola, estou com voce e nao largo ^^</h1>";
  String t = "<h1>Car updated ^^</h1><h2 style=\"color:blue\">";
  int w0 = digitalRead(pinMotor0);
  int w1 = digitalRead(pinMotor1);
  int w2 = digitalRead(pinMotor2);
  int w3 = digitalRead(pinMotor3);
  t += w0; 
  t += w1;
  t += w2;
  t += w3;
  t += "</h2>";
  server.send(200, "text/html", a+t);
}

void loop() {
  server.handleClient();
}

//String t = "<h1>Car updated ^^</h1> ";//+"<h2>" + w0.toInt() + w1.toInt() + w2.toInt() + w3.toInt() + "</h2>";
  //t+= "</h2>";
  //server.send(200, "text/html", t);
  //t+= "<h2>";
  
