'''
НЕ СТИРАТЬ!!!!!!!!!!!!!!!!!!!!!!!!

эта рабочая зона моя. Сервер делаю я, сюда не лезть и ничего не трогать.
Если есть предложения, будем вместе это обсуждать и если что будешь работать с серваком

Наши общие данные будут такие:
HOST = 'localhost'
PORT = 12345 '''


import socket
import threading
import os


clients = []

# функция для принятия сообщений от клиентов и дальнейшая их переотправка
def send_message(clients_sock, sock_addres):
    while True:
        message = clients_sock.recv(1024).decode('utf-8')

        # проверяем, есть ли совпадение адрессов в клиентах. Если нет, то мы добавляем нового клиента в список
        if sock_addres not in [i[1] for i in clients]:
            clients.append((clients_sock, sock_addres))


        # отправка сообщения от клиента2 для клиента1
        if len(clients) > 1 and sock_addres == clients[0][1]:
            client1_sock, _ = clients[0] # распаковка кортежа с данными для первого клиента
            client1_sock.send(message.encode('utf8'))

        # отправка сообщения от клиента1 для клиента2
        if len(clients) > 1 and sock_addres == clients[1][1]:
            client2_sock, _ = clients[1] # распаковка кортежа с данными для второго клиента
            client2_sock.send(message.encode('utf8'))

# функция запуска сервера
def start_server():
    # привязка к сокету , нашего хоста и порта
    HOST, PORT = 'localhost', 12345
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((HOST, PORT))

    # прослушка подключений
    server_sock.listen(5) # до 5 клиентов
    print('Сервер запущен и ждет подключений...')

    # подключение клиентов
    while True:
        clients_sock, sock_addres = server_sock.accept()
        print(f'Подключен клиент с адрессом - {sock_addres}')
        client_thread = threading.Thread(target=send_message, args=(clients_sock, sock_addres)) # поток отправлений инфы клиентов в функцию
        client_thread.start()

start_server()




