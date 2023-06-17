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
import threading

HOST = 'localhost'
PORT = 12347

client2_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2_sock.connect((HOST, PORT))
print(f'Присоеденился к серверу - [{HOST}]')

# tkinter часть
# окно для имени
window_name = Tk()
window_name.title('Как Вас зовут?')

lbl = Label(window_name, text='Введите имя:')
lbl.pack()

name_input = Entry(window_name)
name_input.pack()

def name_input_clicked():
    name = name_input.get()
    window_name.destroy()

btn_name = Button(window_name, text='Отправить', command=name_input_clicked)
btn_name.pack()


# окно
window = Tk()
window.title('Онлайн чат. Клиент 2')
window.geometry('400x600')

# отображение текста
text_display = scrolledtext.ScrolledText(window)
text_display.pack()

# ввод текста
text_input = Entry(window)
text_input.pack()


# функция отправки сообщений
def message_send_clicked():
    message_send = text_input.get()
    name = name_input.get()
    text_display.insert(END, f'{name}: {message_send}\n')
    text_input.delete(0, END)       #стирание текста с текстового поля после отправки сообщения

    if message_send != '':
        client2_sock.sendall((f'{name}: {message_send}').encode('utf-8'))


# кнопка "отправить"
btn = Button(window, text='Отправить', command=message_send_clicked)
btn.pack()


# функция получения сообщений
def message_receiving():
    while True:
        # обновление интерфейса
        window.update()

        # получение и вывод сообщений
        try:
            msg_rcv = client2_sock.recv(1024).decode('utf-8')

            if msg_rcv:
                text_display.insert(END, f'{msg_rcv}\n')
        except socket.error as e:
            print(f'Ошибка: {e}')
            break

msg_theard = threading.Thread(target=message_receiving)

msg_theard.daemon = True
msg_theard.start()

window.mainloop()