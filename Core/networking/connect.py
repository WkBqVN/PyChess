import socket
import threading

class Connector:
    def __init__(self):
        self.server_ip = "localhost"
        self.server_port = 8080
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Kiểm tra kết nối trước khi kết nối đến máy chủ
        if not self.check_connection():
            print("Unable to connect to the server.")
            self.sock.close()  # Đóng socket nếu không thể kết nối
            return
        print("Connected to the server.")

    def check_connection(self):
        """Kiểm tra kết nối đến máy chủ bằng cách gửi ping."""
        try:
            self.sock.connect((self.server_ip, self.server_port))                # Kết nối để gửi ping
            return True
        except (socket.error, ConnectionResetError) as e:
            # Nếu có lỗi kết nối, trả về False
            print(f"Connection error: {e}")
            return False

    def close_connection(self):
        self.sock.close()
    
    def send_match_data(self, match_data):
        """Gửi dữ liệu trận đấu đến máy chủ."""
        self.sock.sendall(match_data.encode('utf-8'))                           # Phải định dạng JSON

# threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

# while True:
#     # Gửi tin nhắn từ người dùng
#     message = input("Enter message: ")
#     if message.lower() == "exit":
#         print("Exiting chat.")
#         break
    # sock.sendall(message.encode('utf-8'))
