import socket
c = socket.socket()
c.connect(('localhost', 9999))
while True:
    Brainfuck_code = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    code_bytes = Brainfuck_code.encode('utf-8')
    c.send(code_bytes)
    i = 1
    if i==1:
        break
c.close()
