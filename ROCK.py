import random


def play():
    user=input("What is your choice'r' for rock,'p' for paper,'s'for scissors")
    computer= random.choice(['r','p','s'])
    print(computer)

    if user==computer:
        return "tie"

    if is_win(user, computer):
        return "youwon"

    return "you lost"

def is_win(player, opponent):

    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='r' and opponent=='r'):
        return True
play()