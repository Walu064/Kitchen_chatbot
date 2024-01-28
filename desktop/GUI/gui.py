import requests
import tkinter as tk
from tkinter import scrolledtext
import tkinter.font as tkFont

import spacy

nlp = spacy.load('pl_core_news_sm') 

def extract_food_name(message):
    doc = nlp(message)
    for token in doc:
        if token.pos_ == 'NOUN':
            return token.text
    return None

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

        food_name = extract_food_name(user_message)
        if food_name:
            try:
                response = requests.get(f"http://localhost:8000/recipes/{food_name}")
                if response.status_code == 200:
                    recipe_details = response.json()
                    
                    # Formatowanie listy składników
                    ingredients = recipe_details['ingredients'].split(', ')
                    formatted_ingredients = "\n".join(ingredients)

                    # Formatowanie kroków przygotowania
                    preparation_steps = recipe_details['content'].split('. ')
                    formatted_steps = ". ".join(preparation_steps)+"\n"

                    bot_response = f"Kitcher: Znalazłem przepis na {food_name}.\n\nLista składników:\n{formatted_ingredients}\n\nKroki przygotowania:\n{formatted_steps}"
                else:
                    bot_response = "Kitcher: Przepis nie znaleziony"
            except Exception as e:
                bot_response = f"Kitcher: Wystąpił problem podczas wyszukiwania przepisu: {e}"
        else:
            bot_response = "Kitcher: Nie mogę znaleźć nazwy potrawy w Twoim zapytaniu"

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
