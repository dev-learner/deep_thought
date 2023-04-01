import tkinter as tk
from playsound import playsound

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("My App")

        # Create the button
        self.button = tk.Button(
            self.master,
            text="Play Audio",
            command=self.play_audio
        )
        self.button.pack()

    def play_audio(self):
        # Play the audio clip
        playsound("stonedandmissedit.mp3")

if __name__ == "__main__":
    root = tk.Tk()
    MyApp(root)
    root.mainloop()
