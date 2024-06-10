# ECE 140B - The Art of Product  Engineering II
## Team 12 - Hydrolink

![img](/admin/assets/hydrolink-banner.png)

## Table of Contents
  - [About Us](#about-us)
    - [Team Members](#team-members)
  - [High Level Overview of Hydrolink](#high-level-overview-of-hydrolink)
    - [System Design and Architecture](#system-design-and-architecture)
    - [Hardware](#hardware)
    - [Software](#software)
  - [Getting Started](#getting-started)
  - [Repository Structure](#repository-structure)

## About Us
>At Hydrolink, we are a team of passionate engineering students dedicated to enhancing health and wellness through technology. Our mission is to simplify and democratize personal hydration monitoring. We provide a smart, cost-effective universal lid that fits any water bottle, allowing users to effortlessly track their hydration levels. With Hydrolink, monitoring your personal hydration is simple, accessible, and adaptable to any mainstream brand of water bottle.

- You can read more about us and our product [here](/admin/Hydrolink%20-%20MVP%20Report.pdf).
- You can access our MVP pitch deck here.
- You can access our Iri Kumis [here](/admin/Iri%20Kumis/).

### Team Members
<div>
  <div style="margin-bottom: 20px;">
    <img src="./admin/assets/georgio.png" width="60" height="60" alt="Georgio" style="vertical-align: middle; margin-right: 10px;">
    <span style="vertical-align: middle;">Georgio Feghali</span>
  </div>
  <div style="margin-bottom: 20px;">
    <img src="./admin/assets/daniel.png" width="60" height="60" alt="Daniel" style="vertical-align: middle; margin-right: 10px;">
    <span style="vertical-align: middle;">Daniel Sanei</span>
  </div>
  <div style="margin-bottom: 20px;">
    <img src="./admin/assets/ned.png" width="60" height="60" alt="Ned" style="vertical-align: middle; margin-right: 10px;">
    <span style="vertical-align: middle;">Ned Bitar</span>
  </div>
</div>

## High Level Overview of Hydrolink
>Hydrolink is a universal smart water bottle lid designed to enhance hydration
tracking and management. It features an LED ring light that turns on as a reminder to drink
water, and the light can be customized to match your style. The lid includes an ESP32
microcontroller, which handles processing and connectivity for real-time data updates. An
ultrasonic sensor measures the water level in the bottle, ensuring accurate hydration
tracking. Hydrolink works with a range of popular water bottle brands like Hydro Flask and
YETI, making it easy to upgrade your existing bottles without buying new ones. The
accompanying Hydrolink web app enhances the experience with features like daily
hydration tracking, LED customization, and personalized hydration recommendations. The
app uses user data to offer advice tailored to help you meet your hydration goals. Overall,
Hydrolink is a practical, stylish, and tech-savvy solution for staying hydrated.

### System Design and Architecture
>The Hydrolink system combines both hardware and software components to create an effective hydration tracking solution. For hardware, it uses the HC-SR04 Ultrasonic Sonar Distance Sensor to measure the distance between the lid and the water surface, allowing it to calculate the amount of water consumed. The 16Bits WS2812 5050 RGB LED ring provides reminders to drink water through visual cues. An ESP32 DEVKIT V1 microprocessor powers the sensors and handles data transmission (via Websockets) to the server. On the software side, the backend utilizes FastAPI and Uvicorn to run the server, with Supabase managing the database and user authentication. The frontend is built using HTML, CSS, and Vanilla JS, focusing on a mobile-first design for a seamless user experience across all devices. This integrated system ensures reliable and user-friendly hydration management.

![img](/admin/assets/architecture.png)

### Hardware
![img](/admin/assets/cad.png)
![img](/admin/assets/prototype.png)

### Software
![img](/admin/assets/ui.png)

## Getting Started
Coming Soon!

## Repository Structure
```bash
.
├── README.md
├── admin
│   ├── Hydrolink - MVP Report.pdf
│   ├── Interviews
│   │   ├── ECE 140B - Gali Interview.pdf
│   │   ├── ECE 140B - Harry Interview.pdf
│   │   └── ECE 140B - Sarkis Interview.pdf
│   ├── Iri Kumis
│   │   ├── README.md
│   │   └── Slides
│   │       ├── ECE 140B Iri Kumi #2 - The Kano Model.pdf
│   │       ├── ECE 140B Iri Kumi #3 - Sprint 1 Review.pdf
│   │       ├── ECE 140B Iri Kumi #5 - Artificial Intelligence.pdf
│   │       ├── ECE 140B Iri Kumi #6 - Sprint 2 Review.pdf
│   │       └── ECE 140B Iri Kumi #8 - Final Update.pdf
│   └── assets
│       ├── architecture.png
│       ├── daniel.png
│       ├── georgio.png
│       ├── hydrolink-banner.png
│       └── ned.png
├── backend
│   ├── __pycache__
│   │   ├── auth.cpython-310.pyc
│   │   ├── auth.cpython-312.pyc
│   │   ├── db_access.cpython-310.pyc
│   │   ├── main.cpython-310.pyc
│   │   ├── server.cpython-312.pyc
│   │   ├── supabase_setup.cpython-310.pyc
│   │   └── supabase_setup.cpython-312.pyc
│   ├── auth.py
│   ├── db_access.py
│   ├── main.py
│   ├── platformio
│   │   ├── include
│   │   │   └── README
│   │   ├── lib
│   │   │   └── README
│   │   ├── platformio.ini
│   │   ├── src
│   │   │   └── main.cpp
│   │   └── test
│   │       └── README
│   ├── server.py
│   ├── supabase_setup.py
│   └── tempCodeRunnerFile.py
└── frontend
    ├── pages
    │   ├── about.html
    │   ├── dashboard.html
    │   ├── help-support.html
    │   ├── register.html
    │   ├── signin.html
    │   └── welcome.html
    └── static
        ├── assets
        │   ├── bottle.png
        │   ├── daniel-avatar.png
        │   ├── favicon.png
        │   ├── georgio-avatar.png
        │   ├── ned-avatar.png
        │   └── placeholder.png
        ├── css
        │   ├── about-styles.css
        │   ├── dashboard-styles.css
        │   ├── header-menu-styles-white.css
        │   ├── header-menu-styles.css
        │   ├── help-support-styles.css
        │   ├── register-styles.css
        │   ├── signin-styles.css
        │   ├── styles.css
        │   └── welcome-styles.css
        └── js
            ├── about-script.js
            ├── dashboard-script.js
            ├── help-support-script.js
            ├── script.js
            └── welcome-script.js

19 directories, 60 files
```