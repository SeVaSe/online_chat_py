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
from tkinter import *

HOST = 'localhost'
PORT = 12345

client2_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2_sock.connect((HOST, PORT))
print(f'Присоеденился к серверу - [{HOST}]')

flag = True

while flag:
    message = input('Введите сообщение: ')  # вводим сообщение

    if message != '':  # если сообщение не равно пустому символу
        client2_sock.sendall(message.encode('utf-8'))

    mes = client2_sock.recv(1024).decode('utf-8')
    print(f'Клиент1 - {mes}\n')

# tkinter часть
# окно
window = Tk()
window.title('Онлайн чат. Клиент 2')
window.geometry('400x600')

