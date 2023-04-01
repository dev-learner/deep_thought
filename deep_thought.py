import tkinter as tk
# import requests
# import json
import sys

class DeepThoughtApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Deep Thought")
        self.master.configure(bg="black")
        self.master.resizable(False, False)

        # Calculate the window size
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.5)

        # Calculate the window position
        x = int(screen_width/2 - window_width/2)
        y = int(screen_height/2 - window_height/2)
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create a frame to hold the buttons
        button_frame = tk.Frame(self.master, bg="black")
        button_frame.pack(side="bottom", fill="x", pady=10)

        # Create the OK button
        self.ok_button = tk.Button(
            button_frame,
            text="Ok",
            command=self.show_message,
            state="active"
        )
        self.ok_button.pack(side="right", padx=10)

        # Create the Cancel button
        self.cancel_button = tk.Button(
            button_frame,
            text="Cancel",
            command=self.cancel,
            state="active"
        )
        self.cancel_button.pack(side="right", padx=10)

    def cancel(self):
        # self.send_webhook("Cancel selected...")
        sys.exit()

    # def send_webhook(self, message):
    #     data = {'content': message}

    #     # Webhook:Tradingview (My Server)
    #     webhook_url1 = 'https://discord.com/api/webhooks/1083459595026051123/-H-MaBu73G3VKFAxknwuCVwjW8FplImLOGmtAeeeUQUCeI_pxUOUTg-2NP7cLgrj6fBQ'
    #     response = requests.post(
    #         webhook_url1, data=json.dumps(data),
    #         headers={'Content-Type': 'application/json'}
    #     )

    #     if response.status_code != 204:
    #         print("Webhook not sent successfully")

    def show_message(self):
        # Disable the buttons
        self.ok_button.config(state="disabled")
        self.cancel_button.config(state="disabled")

        # Create the message box
        message_box = tk.Label(
            self.master,
            text="Gotcha!\nThank you for your data...\n😉😘",
            font=("Arial", 24),
            fg="red",
            bg="black"
        )
        message_box.place(relx=0.5, rely=0.5, anchor="center")

        # self.send_webhook("Gotcha message seen...")

        # Schedule the message box to disappear after 5 seconds
        self.master.after(5000, self.master.destroy)

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    DeepThoughtApp(root)
    root.mainloop()
