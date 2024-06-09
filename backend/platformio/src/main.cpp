#include <WiFi.h>
#include <Adafruit_NeoPixel.h>
#include <WebSocketsClient.h>
#include <ArduinoJson.h>

// Replace with your network credentials
const char* ssid = "AbelsTheorem";
const char* password = "M1alyan123";

// Server settings
const char* websocket_server = "192.168.1.236"; // Replace with your server's IP

// NeoPixel settings
#define PIXEL_PIN 26
#define NUMPIXELS 16

// HC-SR04 settings
#define TRIGGER_PIN 14
#define ECHO_PIN 35

Adafruit_NeoPixel pixels(NUMPIXELS, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

// Variables for interval timing
unsigned long previousMillis = 0;
unsigned long interval = 0; // Default interval (0 means no lighting)
bool ledState = false;
unsigned long onTime = 5000; // 5 seconds
bool demoMode = false; // Demo mode toggle state

// Create a WebSocket client
WebSocketsClient webSocket;

// Function Declarations
void webSocketEvent(WStype_t type, uint8_t * payload, size_t length);
void setPixels(bool state);
long readUltrasonicDistance(int triggerPin, int echoPin);
void setPixelsBasedOnDistance(long distance);

void setup() {
  Serial.begin(115200);
  
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());

  // Initialize NeoPixel
  pixels.begin();
  pixels.show(); // Initialize all pixels to 'off'

  // Setup WebSocket
  webSocket.begin(websocket_server, 500, "/ws");
  webSocket.onEvent(webSocketEvent);
  webSocket.setReconnectInterval(5000);

  // Ensure LED is off initially
  setPixels(false);

  // Initialize ultrasonic sensor pins
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  webSocket.loop();

  if (demoMode) {
    // Demo mode: Update LED color based on distance
    long distance = readUltrasonicDistance(TRIGGER_PIN, ECHO_PIN);
    setPixelsBasedOnDistance(distance);
    delay(100); // Small delay to avoid overloading the CPU
  } else {
    // Original behavior
    unsigned long currentMillis = millis();

    if (interval > 0) {
      if (ledState == false && (currentMillis - previousMillis >= interval)) {
        // Light up the LED
        ledState = true;
        setPixels(ledState);
        Serial.println("LEDs ON");
        previousMillis = currentMillis; // Reset the timer for onTime
      }

      if (ledState == true && (currentMillis - previousMillis >= onTime)) {
        // Turn off the LED after onTime has passed
        ledState = false;
        setPixels(ledState);
        Serial.println("LEDs OFF");
        previousMillis = currentMillis; // Reset the timer for interval
      }
    }

    delay(100); // Small delay to avoid overloading the CPU
  }
}

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {
  switch(type) {
    case WStype_DISCONNECTED:
      Serial.println("WebSocket Disconnected!");
      break;
    case WStype_CONNECTED:
      Serial.println("WebSocket Connected!");
      break;
    case WStype_TEXT: {
      Serial.printf("WebSocket message: %s\n", payload);
      String response = String((char*)payload);
      Serial.printf("Parsed response: %s\n", response.c_str());
      if (response == "null") {
        interval = 0; // Set interval to 0 to turn off LED
        setPixels(false); // Ensure LED is off
      } else if (response == "demo_on") {
        demoMode = true;
        Serial.println("Demo mode ON");
      } else if (response == "demo_off") {
        demoMode = false;
        Serial.println("Demo mode OFF");
        setPixels(false); // Ensure LED is off initially
      } else {
        interval = response.toInt() * 1000; // Convert seconds to milliseconds
        Serial.print("New interval set: ");
        Serial.println(interval);
        // Reset the timers and LED state
        previousMillis = millis(); // Reset the timer
        ledState = false;
        setPixels(false); // Ensure LED is off initially
      }
      break;
    }
    default:
      break;
  }
}

// Set NeoPixel state
void setPixels(bool state) {
  uint32_t color = state ? pixels.Color(255, 255, 255) : pixels.Color(0, 0, 0); // White if on, off otherwise

  for (int i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, color);
  }
  pixels.show();
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