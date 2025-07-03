import random
import tkinter as tk
from tkinter import messagebox # For pop-up messages
from collections import Counter

# All the fruits name
someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')

class GuessTheWordGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Word Game")
        master.geometry("500x400") # Set initial window size
        master.resizable(False, False) # Make window not resizable

        self.word_list = someWords

        # --- Game State Variables (initialized here, reset in reset_game) ---
        self.word = ""
        self.word_letters = []
        self.guessed_letters = []
        self.revealed_count = 0
        self.chances = 0

        # --- GUI Elements ---

        # Title Label
        self.title_label = tk.Label(master, text="Guess the Word!", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        # Word Display Label
        self.word_display_var = tk.StringVar()
        self.word_display_label = tk.Label(master, textvariable=self.word_display_var, font=("Courier New", 24, "bold"), fg="blue")
        self.word_display_label.pack(pady=10)

        # Chances Left Label
        self.chances_var = tk.StringVar()
        self.chances_label = tk.Label(master, textvariable=self.chances_var, font=("Arial", 14))
        self.chances_label.pack(pady=5)

        # Message Label (for hints, already guessed, invalid input)
        self.message_var = tk.StringVar()
        self.message_label = tk.Label(master, textvariable=self.message_var, font=("Arial", 12), fg="red")
        self.message_label.pack(pady=5)

        # Guess Input Entry
        self.guess_entry_label = tk.Label(master, text="Enter your guess:", font=("Arial", 12))
        self.guess_entry_label.pack(pady=5)
        self.guess_entry = tk.Entry(master, width=10, font=("Arial", 14))
        self.guess_entry.pack(pady=5)
        self.guess_entry.bind("<Return>", self.check_guess_event) # Allows pressing Enter to guess

        # Guess Button
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess, font=("Arial", 14), bg="lightgreen")
        self.guess_button.pack(pady=10)

        # Guessed Letters Label
        self.guessed_letters_var = tk.StringVar()
        self.guessed_letters_label = tk.Label(master, textvariable=self.guessed_letters_var, font=("Arial", 12))
        self.guessed_letters_label.pack(pady=5)

        # New Game Button
        self.new_game_button = tk.Button(master, text="New Game", command=self.reset_game, font=("Arial", 14), bg="lightblue")
        self.new_game_button.pack(pady=10)

        # --- Initial setup - IMPORTANT: Call reset_game AFTER all widgets are created ---
        self.reset_game()

    def reset_game(self):
        """Resets all game variables and updates the display for a new game."""
        self.word = random.choice(self.word_list).lower()
        self.word_letters = list(self.word)
        self.guessed_letters = [] # Stores unique correctly/incorrectly guessed letters
        self.revealed_count = 0
        self.chances = len(self.word) + 3 # Adjust difficulty here

        # Clear input field and enable it
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state=tk.NORMAL)

        # Update all Tkinter StringVars
        self.update_display()
        self.message_var.set("") # Clear messages
        self.guess_button.config(state=tk.NORMAL) # Enable guess button

    def update_display(self):
        """Updates the word display, chances label, and guessed letters label."""
        display = ''
        current_revealed_count = 0
        for char in self.word_letters:
            if char in self.guessed_letters:
                display += char + ' '
                current_revealed_count += 1
            else:
                display += '_ '
        self.word_display_var.set(display.strip())
        self.chances_var.set(f"Chances left: {self.chances}")
        self.guessed_letters_var.set(f"Guessed Letters: {', '.join(sorted(self.guessed_letters))}")
        self.revealed_count = current_revealed_count # Update actual revealed count

    def check_guess_event(self, event):
        """Event handler for pressing Enter in the entry field."""
        self.check_guess()

    def check_guess(self):
        """Processes the user's guess."""
        guess = self.guess_entry.get().strip().lower()
        self.guess_entry.delete(0, tk.END) # Clear the entry field after getting input

        # --- Input Validation ---
        if not guess.isalpha():
            self.message_var.set("Invalid input. Please enter a letter.")
            return
        elif len(guess) != 1:
            self.message_var.set("Please enter only one letter at a time.")
            return
        elif guess in self.guessed_letters:
            self.message_var.set(f"You have already guessed '{guess}'. Try again.")
            return

        # Add the guess to the list of guessed letters
        self.guessed_letters.append(guess)
        self.message_var.set("") # Clear previous message if guess is valid

        # --- Game Logic ---
        if guess in self.word_letters:
            self.message_var.set(f"Good guess! '{guess}' is in the word.")
        else:
            self.message_var.set(f"Sorry, '{guess}' is not in the word.")
            self.chances -= 1

        self.update_display()
        self.check_game_over()

    def check_game_over(self):
        """Checks if the game has ended (win or lose)."""
        if self.revealed_count == len(self.word):
            self.message_var.set(f"Congratulations! You guessed the word: {self.word.upper()}")
            messagebox.showinfo("Game Over", f"You won! The word was: {self.word.upper()}")
            self.disable_game_input()
        elif self.chances <= 0:
            self.message_var.set(f"You ran out of chances! The word was: {self.word.upper()}")
            messagebox.showinfo("Game Over", f"You lost! The word was: {self.word.upper()}")
            self.disable_game_input()

    def disable_game_input(self):
        """Disables input and guess button when the game is over."""
        self.guess_entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)


# Create the main window
if __name__ == '__main__':
    root = tk.Tk()
    game = GuessTheWordGame(root)
    root.mainloop() # Start the Tkinter event loop