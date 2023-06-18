import socket
import threading
import os


clients = []

# функция для принятия сообщений от клиентов и дальнейшая их переотправка
def send_message(clients_sock, sock_addres):
    while True:
        message = clients_sock.recv(1024).decode('utf-8')

        # # проверяем, есть ли совпадение адрессов в клиентах. Если нет, то мы добавляем нового клиента в список
        # if sock_addres not in [i[1] for i in clients]:
        #     clients.append((clients_sock, sock_addres))

        # проверка на то, какой это клиент и вывод на консоль контроля, от кого пришло сообщение
        if len(clients) > 1 and sock_addres == clients[0][1]: # клиент1
            print(f'[Клиент 1] -{message}')
        if len(clients) > 1 and sock_addres == clients[1][1]: # клиент2:
            print(f'[Клиент 2] -{message}')

        # отправка сообщения клиентам
        for client_conn, client_addr in clients:
            if client_addr != sock_addres:
                client_conn.sendall(message.encode('utf-8'))


# функция запуска сервера
def start_server():
    # привязка к сокету , нашего хоста и порта
    HOST, PORT = 'localhost', 12348
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((HOST, PORT))

    # прослушка подключений
    server_sock.listen(5) # до 5 клиентов
    print('Сервер запущен и ждет подключений...')


    # подключение клиентов
    while True:
        clients_sock, sock_addres = server_sock.accept()
        print(f'Подключен клиент с адрессом - {sock_addres}')

        new_client = True

        client_thread = threading.Thread(target=send_message, args=(clients_sock, sock_addres)) # поток отправлений инфы клиентов в функцию
        client_thread.start()

        if new_client:
            clients.append((clients_sock, sock_addres))
            new_client = False

start_server()




