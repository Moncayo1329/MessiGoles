import random 
import json 
import webbrowser 

with open("data.json") as data:
    goles = json.load(data)


print("Bievenido a la app de goles del goat 🐐")
print(f"Tenemos disponibles {len(goles)} goles del goat")
respuesta = input("Quieres sacar un gol del goat?( si/no): ")


if respuesta.lower() == "si": 
   print("Perfecto, vamos a sacar un gol del goat!")
   while True: 
       gol_elegido = random.choice(goles)
       print(f"Tu gol elegido de hoy:{gol_elegido['rival']} - {gol_elegido['competición']} - {gol_elegido['año']}")
       respuesta2 = input("Presiona Enter para otro gol o escribe salir para terminar: ").lower()
       if respuesta2 == "salir":
          print("Hasta la proxima amigo del goat!")
          break
   webbrowser.open(gol_elegido["link"])
else: 
       print("Vuelve cuando quieras sacar un gol del goat!")
  

   
