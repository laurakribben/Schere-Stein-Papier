import csv
import os
from random import randint


opt = ["schere","stein","papier"]


def setup():
    welcome = """
    Schere Stein Papier

    Anleitung:

    Schere gewinnt gegen Papier;
    Papier gewinnt gegen Stein;
    Stein gewinnt gegen Schere.

    Bei gleichen Zügen wird der Zug wiederholt.

    Wenn du gewinnst bekommst du 1 Punkt.
    Wenn der Bot gewinnt verlierst du 0.5 Punkte.

    Viel Erfolg!
    """
    print(welcome)

def load_csv(filename,player_data):

    if os.path.isfile(filename):
        with open(filename) as csvdatei:
            csv_reader_object = csv.reader(csvdatei,delimiter=';')
            #print(csv_reader_object)

            for row in csv_reader_object:
                #print(row[0],row[1])
                player_data[str(row[0])] = int(row[1])

    open(filename, "w")
    
def print_players(player_data):
    for d in player_data:
        print(d,player_data[d])

def save_player_data(filename,player_data):
    os.remove(filename)
    with open(filename,'a') as csv_file:
        for row in player_data:
            csv_file.write(row+";"+str(player_data[row])+"\n")


def play_round():

    print("Wähle:",opt)
    t_bot = opt[randint(0, 2)]
    t_player = input("Spieler: ")

    print("Bot: "+t_bot)
    result = 0

    if t_player not in opt:
        print("Eingabe ungültig, bitte wiederholen...")
        return play_round()

    if t_bot != t_player :

        if t_bot == 'schere' and t_player == 'stein':
            result += 1
            print("gewonnen")
        
        elif t_bot == 'stein' and t_player == 'papier':
            result += 1
            print("gewonnen")

        elif t_bot == 'papier' and t_player == 'schere':
            result += 1
            print("gewonnen")
        else:
            result -= 0.5
            print("verloren")
    else:
        print("unentschieden")
        return play_round()

    return result



def start_game(filename,player_data):
    setup()

    load_csv(filename,player_data)

    

    flag_in = True
    while(flag_in):
        print("Wie heißt du?")
        name = input()

        if name in player_data:
            print("Aktueller Punktestand:",player_data[name])
        else:
            print("Hallo", name)
            player_data[name] = 0

        print("Wie viele Runden möchtest du spielen?")
        num_rounds = int(input())
        r=0
        for i in range(num_rounds):
            r += play_round()

        
        player_data[name] += r
      
        print("Dein neuer Punktestand ist:",player_data[name])

        print("Nochmal spielen? ['j','n']")
        answer = input()
        if answer == "j":
            flag_in = True
        else:
            flag_in = False


    save_player_data(filename,player_data)

        
players = dict()
start_game("dat.csv",players)



