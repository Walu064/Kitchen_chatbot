import tkinter as tk
from tkinter import scrolledtext
import tkinter.font as tkFont

class KitcherChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kitcher Chatbot")
        
        self.root.configure(bg="#333333")
        self.text_color = "#FFFFFF"
        self.bg_color = "#333333"
        self.entry_bg_color = "#555555"
        self.entry_fg_color = "#FFFFFF"
        
        self.root.resizable(False, False)

        font = tkFont.Font(family="Arial", size=12)

        self.conversation_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg=self.bg_color, fg=self.text_color, font=font)
        self.conversation_box.place(x=20, y=20, width=460, height=360)
        self.conversation_box.configure(state='disabled')

        self.entry_message = tk.Entry(root, bg=self.entry_bg_color, fg=self.entry_fg_color, font=font)
        self.entry_message.place(x=20, y=400, width=360, height=50)
        self.entry_message.focus()

        self.send_button = tk.Button(root, text="Send", bg="#0078D7", fg=self.text_color, command=self.send_message)
        self.send_button.place(x=390, y=400, width=90, height=50)

    def send_message(self):
        user_message = self.entry_message.get()
        self.update_conversation("Ty: " + user_message)
        self.entry_message.delete(0, tk.END)

        bot_response = "Kitcher: Odpowiedź na '" + user_message + "'"
        self.update_conversation(bot_response)

    def update_conversation(self, message):
        self.conversation_box.configure(state='normal')
        self.conversation_box.insert(tk.END, message + "\n")
        self.conversation_box.configure(state='disabled')
        self.conversation_box.see(tk.END)

def run_app():
    root = tk.Tk()
    app = KitcherChatApp(root)
    root.geometry("500x470")
    root.mainloop()
