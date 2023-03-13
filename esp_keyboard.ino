#include <BleKeyboard.h>

int LED_BUILTIN = 2;

BleKeyboard bleKeyboard("ArduinoBT", "KK", 100);

void blinkLights(int d) {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(d);
  digitalWrite(LED_BUILTIN, LOW);
  delay(d);
}

void setup() {
  Serial.begin(115200); // set BAUD

  pinMode(LED_BUILTIN, OUTPUT); // enable LED

  Serial.println("Starting up..");
  bleKeyboard.setDelay(50);
  bleKeyboard.begin();
}

void loop() {
  if(bleKeyboard.isConnected()) {
    while(Serial.available() == 0) {
      Serial.println("Waiting for commands..");
      digitalWrite(LED_BUILTIN, HIGH);
      delay(250);
    }

    digitalWrite(LED_BUILTIN, LOW);
    
    int in = Serial.read();
    switch (in) {
      case 'g':
        if (random(1,4) == 1) {
          Serial.println("Sending 'Hello world'...");
          bleKeyboard.print("Hello world");
        }

        if (random(1,4) == 1) {
          for (int i=1; i <= random(1,8); i++) {
            Serial.println("Sending KEY_UP_ARROW...");
            bleKeyboard.write(KEY_UP_ARROW);
          }
        }

        if (random(1,4) == 1) {
          for (int i=1; i <= random(1,8); i++) {
            Serial.println("Sending KEY_DOWN_ARROW...");
            bleKeyboard.write(KEY_DOWN_ARROW);
          }
        }

        if (random(1,4) == 1) {
          for (int i=1; i <= random(1,8); i++) {
            Serial.println("Sending KEY_LEFT_ARROW...");
            bleKeyboard.write(KEY_LEFT_ARROW);
          }
        }

        if (random(1,4) == 1) {
          for (int i=1; i <= random(1,8); i++) {
            Serial.println("Sending KEY_RIGHT_ARROW...");
            bleKeyboard.write(KEY_RIGHT_ARROW);
          }
        }

        for (int i=1; i <= random(1,15); i++) {
          Serial.println("Sending KEY_TAB...");
          bleKeyboard.write(KEY_TAB);
        }

        //Serial.println("Sending KEY_RETURN...");
        //bleKeyboard.write(KEY_RETURN);
        Serial.println("Sending ' '...");
        bleKeyboard.write(' ');

        break;
      default:
        Serial.println(in);
        
        break;
    }
  } else {
    Serial.println("Disconnected..");

    for (int i=1; i <= 4; i++)
      blinkLights(250);
  }
}