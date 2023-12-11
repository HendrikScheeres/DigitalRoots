# Digital Roots

In our increasingly interconnected yet physically distant world, traditional digital communication lacks the vital physical connection essential for meaningful interactions. Our project aims to bridge this gap by integrating houseplants into digital communication, creating an interactive system that facilitates tactile and emotional connections between individuals over the internet, using houseplants as a medium.

This is an elective project for the MSc Media Technolgy at Leiden University

## Description

This repository contains scripts and components for processing sensor data, connecting to Arduino sensors, and transmitting signals to a receiver.

### Files

- `main.py`: Executes the sensor, measures incoming signals, transforms them, and sends them to the receiver end.
- `capacitiveSensory.py`: Connects to the Arduino plant sensor, untangles incoming data for interpretation in `Main.py`.
- `dataCollection.py`: A variant of the script for data collection. This collected data can be utilized for network training.
- `training.py`: Handles network training processes.
- `transformer.py`: Loads trained weights and classifies incoming signals.
- `server.py`: Contains functions for connecting to and sending data to the receiving end.
- `connection/`: Folder containing the receiver script responsible for receiving incoming signals and sending them to the Arduino actuator (server).
    - `sender.py`: Test file for sending signals to the server.
    - `receiver.py`
- `arduinoSketch/`: Contains the Arduino sketch to be uploaded to the sensor.

## Getting Started

### Dependencies

Python 3.7.7
Arduino IDE 1.8.19

### Setting Up the Environment

To set up the project environment, install the required dependencies listed in the `requirements.txt` file. Use the following command:

```bash
pip install -r requirements.txt

### Executing program
python main.py
```
## Authors

Contributors Hendrik Scheeres & Zhu Ou 

## Acknowledgments

Inspiration, code snippets, etc.
* [Advanced Touch Sensing](https://github.com/Illutron/AdvancedTouchSensing)
