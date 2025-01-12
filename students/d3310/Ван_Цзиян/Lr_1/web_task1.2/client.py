import socket

def tcp_client():
    # Создаем TCP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Указываем адрес сервера
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    try:
        # Запрашиваем ввод параметров у пользователя
        a = input("Введите значение a: ")
        b = input("Введите значение b: ")

        # Отправляем параметры на сервер
        message = f"{a},{b}"
        client_socket.sendall(message.encode())

        # Получаем результат от сервера
        result = client_socket.recv(1024).decode()
        print(f"Гипотенуза c = {result}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    tcp_client()