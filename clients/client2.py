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
from tkinter import scrolledtext

HOST = 'localhost'
PORT = 12345

client2_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2_sock.connect((HOST, PORT))
print(f'Присоеденился к серверу - [{HOST}]')

# tkinter часть
# окно
window = Tk()
window.title('Онлайн чат. Клиент 2')
window.geometry('400x600')

# ввод текста
text_input = Entry(window)
text_input.pack()

# отображение текста
text_display = scrolledtext.ScrolledText(window)
text_display.pack()

# функция отправки сообщения
def message_send_clicked():
    message_send = text_input.get()

    if message_send != '':
        client2_sock.sendall(message_send.encode('utf-8'))

# кнопка "отправить"
btn = Button(window, text='Отправить', command=message_send_clicked)
btn.pack()