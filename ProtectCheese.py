import Data as data
import random as rd 
import tkinter as tk
from PIL import Image, ImageTk


    
class ProtectCheese:
    def __init__(self, root):
        
        color0 = "#355C7D"
        color1 = "#725A7A"
        color2 = "#C56C86"
        color3 = "#FF7582"
        
        
        self.root = root
        self.root.title("Protect The Cheese")
        
        # image5 = Image.open("photos/5 Steps.png")
        # image5 = image5.resize((200, 200), Image.ANTIALIAS)
        
        # image4 = Image.open("photos/4 Steps.png")
        # image4 = image4.resize((200, 200), Image.ANTIALIAS)
        
        # image3 = Image.open("photos/3 Steps.png")
        # image3 = image3.resize((200, 200), Image.ANTIALIAS)
        
        # image2 = Image.open("photos/2 Steps.png")
        # image2 = image2.resize((200, 200), Image.ANTIALIAS)
        
        # image1 = Image.open("photos/1 Steps.png")
        # image1 = image1.resize((200, 200), Image.ANTIALIAS)
        
        # image0 = Image.open("photos/Game Over.png")
        # image0 = image0.resize((200, 200), Image.ANTIALIAS)
        
        self.steps = 5
        self.image = self.visual_stair()
        
        
        
        # Window 
        self.root.geometry(f'{300}x{650}')
        self.root.configure(bg = color0)
        
        # # PLace Holder 00
        self.frame00 = tk.Frame(root, bg = color0, width = 202, height = 10)
        self.frame00.pack()
        
        # # Label
        self.label = tk.Label(root, text = "PROTECT THE CHEESE", width = 28, height = 2)
        self.label.pack()
        
        # # PLace Holder 01
        self.frame01 = tk.Frame(root, bg = color0, width = 202, height = 20)
        self.frame01.pack()
        
        # # Hint Message
        self.hint_box_frame = tk.Frame(root, bg = "white", width = 202, height = 40)
        self.hint_box = tk.Text(self.hint_box_frame, width = 25, height = 2)
        self.hint_box_frame.pack()
        self.hint_box.pack()
        
        # # PLace Holder 02
        self.frame02 = tk.Frame(root, bg = color0, width = 202, height = 20)
        self.frame02.pack()
        
        # # Visual Box
        
        photo = ImageTk.PhotoImage(self.image)
        
        self.visual_box = tk.Label(root, image=photo, width=200, height=200)
        self.visual_box.image = photo
        self.visual_box.pack()
        

        # # PLace Holder 03
        self.frame03 = tk.Frame(root, bg = color0, width = 202, height = 20)
        self.frame03.pack()
        
        # # Progress Box
        self.progress_box = tk.Text(root, width = 25, height = 2)
        self.progress_box.pack()
        
        # # PLace Holder 04
        self.frame04 = tk.Frame(root, bg = color0, width = 202, height = 20)
        self.frame04.pack()
        
        # # Message Box
        self.message_box = tk.Text(root, width = 25, height = 2)
        self.message_box.pack()
        
        # # PLace Holder 05
        self.frame05 = tk.Frame(root, bg = color0, width = 202, height = 20)
        self.frame05.pack()
        
        # # Input Frame
        self.input_frame = tk.Frame(root, bg = color0, width = 202, height = 150)
        
        self.letter_input = tk.Entry(self.input_frame, text="LETTER INPUT")     
        self.letter_submit = tk.Button(self.input_frame, text="LETTER SUBMIT", command = self.letter_guess)
        
        self.word_input = tk.Entry(self.input_frame, text="WORD INPUT")
        self.word_submit = tk.Button(self.input_frame, text="WORD SUBMIT", command = self.word_guess)
        
        self.letter_input.grid(row=0, column=0, padx=5, pady=5)
        
        self.letter_submit.grid(row=0, column=1, padx=5, pady=5)
        
        self.word_input.grid(row=1, column=0, padx=5, pady=5)
        
        self.word_submit.grid(row=1, column=1, padx=5, pady=5)
        
        self.input_frame.pack()
        
        self.guesses = []
        
        self.target_word = self.get_word()

        self.get_hint(self.target_word)

        self.progress_update()
        
        self.visual_update()
        
        self.message_display('Welcome')
        
        self.game_restart_frame()
        
    
        
        
        
        
    # # Get Word Function
    def get_word(self):
        return (rd.choice(data.answer))
        
    def get_hint(self, word):
        hint = data.hint[word]
        self.hint_box.delete(1.0, tk.END)
        self.hint_box.insert(tk.END, hint)
        self.hint_box.configure(state = "disabled")
        
    def progress(self, word, guessed):
        correct_letters = ""
        for letter in word:
            if letter in guessed:
                correct_letters += letter
            else:
                correct_letters += "-"
        return correct_letters
        
    def progress_display(self, word):
        self.progress_box.delete(1.0, tk.END)
        self.progress_box.insert(tk.END, word)
    
    def message_display(self, string):
        self.message_box.delete(1.0, tk.END)
        self.message_box.insert(tk.END, string)
        
    def word_guess(self):
        guessed_word = self.word_input.get().upper()
        if guessed_word == self.target_word:
            self.message_display('Well Done Word Complete')
            current_guesses = self.guesses
            letter_difference = set(guessed_word) - set(current_guesses)
            self.guesses.extend(letter_difference)
        else:
            self.message_display('Try Again')
            self.steps -= 1
            self.message_display(f"Only {self.steps} Left")
            if self.steps == 0:
                self.message_display(f"GAME OVER")
                self.word_submit.configure(state = "disabled")
                self.letter_submit.configure(state = "disabled")
                self.game_restart_frame()
        self.progress_update()
        self.visual_update()
        
        # if guessed_letter in self.guesses:
        #     self.message_display('You already tried this letter')
        # else:
    def letter_guess(self):
        guessed_letter = self.letter_input.get().upper()
        
        if guessed_letter in self.guesses:
            self.message_display('You already tried this letter')
        else:
            self.guesses.append(guessed_letter)
            if len(guessed_letter) == 1 and guessed_letter.isalpha():
                if guessed_letter in self.target_word:
                    self.message_display('Correct')
                else:
                    self.steps -= 1
                    self.message_display(f"Only {self.steps} Left")
                    if self.steps == 0:
                        self.message_display(f"GAME OVER")
                        self.word_submit.configure(state = "disabled")
                        self.letter_submit.configure(state = "disabled")
                        self.game_restart_frame()
            else:
                self.message_display('Invalid')     
        self.progress_update()
        self.visual_update()
        
        
    def visual_stair(self):
        
        if self.steps == 5:
            image = Image.open("photos/5 Steps.png")
            image = image.resize((200,200), Image.ADAPTIVE)
        elif self.steps == 4:
            image = Image.open("photos/4 Steps.png")
            image = image.resize((200,200), Image.ADAPTIVE)
        elif self.steps == 3:
            image = Image.open("photos/3 Steps.png")
            image = image.resize((200,200), Image.ADAPTIVE)
        elif self.steps == 2:
            image = Image.open("photos/2 Steps.png")
            image = image.resize((200,200), Image.ADAPTIVE)
        elif self.steps == 1:
            image = Image.open("photos/1 Steps.png")
            image = image.resize((200,200), Image.ADAPTIVE)
        else:
            image = Image.open("photos/Game Over.png")
            image = image.resize((200,200), Image.ADAPTIVE)
            
        return image
        
        
    def progress_update(self):
        progress = self.progress(self.target_word, self.guesses)       
        if (progress == self.target_word):
            self.message_display('Well Done Word Complete')
            self.progress_display(progress)
        self.progress_display(progress)
        
    def visual_update(self):
        self.image = self.visual_stair()
        photo = ImageTk.PhotoImage(self.image)
        self.visual_box.configure(image=photo)
        self.visual_box.image = photo
        
    def game_restart_frame(self):
        if hasattr(self, 'restart') and self.restart is not None:
            self.restart.destroy()
        self.restart = tk.Button(root, text="Restart", command = self.game_restart)
        self.restart.pack()
        
    def game_restart(self):
        self.guesses.clear()
        self.target_word = self.get_word()
        self.word_submit.configure(state = "normal")
        self.letter_submit.configure(state = "normal")
        self.hint_box.configure(state = "normal")
        self.get_hint(self.target_word)
        self.steps = 5
        self.progress_update()  
        self.visual_update()
        self.message_display('Welcome Back')     
        

if __name__ == "__main__":
    root = tk.Tk()
    protect_cheese = ProtectCheese(root)
    root.mainloop()