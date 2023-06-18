import socket
from tkinter import *
from tkinter import scrolledtext
import threading

HOST = 'localhost'
PORT = 12348

client2_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2_sock.connect((HOST, PORT))
print(f'Присоеденился к серверу - [{HOST}]')


# tkinter часть
def open_chat_window(name):
    # окно чата
    window = Toplevel(window_name)
    window.title(f'Онлайн чат. Пользователь: {name}')
    window.geometry('400x600')

    # отображение текста
    text_display = scrolledtext.ScrolledText(window)
    text_display.pack()

    # ввод текста
    text_input = Entry(window)
    text_input.pack()

    # функция отправки сообщений
    def message_send_clicked():
        message_send = f'{name}: {text_input.get()}'
        text_display.insert(END, f'Я: {text_input.get()}\n')
        text_input.delete(0, END)  # стирание текста с текстового поля после отправки сообщения

        if message_send != '':
            client2_sock.sendall((message_send.encode('utf-8')))

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
    # поток
    msg_theard = threading.Thread(target=message_receiving)

    msg_theard.daemon = True
    msg_theard.start()


# окно для имени
window_name = Tk()
window_name.title('Как Вас зовут?')
window_name.geometry('300x100')

lbl = Label(window_name, text='Введите имя:')
lbl.pack()

# ввод текста
name_input = Entry(window_name)
name_input.pack()

# кнопка для отправки имени
btn_name = Button(window_name, text='Отправить', command=lambda: open_chat_window(name_input.get()))
btn_name.pack()

window_name.mainloop()
