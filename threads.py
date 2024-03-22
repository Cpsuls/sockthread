import threading
import socket
import time

global client_socket, addr
client_socket = None
addr = "localhost"

def listen_to_port():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)

    while True:
        global client_socket, addr
        client_socket, addr = server_socket.accept()
        print(f"Подключение от {addr}")
        with open("logs.txt", "a") as file:
            file.write(f"Подключение от {addr}\n")
        with open("ids.txt", "a") as file:
            file.write(f"{client_socket} - {addr}\n")

def handle_commands():
    with open("logs.txt", "a") as file:
        file.write(f"Подключение от {addr}\n")
    with open("ids.txt", "a") as file:
        file.write(f"{addr}")
    while True:
        command = input("Введите команду: ")
        with open("logs.txt", "a") as file:
            file.write("Введите команду: ")
        if command == "exit":
            print("Завершение программы")
            with open("logs.txt", "a") as file:
                file.write("Завершение программы")
            break
        elif command == "pause":
            print("Остановка прослушивания порта")
            with open("logs.txt", "a") as file:
                file.write("Остановка прослушивания порта")
            time.sleep(10)
        elif command == "show_logs":
            print("Показ логов")
            with open("logs.txt", "r") as file:
                print(file.read())
        elif command == "clear_logs":
            print("Очистка логов")
            with open("logs.txt", "w") as file:
                file.write("")
            print("Логи очищены")
        elif command == "clear_id_file":
            print("Очистка файла идентификации")
            with open("ids.txt", "w") as file:
                file.write("")
            print("Файл идентификации очищен")
        else:
            print("Неизвестная команда")

listen_thread = threading.Thread(target=listen_to_port)
listen_thread.start()

command_thread = threading.Thread(target=handle_commands)
command_thread.start()