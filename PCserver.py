import time
import socketserver
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Button, Controller as MouseController

mouse = MouseController()
keyboard = KeyboardController()

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            # Receive the message from the Raspberry Pi
            self.data = self.request.recv(1024).strip()
            if not self.data:
                break
            print(f"{self.client_address[0]} wrote: {self.data}")
            
            # Simulate a mouse click down
            elif self.data == b'left_click_down':
                mouse.press(Button.left)

            # Simulate a mouse click up
            elif self.data == b'left_click_up':
                mouse.release(Button.left)

            # Simulate a right mouse click down
            elif self.data == b'right_click_down':
                mouse.press(Button.right)

            # Simulate a right mouse click up
            elif self.data == b'right_click_up':
                mouse.release(Button.right)
            
            # Simulate ALT + TAB with basic implementation
            elif self.data == b'alt_tab_down':
                keyboard.press(Key.alt)
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
            
            # Simulate ALT + TAB with basic implementation
            elif self.data == b'alt_tab_up':
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
                keyboard.release(Key.alt)

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 12345

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()