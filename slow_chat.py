import random
import tkinter as tk
from QandAsCB import QandAsCB
import time
import pyttsx3
import threading


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("{0}x{1}+{2}+{3}".format(
            int(self.master.winfo_screenwidth() * 0.5),
            int(self.master.winfo_screenheight() * 0.5),
            int(self.master.winfo_screenwidth() * 0.25),
            int(self.master.winfo_screenheight() * 0.25)
        ))
        self.pack()
        self.create_widgets()

        self.ai = QandAsCB('qandas.csv')

        # Create a pyttsx3 object
        self.engine = pyttsx3.init()

    def create_widgets(self):
        self.message_label = tk.Label(self, text="Enter your message:")
        self.message_label.pack()

        self.message_entry = tk.Entry(self)
        self.message_entry.pack(fill="x", padx=10, pady=10)

        self.response_text = tk.Text(self, height=10)
        self.response_text.pack(fill="both", expand=True, padx=10, pady=10)

        self.quit_button = tk.Button(self, text="Exit", command=self.master.destroy)
        self.quit_button.pack()

        # Bind the <Return> key to the send_message method
        self.message_entry.bind("<Return>", lambda event: self.send_message())

        # Set the width of the message entry widget to match the response text widget
        self.message_entry.config(width=self.response_text['width'])

        # Disable the response text widget
        self.response_text.configure(state="disabled")

        # Set focus to message entry box
        self.message_entry.focus()

    def send_message(self):
        message = self.message_entry.get()
        response = self.ai.respond(message)
        self.display_response(response)
        self.message_entry.delete(0, tk.END)
        self.message_entry.focus()


    def display_response(self, response):
        self.response_text.config(state="normal")
        self.response_text.delete("1.0", tk.END)
        if response is not None:
            spoken_time = len(response) / 10  # 10 characters per second
            threading.Thread(target=self.speak_response, args=(response,)).start()

            for char in response:
                self.response_text.insert(tk.END, char)
                self.response_text.update()
                time.sleep(random.uniform(0.09, 0.3))
        self.response_text.config(state="disabled")

    def speak_response(self, response):
        spoken_time = len(response) / 10  # 10 characters per second
        self.engine.say(response)
        self.engine.setProperty('rate', round(len(response) / spoken_time))
        self.engine.runAndWait()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
