int uno;
#include <Servo.h>
#include <LiquidCrystal.h>

#define servoPin1 0
#define servoPin2 1
#define servoPin3 7
#define switchPin2 3
#define switchPin1 2

Servo myservo1;
Servo myservo2;
Servo myservo3;

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(6, OUTPUT);
  digitalWrite(6, LOW);

  pinMode(9, INPUT);
  pinMode(10, INPUT);
  lcd.begin(16, 2);
  
  myservo1.attach(servoPin1);
  myservo2.attach(servoPin2);
  myservo3.attach(servoPin3);

  myservo1.write(0);
  myservo2.write(0);
  myservo3.write(0);
}

void next() {
  myservo3.write(60);
  delay(350);
  Serial.println("Servo 1 Engaged");
  myservo1.write(180);
  delay(500);
  myservo3.write(20);
  delay(250);
  myservo1.write(0);
  Serial.println("Servo 1 Unengaged");
}

void servoReset() {
  myservo3.write(0);
  myservo2.write(150);
  Serial.println("Servo 2 Engaged");
  delay(5000);
  myservo2.write(60);
  Serial.println("Servo 3 Unengaged");
}

void loop() {

  if (Serial.available()) {
    int x = Serial.readString().toInt();
    lcd.setCursor(0, 1);
    // print the number of seconds since reset:
    lcd.print(x);
    if (x == 1) {
      next();
    }
    else if (x == 2)
    {
      servoReset();
    }
  }

  int buttonState1;
  int buttonState2;
  buttonState1 = digitalRead(9);
  buttonState2 = digitalRead(10);
  if (buttonState1 == HIGH) {
    Serial.println("played");
  }
  if (buttonState2 == HIGH) {
    Serial.println("skipped");
  }
  else {
    Serial.println("no");
  }
  //while (!Serial.available());
  //uno = Serial.readString().toInt();
  uno = 0;
  if (uno == 1) {
    lcd.setCursor(0, 1);
    // print the number of seconds since reset:
    lcd.print("UNO!");
  }
}
