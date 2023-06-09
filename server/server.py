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







def start_server():
    # привязка к сокету , нашего хоста и порта
    HOST, PORT = 'localhost', 12345
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((HOST, PORT))

    # прослушка подключений
    server_sock.listen(5) # до 5 клиентов
    print('Сервер запущен и ждет подключений...')





