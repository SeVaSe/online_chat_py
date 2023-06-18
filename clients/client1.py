import socket
import tkinter
from tkinter import *
from tkinter import scrolledtext
import threading


# хост и порт
HOST = 'localhost'
PORT = 12348

# установление данных сокету
client1_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1_sock.connect((HOST, PORT))
print(f'Присоеденился к серверу - [{HOST}]')



### TKINTER часть окна чата
def open_chat_window(name_client):
    # окно
    window_chat = tkinter.Toplevel(window_name)
    window_chat.title(f'Онлайн чат. Пользователь: {name_client}')
    window_chat.geometry('400x600')

    # отображение текста
    message_display = scrolledtext.ScrolledText(window_chat)
    message_display.pack()

    # ввод текста
    input_text = Entry(window_chat)
    input_text.pack()

    # функция отправки соо
    def send_message_click():
        message = f'{name_client}: {input_text.get()}' # сохранение в переменную, наше соо
        message_display.insert(END, f'Я: {input_text.get()}\n') # вывод на собственном окне
        input_text.delete(0, END)


        if message != '':       #если сообщение не равно пустому символу
            client1_sock.sendall(message.encode('utf-8'))


    # кнопка "отправить"
    btn = Button(window_chat, text='Отправить', command=send_message_click)
    btn.pack()



    # функция получения сообщений
    def out_message():
        while True:
            # обновление интерфейса
            window_chat.update()

            # получение и вывод сообщений
            try:
                mes = client1_sock.recv(1024).decode('utf-8')

                if mes:
                    message_display.insert(END, f'{mes}\n')
            except socket.error as e:
                print(f'Ошибка: {e}')
                break

    # поток для получения беспрерывных соо
    mes_theard = threading.Thread(target=out_message)

    '''как я понял, что этот поток будет автоматически остановлен, когда основной 
    поток программы (в данном случае window.mainloop()) завершится. Это позволяет корректно завершать 
    программу при закрытии окна.'''

    mes_theard.daemon = True
    mes_theard.start() # запуск потока




# создание основного окна
window_name = tkinter.Tk()
window_name.title('Знакомство')
window_name.geometry('300x100')

# label
lb = tkinter.Label(window_name,text='Введите свое имя:')
lb.pack()

# ввод текста
input_name_cl = Entry(window_name)
input_name_cl.pack()

# кнопка отправки имени
btn_name = tkinter.Button(window_name, text='Подтвердить имя', command=lambda: open_chat_window(input_name_cl.get())) # отправка аргумента в котором хранится имя клиента
btn_name.pack()

window_name.mainloop()

