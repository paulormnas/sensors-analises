from devices import Sensors
from datetime import datetime
import time
import json

dht22 = Sensors.DHT22(pino=22)
read_time = 1  # intervalo entre leituras em minutos.


def data_register(data):
    date_str = datetime.fromtimestamp(data["data"]).strftime("%d/%m/%y %H:%M")
    print(date_str + "\t",
          'Temperatura: ' + str(data["temperatura"]) + "ºC\t",
          'Umidade: ' + str(data["umidade"]) + "%\t")

    dados_json = json.dumps(data)
    file_path = "registros/" + str(data["data"]) + ".json"

    with open(file_path, "a+") as f:
        f.write(dados_json)


def main():
    inicial_time = 0
    while True:
        if time.time() - inicial_time > read_time:
            humidity, temperature = dht22.ler_dados()
            date = time.time()
            dados = {
                'umidade': humidity,
                'temperatura': temperature,
                'data': date
            }
            data_register(dados)

            inicial_time = time.time()



if __name__ == '__main__':
    main()
