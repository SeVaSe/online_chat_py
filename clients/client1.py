'''
НЕ СТИРАТЬ!!!!!!!!!!!!!!!!!!!!!!!!

эта рабочая зона твоя. На тебе изначально стоят задачи:

подключить двух клиентов к серваку, который Я сделаю
сделать так, один клиент писал на сервер и второй клиент писал на сервер
так же чтобы на тестовом уровне работало все в консоли
в дальнейшем МЫ ВМЕСТЕ БУДЕМ ДЕЛАТЬ ДЛЯ КЛИЕНТОВ ДИЗАЙН UI

Ниши общие данные будут такие:
HOST = 'localhost'
PORT = 12345'''


import socket
from tkinter import *
from tkinter import scrolledtext


# хост и порт
HOST = 'localhost'
PORT = 12345

# установление данных сокету
client1_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1_sock.connect((HOST, PORT))
print(f'Присоеденился к серверу - [{HOST}]')



### TKINTER часть
# окно
window = Tk()
window.title('Онлайн чат. Клиент1')
window.geometry('400x600')

# отображение текста
message_display = scrolledtext.ScrolledText(window)
message_display.pack()

# ввод текста
input_text = Entry(window)
input_text.pack()

# функция отправки соо
def send_message_click():
    message = input_text.get()

    if message != '':       #если сообщение не равно пустому символу
        client1_sock.sendall(message.encode('utf-8'))

# кнопка "отправить"
btn = Button(window, text='Отправить', command=send_message_click)
btn.pack()









flag = True

while flag:
    mes = client1_sock.recv(1024).decode('utf-8')
    print(f'Клиент2 - {mes}\n')
