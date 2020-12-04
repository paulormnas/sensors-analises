import Adafruit_DHT

class DHT22():
    def __init__(self, pino):
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = pino

    def ler_dados(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
        if humidity is None and temperature is None:
            print('Erro ao ler dados do sensor DHT22!')

        return humidity, temperature