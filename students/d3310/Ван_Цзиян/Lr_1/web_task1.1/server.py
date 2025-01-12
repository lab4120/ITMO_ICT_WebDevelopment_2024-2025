import socket

def udp_server():
    # Создаем UDP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Привязываем сокет к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    print("Сервер запущен и ожидает сообщение...")

    while True:
        # Ждем сообщения от клиента
        message, client_address = server_socket.recvfrom(1024)
        print(f"Получено сообщение от клиента: {message.decode()}")

        # Отправляем ответ клиенту
        response = "Hello, client"
        server_socket.sendto(response.encode(), client_address)
        print("Ответ отправлен клиенту.")

if __name__ == "__main__":
    udp_server()