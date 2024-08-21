import random
import time
import requests # type: ignore

def read_temperature():
    # Simula a leitura de um sensor de temperatura
    return random.uniform(-10, 40)  # Gera uma temperatura entre -10 e 40 graus Celsius

def send_temperature_to_cloud(temperature):
    # Envia a temperatura para o servidor web (interface)
    try:
        requests.post('http://localhost:5000/update-temperature', json={'temperature': temperature})
    except Exception as e:
        print(f"Erro ao enviar dados para o servidor: {e}")

def main():
    while True:
        temperature = read_temperature()
        print(f"Temperatura atual: {temperature:.2f}°C")
        send_temperature_to_cloud(temperature)
        time.sleep(5)  # Aguarda 5 segundos antes de ler a temperatura novamente

if __name__ == '__main__':
    main()
