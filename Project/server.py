import socket 

s = socket.socket()
print('Socket Created')
s.bind(('localhost',9999))
s.listen()
print('Waiting for connection')

while True:
    c,addr = s.accept()
    print('Connected with', addr)
    Brainfuck_code = c.recv(1024).decode()
    print(Brainfuck_code)
    i = 1
    if i==1:
        break
c.close()

