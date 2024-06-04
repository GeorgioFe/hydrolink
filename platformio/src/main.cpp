#include <BluetoothSerial.h>
#include <Adafruit_NeoPixel.h>

// NeoPixel settings
#define PIXEL_PIN 26
#define NUMPIXELS 16

Adafruit_NeoPixel pixels(NUMPIXELS, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

// HC-SR04 settings
#define TRIG_PIN 14
#define ECHO_PIN 35

// Bluetooth settings
BluetoothSerial SerialBT;

// Function prototypes
long readUltrasonicDistance(int triggerPin, int echoPin);
void setPixelsBasedOnDistance(long distance);

void setup() {
  Serial.begin(115200);
  if (!SerialBT.begin("ESP32Ultrasonic")) {
      Serial.println("Bluetooth initialization failed!");
      while (true);
  }
  Serial.println("Bluetooth device is ready to pair");
  
  // Initialize NeoPixel
  pixels.begin();
  pixels.show(); // Initialize all pixels to 'off'
  
  // Initialize HC-SR04 pins
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  long distance = readUltrasonicDistance(TRIG_PIN, ECHO_PIN);
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  // Send the distance over Bluetooth
  if (SerialBT.hasClient()) {
      SerialBT.print(distance);
      SerialBT.print("\n");
      Serial.println("Data sent via Bluetooth");
  } else {
      Serial.println("No Bluetooth clients connected");
  }

  setPixelsBasedOnDistance(distance);
  
  delay(100); // Delay between readings
}

// Read distance from HC-SR04
long readUltrasonicDistance(int triggerPin, int echoPin) {
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  
  long duration = pulseIn(echoPin, HIGH);
  long distance = (duration / 2) / 29.1; // Convert to cm
  
  return distance;
}

// Set NeoPixel color based on distance
void setPixelsBasedOnDistance(long distance) {
  uint32_t color;
  const long max_distance = 30.48; // Maximum measurable distance in cm

  if (distance < 2.54) {
    color = pixels.Color(255, 0, 0); // Red for 0-1 inches
  } else if (distance < 5.08) {
    color = pixels.Color(255, 127, 0); // Orange for 1-2 inches
  } else if (distance < 7.62) {
    color = pixels.Color(255, 255, 0); // Yellow for 2-3 inches
  } else if (distance < 10.16) {
    color = pixels.Color(0, 255, 0); // Green for 3-4 inches
  } else if (distance < 12.70) {
    color = pixels.Color(0, 255, 127); // SpringGreen for 4-5 inches
  } else if (distance < 15.24) {
    color = pixels.Color(0, 255, 255); // Cyan for 5-6 inches
  } else if (distance < 17.78) {
    color = pixels.Color(0, 127, 255); // DeepSkyBlue for 6-7 inches
  } else if (distance < 20.32) {
    color = pixels.Color(0, 0, 255); // Blue for 7-8 inches
  } else if (distance < 22.86) {
    color = pixels.Color(75, 0, 130); // Indigo for 8-9 inches
  } else if (distance < 25.40) {
    color = pixels.Color(139, 0, 255); // Violet for 9-10 inches
  } else if (distance < 27.94) {
    color = pixels.Color(255, 0, 255); // Magenta for 10-11 inches
  } else if (distance < 30.48) {
    color = pixels.Color(255, 20, 147); // DeepPink for 11-12 inches
  } else {
    color = pixels.Color(0, 0, 0); // Off for anything beyond 12 inches
  }
  
  for (int i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, color);
  }
  pixels.show();
}
