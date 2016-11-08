import usocket as socket
import time
import temp
import network

# Response sent to web-client
CONTENT = b"""\
HTTP/1.0 200 OK

I have been alive for {} s.

The temperature is {}.{} C.

Best regards,
WiPy
"""

def answer_request(client_socket, client_addr):
    """Answer request with temperature measurement"""
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
    # Block to make sure all data is written before closing socket.
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
    s.listen(0)

    # Do not block to allow main loop to proceed
    # while waiting for request.
    s.setblocking(False)

    while True:
        """Main loop"""
        client_socket, client_addr = None, None
        try: # Will fail if allready accepted socket
            client_socket, client_addr = s.accept()
        except:
            pass

        if client_socket:
            try: # Improve stability
                answer_request(client_socket, client_addr)
            except:
                try:
                    # Closing socket will fail if
                    # socket is allready closed.
                    client_socket.close_socket()
                except:
                    pass
        time.sleep_ms(10)

main()
