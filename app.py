from flask import Flask, jsonify
import RPi.GPIO as GPIO

# Import CORS (since live server and flask run on different ip addresses and port numbers)
from flask_cors import CORS  

# Set up GPIO for the LED 
LED_PIN = 18  # GPIO 18

# Use BCM GPIO numbering
GPIO.setmode(GPIO.BCM)  

 # Set pin as output
GPIO.setup(LED_PIN, GPIO.OUT) 

 # Start with the LED off
GPIO.output(LED_PIN, GPIO.LOW) 

# Enable CORS for the Flask app(if code not included it wont be able to fun the server)
app = Flask(__name__)
CORS(app)  

# Track the LED status
led_status = "off"

#registers a new URL endpoint (/toggle) that the Flask application will respond to.
@app.route('/toggle', methods=['GET'])
def toggle_led():

    # Access the global variable led_status to track the LED state
    global led_status
    if led_status == "off":
        
         # Turn the LED on
        GPIO.output(LED_PIN, GPIO.HIGH) 
        led_status = "on"
    else:
         # Turn the LED off
        GPIO.output(LED_PIN, GPIO.LOW) 
        led_status = "off"

    # returns the status in json format 
    return jsonify({"status": led_status})

# Start the Flask application on all available IP addresses (0.0.0.0) and port 5000
if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
