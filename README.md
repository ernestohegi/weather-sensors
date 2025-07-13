# Weather Sensors Web Dashboard

A MicroPython web application for Raspberry Pi Pico that reads environmental sensor data and provides a very simple web dashboard interface.

## Features

- Reads temperature, humidity and pressure from BME280 sensor (I2C)
- Reads temperature and humidity from DHT11 sensor (GPIO)
- Web dashboard to view sensor readings
- Control of onboard LED
- Lightweight web interface using Microdot framework

## Hardware Requirements

- Raspberry Pi Pico WiFi
- BME280 environmental sensor (I2C connection)
- DHT11 temperature/humidity sensor (GPIO connection)
- Breadboard and jumper wires

## Software Dependencies

- MicroPython firmware
- Required libraries:
  - `microdot` (web framework)
  - `utemplate` (HTML templates)
  - `picozero` (LED control)
  - Custom BME280 library (included in project)

## Installation

1. Flash MicroPython to your Raspberry Pi Pico
2. Upload all project files to the Pico:
   - main.py
   - bme280.py
   - config.py (see Configuration section)
3. Install required packages (if not already included in your MicroPython build):
   - microdot
   - picozero

## Configuration

1. Copy `config.example` to `config.py`
2. Edit `config.py` with your settings:
   ```python
   SSID = 'YOUR_WIFI_NETWORK'
   PASSWORD = 'YOUR_WIFI_PASSWORD'
   PORT = 80  # Web server port
   ```

## Usage

1. Run the application using Thonny:
   - Open main.py in Thonny
   - Click "Run" or press F5
2. Access the web dashboard at:
   ```
   http://[PICO_IP_ADDRESS]:[PORT]
   ```
3. Dashboard features:
   - View BME280 sensor readings (temperature, pressure, humidity)
   - View DHT11 sensor readings (temperature, humidity)
   - Control onboard LED (on/off)

## API Endpoints

- `/` - Main dashboard
- `/bme280` - BME280 sensor readings
- `/dht11` - DHT11 sensor readings
- `/light-on` - Turn onboard LED on
- `/light-off` - Turn onboard LED off

## Credits

- BME280 library adapted from [Rui Santos' ESP-MicroPython implementation](https://github.com/RuiSantosdotme/ESP-MicroPython/blob/master/code/WiFi/HTTP_Client_IFTTT_BME280/BME280.py)
- Microdot web framework
