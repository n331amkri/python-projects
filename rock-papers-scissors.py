import random

def play():
    print("Welcome to Rock, Paper, Scissors!")
    user = input("Enter your choice (rock: 'r', paper: 'p', scissors: 's'): ").lower()

    computer = random.choice(['r','p','c'])
     
    if(user == computer):
        return "It's a tie!"
    
    else:
        return check_win(user, computer)
    

def check_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return "You win!"
    else:
        return "You lose!"
        
print(play())