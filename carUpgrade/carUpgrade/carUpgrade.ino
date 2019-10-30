#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

#define pinMotor0 0
#define pinMotor1 1
#define pinMotor2 2
#define pinMotor3 3
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
  //Serial.begin(115200);
  delay(1);
  
  WiFi.begin("Ric Net", "jrspcmcs03"); //Connect to the WiFi network
  WiFi.disconnect();
   WiFi.config(staticIP, subnet, gateway, dns);
  WiFi.hostname(deviceName);
  WiFi.begin("Ric Net", "jrspcmcs03");
  while (WiFi.status() != WL_CONNECTED) { //Wait for connection
    delay(500);
    Serial.println("Waiting to connect…");
  }
  //Serial.print(“IP address: “);
  //Serial.println(WiFi.localIP()); //Print the local IP
  
  //server.on(“/on”, turnOn);         //Associate the handler function to the path
  //server.on(“/off”, turnOff);        //Associate the handler function to the path
  //server.on(“/toggle”, toggle);   //Associate the handler function to the path
  server.on("/run", run);
  server.begin(); //Start the server
  //Serial.println(“Server listening”);

}
void run(){
  String w0 = server.arg("w0");
  String w1 = server.arg("w1");
  String w2 = server.arg("w2");
  String w3 = server.arg("w3");
  digitalWrite(pinMotor0,w0.toInt());
  digitalWrite(pinMotor1,w1.toInt());
  digitalWrite(pinMotor2,w2.toInt());
  digitalWrite(pinMotor3,w3.toInt());
  String t = "Car updated ^^ " + w0 + w1 + w2 + w3;
  server.send(200, "text/plain", t);
}

void loop() {
  // put your main code here, to run repeatedly:
  server.handleClient();

}
