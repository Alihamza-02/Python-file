const int buttonPin = 2;   // Pin where the button is connected
const int relayPin = 8;    // Pin where the relay is connected

int buttonState = 0;       // Variable to store the current button state
int lastButtonState = 0;   // Variable to store the previous button state

void setup() {
  pinMode(buttonPin, INPUT);  // Set the button pin as input
  pinMode(relayPin, OUTPUT);  // Set the relay pin as output
  digitalWrite(relayPin, LOW); // Ensure the fan is off initially
}

void loop() {
  buttonState = digitalRead(buttonPin); // Read the current state of the button

  // Check if the button is pressed
  if (buttonState == HIGH && lastButtonState == LOW) {
    // If the button was just pressed, toggle the fan
    digitalWrite(relayPin, HIGH);  // Turn on the fan
  }
  // Check if the button is released
  else if (buttonState == LOW && lastButtonState == HIGH) {
    // If the button was just released, turn off the fan
    digitalWrite(relayPin, LOW);  // Turn off the fan
  }

  // Save the current button state for the next loop
  lastButtonState = buttonState;
}
