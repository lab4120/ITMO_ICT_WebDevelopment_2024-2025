import socket
import threading

# Хранит подключенных клиентов
clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            # Прием сообщения
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} покинул чат.".encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Подключено к {str(address)}")

        client.send("Пожалуйста, введите ваш ник: ".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Пользователь с ником {nickname} подключился.")
        broadcast(f"{nickname} вошел в чат.".encode('utf-8'))
        client.send("Добро пожаловать в чат!".encode('utf-8'))

        # Создать новый поток для каждого клиента
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязка IP-адреса сервера и порта
server.bind(('127.0.0.1', 55555))
server.listen()

print("Сервер запущен, ожидает подключения клиентов...")
receive()