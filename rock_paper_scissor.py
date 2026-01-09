""" 
This script implements a Rock-Paper-Scissors game where a player competes against the computer. 
The computer randomly selects its move, and the game determines the winner of each round based 
on the standard rules of Rock-Paper-Scissors. The game includes the following features:
1. Player Input: The player can input their choice (rock, paper, or scissor) or choose to quit the game.
2. Random Computer Choice: The computer randomly selects its move from the available options.
3. Winner Determination: The game determines the winner of each round based on the player's and computer's choices.
4. Score Tracking: The game keeps track of the number of wins, losses, and ties for the player.
5. Multiple Rounds: The player can play multiple rounds until they decide to exit the game.
6. Final Score Display: When the player quits, the game displays the final score summary.
This script is designed to be interactive and user-friendly, providing feedback after each round 
and maintaining a running score to enhance the gaming experience.
"""

import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    choices = ['rock', 'paper', 'scissor']
    return random.choice(choices)

def get_player_choice():
    while True:
        choice = input("\nEnter your choice (rock/paper/scissor or r/p/s) or 'quit' to exit: ").lower().strip()
        # Map short forms to full names
        if choice == 'r':
            choice = 'rock'
        elif choice == 'p':
            choice = 'paper'
        elif choice == 's':
            choice = 'scissor'
        if choice in ['rock', 'paper', 'scissor', 'quit']:
            return choice
        else:
            print("Invalid choice! Please choose rock, paper, or scissor.")

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        return "player"
    else:
        return "computer"

def display_result(player, computer, result):
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")
    
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def play_game():
    print("=" * 50)
    print("Welcome to Rock-Paper-Scissor Game!")
    print("=" * 50)
    
    wins = 0
    losses = 0
    ties = 0
    
    while True:
        player_choice = get_player_choice()
        
        if player_choice == 'quit':
            break
        
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        display_result(player_choice, computer_choice, result)
        
        # Update score
        if result == "player":
            wins += 1
        elif result == "computer":
            losses += 1
        else:
            ties += 1
        
        # Display current score
        print("\n" + "-" * 50)
        print(f"Current Score - Wins: {wins} | Losses: {losses} | Ties: {ties}")
        print("-" * 50)
    
    # Display final score
    print("\n" + "=" * 50)
    print("Game Over! Final Score:")
    print(f"Wins: {wins} | Losses: {losses} | Ties: {ties}")
    print("Thanks for playing!")
    print("=" * 50)

# GUI version using Tkinter
class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # Initialize scores
        self.wins = 0
        self.losses = 0
        self.ties = 0
        
        # Title
        title_label = tk.Label(root, text="🎮 Rock Paper Scissors 🎮", 
                               font=("Arial", 24, "bold"), 
                               bg="#2c3e50", fg="#ecf0f1")
        title_label.pack(pady=20)
        
        # Score frame
        score_frame = tk.Frame(root, bg="#34495e", relief=tk.RAISED, borderwidth=2)
        score_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.score_label = tk.Label(score_frame, 
                                     text=f"Wins: {self.wins}  |  Losses: {self.losses}  |  Ties: {self.ties}",
                                     font=("Arial", 14, "bold"), 
                                     bg="#34495e", fg="#ecf0f1", pady=10)
        self.score_label.pack()
        
        # Result display frame
        result_frame = tk.Frame(root, bg="#34495e", relief=tk.RAISED, borderwidth=2)
        result_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        self.player_choice_label = tk.Label(result_frame, 
                                            text="Your Choice: -", 
                                            font=("Arial", 16), 
                                            bg="#34495e", fg="#3498db")
        self.player_choice_label.pack(pady=10)
        
        self.computer_choice_label = tk.Label(result_frame, 
                                              text="Computer Choice: -", 
                                              font=("Arial", 16), 
                                              bg="#34495e", fg="#e74c3c")
        self.computer_choice_label.pack(pady=10)
        
        self.result_label = tk.Label(result_frame, 
                                     text="Make your choice!", 
                                     font=("Arial", 18, "bold"), 
                                     bg="#34495e", fg="#f39c12", 
                                     wraplength=400)
        self.result_label.pack(pady=20)
        
        # Buttons frame
        buttons_frame = tk.Frame(root, bg="#2c3e50")
        buttons_frame.pack(pady=20)
        
        # Choice buttons
        button_style = {
            "font": ("Arial", 14, "bold"),
            "width": 12,
            "height": 2,
            "relief": tk.RAISED,
            "borderwidth": 3,
            "cursor": "hand2"
        }
        
        rock_btn = tk.Button(buttons_frame, text="🪨 ROCK", 
                            command=lambda: self.play_round("rock"),
                            bg="#3498db", fg="white", 
                            activebackground="#2980b9", **button_style)
        rock_btn.grid(row=0, column=0, padx=5, pady=5)
        
        paper_btn = tk.Button(buttons_frame, text="📄 PAPER", 
                             command=lambda: self.play_round("paper"),
                             bg="#2ecc71", fg="white", 
                             activebackground="#27ae60", **button_style)
        paper_btn.grid(row=0, column=1, padx=5, pady=5)
        
        scissor_btn = tk.Button(buttons_frame, text="✂️ SCISSOR", 
                               command=lambda: self.play_round("scissor"),
                               bg="#e74c3c", fg="white", 
                               activebackground="#c0392b", **button_style)
        scissor_btn.grid(row=0, column=2, padx=5, pady=5)
        
        # Control buttons
        control_frame = tk.Frame(root, bg="#2c3e50")
        control_frame.pack(pady=10)
        
        reset_btn = tk.Button(control_frame, text="🔄 Reset Score", 
                             command=self.reset_score,
                             font=("Arial", 12, "bold"),
                             bg="#95a5a6", fg="white",
                             activebackground="#7f8c8d",
                             width=15, height=1,
                             cursor="hand2")
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        quit_btn = tk.Button(control_frame, text="❌ Quit Game", 
                            command=self.quit_game,
                            font=("Arial", 12, "bold"),
                            bg="#e67e22", fg="white",
                            activebackground="#d35400",
                            width=15, height=1,
                            cursor="hand2")
        quit_btn.pack(side=tk.LEFT, padx=5)
    
    def play_round(self, player_choice):
        # Get computer choice
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(player_choice, computer_choice)
        
        # Update scores
        if result == "player":
            self.wins += 1
            result_text = "🎉 You Win! 🎉"
            result_color = "#27ae60"
        elif result == "computer":
            self.losses += 1
            result_text = "😞 Computer Wins!"
            result_color = "#e74c3c"
        else:
            self.ties += 1
            result_text = "🤝 It's a Tie!"
            result_color = "#f39c12"
        
        # Update display
        self.player_choice_label.config(text=f"Your Choice: {player_choice.upper()}")
        self.computer_choice_label.config(text=f"Computer Choice: {computer_choice.upper()}")
        self.result_label.config(text=result_text, fg=result_color)
        self.score_label.config(text=f"Wins: {self.wins}  |  Losses: {self.losses}  |  Ties: {self.ties}")
    
    def reset_score(self):
        if messagebox.askyesno("Reset Score", "Are you sure you want to reset the score?"):
            self.wins = 0
            self.losses = 0
            self.ties = 0
            self.score_label.config(text=f"Wins: {self.wins}  |  Losses: {self.losses}  |  Ties: {self.ties}")
            self.player_choice_label.config(text="Your Choice: -")
            self.computer_choice_label.config(text="Computer Choice: -")
            self.result_label.config(text="Make your choice!", fg="#f39c12")
    
    def quit_game(self):
        if messagebox.askyesno("Quit Game", 
                              f"Final Score:\nWins: {self.wins}\nLosses: {self.losses}\nTies: {self.ties}\n\nDo you want to quit?"):
            self.root.quit()

def start_gui():
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()

if __name__ == "__main__":
    # Comment out the console version and run GUI version
    # play_game()
    start_gui()