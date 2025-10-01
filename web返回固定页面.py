import socket

if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    tcp_server_socket.bind(("", 8080))
    tcp_server_socket.listen(128)

    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        rev_data = new_socket.recv(4096)
        print(rev_data)

        with open('E:/PythonProject/web方向/index.html', 'r',encoding='utf-8') as f:
            file_data = f.read()

            # 将数据封装成http形式
            # 响应行
            # 响应头
            # 空行
            # 响应体
        response_line = 'HTTP/1.1 200 OK\r\n'
        response_header = 'Server:Apache\r\n'
        response_body = file_data
        response = response_line + response_header + "\r\n" + response_body
        response_data = response.encode('utf-8')

        new_socket.send(response_data)
