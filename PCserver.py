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
            if self.data == b'left_click_down':
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

            # Simulate ENTER
            elif self.data == b'enter_down':
                keyboard.press(Key.enter)

            # Simulate ENTER
            elif self.data == b'enter_up':
                keyboard.release(Key.enter)
                
            # Simulate CTRL + C
            elif self.data == b'ctrl_c_down':
                keyboard.press(Key.ctrl)
                keyboard.press('c')

            # Simulate CTRL + C
            elif self.data == b'ctrl_c_up':
                keyboard.release('c')
                keyboard.release(Key.ctrl)

            # Simulate CTRL + V
            elif self.data == b'ctrl_v_down':
                keyboard.press(Key.ctrl)
                keyboard.press('v')

            # Simulate CTRL + V
            elif self.data == b'ctrl_v_up':
                keyboard.release('v')
                keyboard.release(Key.ctrl)

            # Simulate ALT + TAB with advanced implementation
            elif self.data == b'alt_tab+_down':
                keyboard.press(Key.alt)
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
            
            # Simulate ALT + TAB with advanced implementation
            elif self.data == b'alt_tab+_up':
                keyboard.release(Key.alt)

            # Simulate a left arrow key for use with ALT + TAB with advanced implementation
            elif self.data == b'left_arrow':
                keyboard.press(Key.left)
                keyboard.release(Key.left)
                time.sleep(0.75)

            # Simulate a right arrow key for use with ALT + TAB with advanced implementation
            elif self.data == b'right_arrow':
                keyboard.press(Key.right)
                keyboard.release(Key.right)
                time.sleep(0.75)

            # Simulate CTRL + X
            elif self.data == b'ctrl_x_down':
                keyboard.press(Key.ctrl)
                keyboard.press('x')

            # Simulate CTRL + X
            elif self.data == b'ctrl_x_up':
                keyboard.release('x')
                keyboard.release(Key.ctrl)

            # Simulate CTRL + S
            elif self.data == b'ctrl_s_down':
                keyboard.press(Key.ctrl)
                keyboard.press('s')

            # Simulate CTRL + S
            elif self.data == b'ctrl_s_up':
                keyboard.release('s')
                keyboard.release(Key.ctrl)

            # Simulate CTRL + Z
            elif self.data == b'ctrl_z_down':
                keyboard.press(Key.ctrl)
                keyboard.press('z')

            # Simulate CTRL + Z
            elif self.data == b'ctrl_z_up':
                keyboard.release('z')
                keyboard.release(Key.ctrl)

            # Simulate CTRL + Y
            elif self.data == b'ctrl_y_down':
                keyboard.press(Key.ctrl)
                keyboard.press('y')

            # Simulate CTRL + Y
            elif self.data == b'ctrl_y_up':
                keyboard.release('y')
                keyboard.release(Key.ctrl)

            # Simulate ESC
            elif self.data == b'esc_down':
                keyboard.press(Key.esc)
                

            # Simulate ESC
            elif self.data == b'esc_up':
                keyboard.release(Key.esc)



if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 12345

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()