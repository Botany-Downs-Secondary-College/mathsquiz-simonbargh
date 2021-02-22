from tkinter import *
from tkinter import ttk

import random
import time

class Welcome:
    def __init__(self, parent):      
        
        def Questions():
            
            # Checking whether the user's entry details meet the requirements
            
            '''def show_questions():
            
                try:
                    if self.NameEntry.get() == "":
                        self.EntryErrorLabel.configure(text = "Enter your name.")
                        self.NameEntry.focus()
                
                except ValueError:
                    self.EntryErrorLabel.configure(text = "Enter your age as a number.")
                    self.AgeEntry.delete(0, END)
                    self.AgeEntry.focus()'''
                    
            
            if len(self.NameEntry.get()) >= 1:
                if len(self.AgeEntry.get()) >= 1: # and self.AgeEntry.get() is not int:
                    if clicked.get() == "Easy" or clicked.get() == "Medium" or clicked.get() == "Hard":
                        frames = Quiz(root)
                        self.Welcome.grid_forget()
                    else:
                        self.EntryErrorLabel.configure(text = "Choose a difficulty level.")
                else:
                    self.EntryErrorLabel.configure(text = "Enter your age.")
            else:
                self.EntryErrorLabel.configure(text = "Enter your name.")
        
        # Welcome Frame
        self.Welcome = Frame(parent)
        self.Welcome.grid(row = 0, column = 0)
        self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz!", bg = "lightblue", fg = "blue", width = 24, padx = 30, pady = 10, font = ("Time", "12", "italic", "bold"))       
        
        self.TitleLabel.grid(columnspan = 2)
        
        self.NextButton = ttk.Button(self.Welcome, text = "Next", command = Questions)
        self.NextButton.grid(row = 5, column = 1, pady = 10)      
        
        # Name Label
        
        self.NameLabel = Label(self.Welcome, text = "Name", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", "12", "bold"))
        self.NameLabel.grid(row = 2, column = 0)
        
        # Age Label
        
        self.AgeLabel = Label(self.Welcome, text = "Age", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", "12", "bold"))
        self.AgeLabel.grid(row = 3, column = 0)
        
        # Name Entry
        
        self.NameEntry = ttk.Entry(self.Welcome, width = 20)
        self.NameEntry.grid(row = 2, column = 1, columnspan = 2)
        
        # Age Entry
        
        self.AgeEntry = ttk.Entry(self.Welcome, width = 20)
        self.AgeEntry.grid(row = 3, column = 1, columnspan = 2)
        
        # Difficulty Level
        
        self.DifficultyLabel = Label(self.Welcome, text = "Difficulty Level", anchor = W, fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", "12", "bold"))
        self.DifficultyLabel.grid(row = 4, column = 0)
        
        # Difficulty Options     
        
        options = ["Easy", "Medium", "Hard"]
        
        clicked = StringVar()
        
        clicked.set("Select an Option")
        
        diff_level = OptionMenu(self.Welcome, clicked, *options)
        diff_level.grid(row = 4, column = 1)  
        
        # Warning Error Label
        
        self.EntryErrorLabel = Label(self.Welcome, text = "", fg = "red", width = 10, padx = 50, pady = 10)
        self.EntryErrorLabel.grid(row = 6, column = 0, columnspan = 2)

class Quiz:
    def __init__(self, parent):
        
        def Welcome_Page():
            frames = Welcome(root) 
            self.Quiz.grid_forget()
        
        # Quiz Frame
        self.Quiz = Frame(parent)
        self.Quiz.grid(row = 0, column = 0)
        self.TitleLabel = Label(self.Quiz, text = "Questions", bg = "lightblue", fg = "black", width = 20, padx = 30, pady = 10) 
        
        self.TitleLabel.grid(columnspan = 2)
        
        self.BackButton = ttk.Button(self.Quiz, text = "Back", command = Welcome_Page)
        self.BackButton.grid(row = 8, column = 1, pady = 10)           

if __name__ == "__main__":
    root = Tk()
    frames = Welcome(root)
    root.title("Quiz")
    root.mainloop()



