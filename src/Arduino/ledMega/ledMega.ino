const int ledPin = 13; // Assuming we're using the built-in LED

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) { // Check if data is available to read
    char receivedChar = Serial.read(); // Read the incoming byte
    if (receivedChar == '1') {
      digitalWrite(ledPin, HIGH); // Turn LED on
    } else if (receivedChar == '0') {
      digitalWrite(ledPin, LOW); // Turn LED off
    }
  }
}

