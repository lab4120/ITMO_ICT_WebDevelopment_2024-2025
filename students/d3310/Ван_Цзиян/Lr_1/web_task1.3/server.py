import socket

def http_server():
    # Создаем TCP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сокет к адресу и порту
    server_address = ('localhost', 8080)
    server_socket.bind(server_address)

    # Начинаем прослушивание входящих соединений
    server_socket.listen(1)
    print("Сервер запущен и ожидает подключения на порту 8080...")

    while True:
        # Принимаем подключение от клиента
        connection, client_address = server_socket.accept()
        try:
            print(f"Подключено к клиенту: {client_address}")

            # Получаем запрос от клиента
            request = connection.recv(1024).decode()
            print(f"Получен запрос:\n{request}")

            # Загружаем содержимое HTML-файла
            with open('index.html', 'r', encoding='utf-8') as file:
                html_content = file.read()

            # Формирование HTTP-ответа
            http_response = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n{html_content}"

            # Отправляем ответ клиенту
            connection.sendall(http_response.encode())
        except FileNotFoundError:
            # Обработка ошибки, если файл не найден
            http_response = "HTTP/1.1 404 Not Found\n\n<h1>404 Not Found</h1>"
            connection.sendall(http_response.encode())
        finally:
            connection.close()

if __name__ == "__main__":
    http_server()
#http://127.0.0.1:8080