from microdot import Microdot, Response
from microdot.utemplate import Template
from config import SSID, PASSWORD, PORT
from machine import Pin, I2C
from picozero import pico_led

import mm_wlan
import bme280
import dht

# Initialize sensors
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=10000)
bme = bme280.BME280(i2c=i2c)
sensor = dht.DHT11(Pin(16))

mm_wlan.connect_to_network(SSID, PASSWORD)

app = Microdot()
Response.default_content_type = 'text/html'

pico_led.on()

@app.route('/', methods=['GET'])
def index(request):
    return Template('base.html').render(content=f"""
      <h1 class="text-2xl font-bold mb-4">Sensor Dashboard</h1>
      <p class="mb-4">Welcome to the sensor dashboard. Select a sensor to view its readings:</p>
      <ul class="flex space-x-4">
        <li class="mb-2">
          <a href="/bme280" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            BME280 Sensor
          </a>
        </li>
        <li>
          <a href="/dht11" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
            DHT11 Sensor
          </a>
        </li>
      </ul>
      <ul class="flex space-x-4">
        <li>
          <button onclick="fetch('/light-off').then(() => console.log('Light turned off'))" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
            Light Off
          </button>
        </li>
        <li>
          <button onclick="fetch('/light-on').then(() => console.log('Light turned on'))" class="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded">
            Light On
          </button>
        </li>
      </ul>
    """)

@app.route('/bme280')
def serve_bme280(request):
    """Serve BME280 sensor readings"""

    return Template('base.html').render(content=f"""
        <h2 class="font-bold">BME280 Sensor Readings</h2>
        <p>Temperature: {bme.temperature}</p>
        <p>Humidity: {bme.humidity}</p>
        <p>Pressure: {bme.pressure}</p>
        <p><a href="/">Back to home</a></p>
    """)

@app.route('/dht11')
def serve_dht11(request):
    """Serve DHT11 sensor readings"""
    sensor.measure()
    
    return Template('base.html').render(content=f"""
        <h2 class="font-bold">DHT11 Sensor Readings</h2>
        <p>Temperature: {sensor.temperature()}</p>
        <p>Humidity: {sensor.humidity()}</p>
        <p><a href="/">Back to home</a></p>
    """)

@app.route('/light-off')
def light_off(request):
    pico_led.off()

@app.route('/light-on')
def light_on(request):
    pico_led.on()

app.run(port=PORT)


