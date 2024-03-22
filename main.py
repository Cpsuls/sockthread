import time
import threading

lock = threading.Lock()
value = 0


def incrs():
    global value
    while True:
        with lock:
            value += 1
            print(value)
            time.sleep(0.01)



thr = threading.Thread(target=incrs)
thr.start()


# import socket
# import threading
# from tqdm import tqdm
#
# host = input("Введите имя хоста/IP-адрес: ") or '127.0.0.1'
# open_ports = []
#
#
# def scan_port(port):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.settimeout(1)
#
#     try:
#         s.connect((host, port))
#         open_ports.append(port)
#         print(f"Порт {port} открыт")
#     except:
#         pass
#     finally:
#         s.close()
#
#
# threads = []
# ports = range(1, 10000)
#
# for port in ports:
#     thread = threading.Thread(target=scan_port, args=(port,))
#     threads.append(thread)
#     thread.start()
#
# for thread in tqdm(threads, desc="Сканирование портов", unit="порт"):
#     thread.join()
#
# print("Список открытых портов:")
# print(sorted(open_ports))
