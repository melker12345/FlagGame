import os
import random
import tkinter as tk
from PIL import Image, ImageTk

# Define the directory where the flag images are stored
FLAG_DIR = r'C:\Users\Melker-Desktop\Desktop\Python\FlagGame\flag_img_folder'

class FlagGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Flag Game")
        self.master.geometry("500x500")
        
        # Load all flag image filenames into a list
        self.flag_files = [f for f in os.listdir(FLAG_DIR) if f.endswith(".png")]
        
        # Create the UI elements
        self.canvas = tk.Canvas(self.master, width=400, height=300, background='#333')
        self.canvas.pack(pady=20)
        
        self.button_labels = []
        for i in range(4):
            button = tk.Button(self.master, text="", command=lambda x=i: self.check_answer(x))
            button.pack(fill="x", padx=20, pady=5)
            self.button_labels.append(button)
            
        self.score_label = tk.Label(self.master, text="Score: 0")
        self.score_label.pack(pady=10)
        
        # Start the game
        self.score = 0
        self.next_question()
        
    def next_question(self):
        # Randomly select a flag image filename and corresponding country name
        flag_file = random.choice(self.flag_files)
        self.correct_country = flag_file[:-4]

        # Load the flag image and display it on the canvas
        self.flag_image = Image.open(os.path.join(FLAG_DIR, flag_file))
        self.flag_image = self.flag_image.resize((400, 300), Image.ANTIALIAS)
        self.flag_image = ImageTk.PhotoImage(self.flag_image)
        self.canvas.create_image(0, 0, image=self.flag_image, anchor="nw")
        
        # Randomly select four country names for the buttons
        country_names = [self.correct_country]
        while len(country_names) < 4:
            country_name = random.choice([f[:-4] for f in self.flag_files])
            if country_name not in country_names:
                country_names.append(country_name)
        random.shuffle(country_names)
        
        # Set the button labels to the country names
        for i, label in enumerate(self.button_labels):
            label.configure(text=country_names[i])

    def check_answer(self, button_index):
        # Check if the user clicked the correct button
        if self.button_labels[button_index].cget("text") == self.correct_country:
            self.score += 1
            self.score_label.configure(text=f"Score: {self.score}")
            print("True")
        else:
            print("Wrong")
        self.next_question()
            
        
if __name__ == "__main__":
    root = tk.Tk()
    app = FlagGameGUI(root)
    root.mainloop()
