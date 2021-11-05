import csv
import os

#print(dir(csv))

print("Hello")



def load_csv(filename,player_data):
    with open(filename) as csvdatei:
        csv_reader_object = csv.reader(csvdatei,delimiter=';')
        print(csv_reader_object)

        for row in csv_reader_object:
            #print(row[0],row[1])
            player_data[str(row[0])] = int(row[1])
    
def print_players(player_data):
    for d in player_data:
        print(d,player_data[d])

def save_player_data(filename,player_data):
    os.remove(filename)
    with open(filename,'a') as csv_file:
        for row in player_data:
            csv_file.write(row+";"+str(player_data[row])+"\n")
        

players = dict()

load_csv("data.csv",players)

save_player_data("data.csv",players)

print("____________")


print("____________")


  




