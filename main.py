import usocket as socket
import time
import temp
import network

CONTENT = b"""\
HTTP/1.0 200 OK

I have been alive for {} s.

The temperature is {}.{} C.

Best regards,
WiPy
"""
def answer_request(client_socket, client_addr):
    req = client_socket.readline()
    print("Request:")
    print(req)
    while True:
        h = client_socket.readline()
        if h == b"" or h == b"\r\n" or h == None:
            break
        print(h)
    temperature, temperature_decimal = temp.get_temp(10000,0)
    alive = time.time() - 473385595
    data = CONTENT.format(alive, temperature, temperature_decimal)
    client_socket.setblocking(True)
    client_socket.write(data)
    client_socket.setblocking(False)
    client_socket.close()

def main():
    s = socket.socket()
    ai = socket.getaddrinfo("0.0.0.0", 80)
    print("Bind address info:", ai)

    addr = ai[0][-1]
    s.bind(addr)

    s.listen(5)
    s.setblocking(False)
    print("Listening, connect your browser to http://<this_host>:80/")

    while True:
        client_socket, client_addr = None, None
        try:
            client_socket, client_addr = s.accept()
        except:
            pass
        if client_socket:
            try:
                answer_request(client_socket, client_addr)
            except:
                try:
                    client_socket.close_socket()
                except:
                    pass
        time.sleep_ms(10)

main()
