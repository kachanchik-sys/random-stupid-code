import tkinter 
import re

class Clipboard():
    def __init__(self) -> None:
        self.tk = tkinter.Tk()

    def get_image(self)-> bytes:
        string = self.tk.clipboard_get(type='image/png')
        string = re.sub('0[xX](?=[0-9a-fA-F]{2})', '', string)
        string = string.replace("0x", "0")
        return bytes.fromhex(string)

    def get_text(self)-> str:
        return self.tk.clipboard_get()

    def set_image(self, image: bytes)->None:
        self.tk.clipboard_append(image, type='image/png')

    def set_text(self, text: str)->None:
        self.tk.clipboard_append(text)
    
    def clear(self):
        self.tk.clipboard_clear()


