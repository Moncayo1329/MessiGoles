import random 
import json


data = open("data.json")
goles = json.load(data) 



gol_elegido = random.choice(goles)



while True: 
    gol_elegido = random.choice(goles)
    print(f"Tu gol elegido de hoy:{gol_elegido['rival']} - {gol_elegido['competición']} - {gol_elegido['año']} - {gol_elegido['link']}")
    input("Presiona para sacar otro gol del goat")
