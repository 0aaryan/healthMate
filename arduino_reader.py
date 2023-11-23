# arduino_reader.py
import serial
import time
import random

class ArduinoReader:
    def __init__(self, port, baud_rate):
        self.serial_port = serial.Serial(port, baud_rate, timeout=1)

class ArduinoReader:
    def __init__(self, port, baud_rate):
        self.serial_port = serial.Serial(port, baud_rate, timeout=1)

    def read_data_avg(self, duration_sec):
        start_time = time.time()
        heart_rates = []
        temperatures = []

        while (time.time() - start_time) < duration_sec:
            line = self.serial_port.readline().decode().strip()
            if line:
                # Assume the data is in the format "heart_rate,temp"
                heart_rate, temperature = map(float, line.split(','))

                # Collect the data for averaging
                heart_rates.append(heart_rate)
                temperatures.append(temperature)

        # Calculate the average values
        avg_heart_rate = sum(heart_rates) / len(heart_rates) if heart_rates else 0
        avg_temperature = sum(temperatures) / len(temperatures) if temperatures else 0

        #avg tempaertaure should be random value between 97.7 and 100.1 for testing
        # avg_temperature = random.uniform(97.7, 100.1)
        #limit heartrate to 0 decimal point and temp to 2
        avg_heart_rate = round(avg_heart_rate, 0)
        avg_temperature = round(avg_temperature, 2)

        return avg_heart_rate, avg_temperature

