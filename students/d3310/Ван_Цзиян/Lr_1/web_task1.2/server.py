import socket
import math

def tcp_server():
    # Создаем TCP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сокет к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Начинаем прослушивание входящих соединений
    server_socket.listen(1)
    print("Сервер запущен и ожидает подключения...")

    while True:
        # Принимаем подключение от клиента
        connection, client_address = server_socket.accept()
        try:
            print(f"Подключено к клиенту: {client_address}")

            # Получаем данные от клиента
            data = connection.recv(1024).decode()
            a, b = map(float, data.split(","))
            print(f"Получены параметры: a = {a}, b = {b}")

            # Вычисляем гипотенузу
            c = math.sqrt(a**2 + b**2)

            # Отправляем результат обратно клиенту
            connection.sendall(str(c).encode())
        finally:
            connection.close()

if __name__ == "__main__":
    tcp_server()
