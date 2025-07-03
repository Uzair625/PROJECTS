This is a Tkinter-based word guessing game (like Hangman). The player tries to guess a random fruit name by entering one letter at a time. They have limited chances.

💡 Key Features
Randomly picks a fruit from a list.

Shows blanks for unguessed letters.

Updates display after each guess.

Tracks guessed letters and remaining chances.

Shows win/lose messages with a restart option.

🧱 Main Components
reset_game(): Picks a new word, resets game state.

update_display(): Updates the word display, guessed letters, and chances left.

check_guess(): Validates and checks the player's input letter.

check_game_over(): Ends the game if the word is guessed or chances run out.

disable_game_input(): Locks input when game ends.

Tkinter Widgets: Labels, Entry box, Buttons for interaction.

