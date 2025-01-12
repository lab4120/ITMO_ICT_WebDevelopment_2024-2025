import socket

def udp_client():
    # Создаем UDP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Адрес сервера
    server_address = ('localhost', 12345)

    # Отправляем сообщение серверу
    message = "Hello, server"
    client_socket.sendto(message.encode(), server_address)
    print(f"Сообщение отправлено серверу: {message}")

    # Получаем ответ от сервера
    response, _ = client_socket.recvfrom(1024)
    print(f"Ответ от сервера: {response.decode()}")

    # Закрываем сокет
    client_socket.close()

if __name__ == "__main__":
    udp_client()