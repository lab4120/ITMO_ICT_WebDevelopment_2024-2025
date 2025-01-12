import socket
import threading

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'Пожалуйста, введите ваш ник: ':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Произошла ошибка! Невозможно подключиться к серверу.")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('utf-8'))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
client.connect(('127.0.0.1', 55555))

nickname = input("Выберите ник: ")

# Запуск потоков для приема и отправки сообщений
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()