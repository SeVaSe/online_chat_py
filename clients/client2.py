'''
НЕ СТИРАТЬ!!!!!!!!!!!!!!!!!!!!!!!!

эта рабочая зона твоя. На тебе изначально стоят задачи:

подключить двух клиентов к серваку, который Я сделаю
сделать так, один клиент писал на сервер и второй клиент писал на сервер
так же чтобы на тестовом уровне работало все в консоли
в дальнейшем МЫ ВМЕСТЕ БУДЕМ ДЕЛАТЬ ДЛЯ КЛИЕНТОВ ДИЗАЙН UI

Наши общие данные будут такие:
HOST = 'localhost'
PORT = 12345'''


import socket

HOST = 'localhost'
PORT = 12345

client2_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2_sock.connect((HOST, PORT))
print(f'Присоеденился к серверу - {HOST}')


flag = True

while flag:
    message = input('Введите сообщение')       #вводим сообщение

    if message != '':       #если сообщение не равно пустому символу
        client2_sock.sendall((message.encode('utf-8')))