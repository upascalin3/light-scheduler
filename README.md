# light-scheduler
# 💡 WebSocket-to-MQTT Light Scheduler

Easily control a relay-connected light by scheduling ON/OFF times using a WebSocket interface and MQTT messaging. Ideal for home automation, IoT experimentation, or educational purposes.

---

## 🚀 Overview

This project lets you:
- 🖧 Send ON/OFF schedules via WebSocket
- 📡 Forward them through MQTT
- 🔌 Trigger a relay (via serial) connected to a microcontroller like Arduino

⏱️ Automate your lights — no manual switching, just schedule and go!

---

## 📚 How It Works

```mermaid
graph LR
    A[Client<br>Schedule JSON] --> B[WebSocket Server]
    B --> C[MQTT Broker]
    C --> D[MQTT Subscriber<br>+ Serial Writer]
    D --> E[Microcontroller<br>Relay ON/OFF]
