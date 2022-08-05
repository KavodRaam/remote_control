import socket
import global_remote_control_GARY0 as grc

IP = 'Put IP here'
PORT = 4455
ADDRES = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def connect():
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRES)
    server.listen()
    print("[LISTENING] Server is listening.")
    while True:
        print('listening on' + str(ADDRES))
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        data = conn.recv(SIZE)
        if data == b'exit':
            conn.close
            print(f"[DISCONNECTED] {addr} disconnected.")
            grc.read_response([0,0])
            exit()
        elif data == b'right':
            grc.read_response([1,0])
        print(f"[RECV] Receiving the file data.")
        print(data)


if __name__ == '__main__':
    connect()

