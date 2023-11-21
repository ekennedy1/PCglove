import socketserver
from pynput.keyboard import Controller
from pynput.mouse import Button, Controller as MouseController

keyboard = Controller()
mouse = MouseController()

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            # Receive the message from the Raspberry Pi
            self.data = self.request.recv(1024).strip()
            if not self.data:
                break
            print(f"{self.client_address[0]} wrote: {self.data}")
        
            # Simulate a keystroke
            if self.data == b'Hello, PC!':
                keyboard.type('Hello, Raspberry Pi!')
            
            # Simulate a mouse click
            elif self.data == b'left_click':
                mouse.click(Button.left)

            # Simulate a right mouse click
            elif self.data == b'right_click':
                mouse.click(Button.right)

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 12345

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()