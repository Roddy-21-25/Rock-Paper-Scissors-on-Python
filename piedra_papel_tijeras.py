import random
while True:
    user = input("A)-> piedra | B)-> Papel | C)-> tijeras | Escribe la letra: ")
    
    r = ["piedra", "papel", "tijeras"]
    letra_aleatorio = random.randint(0, 2)

# piedra
    if user.lower() == "a" and r[letra_aleatorio] == "piedra":
        print(f"tu elegiste piedra y la maquina {r[letra_aleatorio]}, entonces: Empate")

        again = input("quieres continuar jugando, si o no ")
        if again == "si":
            continue
        else:
            break

    elif user.lower() == "a" and r[letra_aleatorio] == "tijeras":
        print(f"tu elegiste piedra y la maquina {r[letra_aleatorio]}, entonces: Ganaste")

        again = input("quieres continuar jugando, si o no ")
        if again == "si":
            continue
        else:
            break
        
    elif user.lower() == "a" and r[letra_aleatorio] == "papel":
        print(f"tu elegiste piedra y la maquina {r[letra_aleatorio]}, entonces: Perdiste")
            
        again = input("quieres continuar jugando, si o no ")
        if again == "si":
            continue
        else:
            break

# papel
    elif user.lower() == "b" and r[letra_aleatorio] == "piedra":
        print(f"tu elegiste Papel y la maquina {r[letra_aleatorio]}, entonces: Ganaste")
            
        again = input("quieres continuar jugando, si o no ")
        if again == "si":
            continue
        else:
            break

    elif user.lower() == "b" and r[letra_aleatorio] == "tijeras":
        print(f"tu elegiste Papel y la maquina {r[letra_aleatorio]}, entonces: Perdiste")
            
        again = input("quieres continuar jugando, si o no ")
        if again == "si":
            continue
        else:
            break

    elif user.lower() == "b" and r[letra_aleatorio] == "papel":
        print(f"tu elegiste Papel y la maquina {r[letra_aleatorio]}, entonces: Empate")
            
        again = input("quieres continuar jugando, si o no ")
        if again == "si":
            continue
        else:
            break

# tijeras
    elif user.lower() == "c" and r[letra_aleatorio] == "piedra":
        print(f"tu elegiste Tijeras y la maquina {r[letra_aleatorio]}, entonces: Perdiste")
            
        again = input("quieres continuar jugando, si o no ")
        if again == "si":
            continue
        else:
            break

    elif user.lower() == "c" and r[letra_aleatorio] == "tijeras":
        print(f"tu elegiste Tijeras y la maquina {r[letra_aleatorio]}, entonces: Empate")
            
        again = input("quieres continuar jugando, si o no ")
        if again == "si":
            continue
        else:
            break

    elif user.lower() == "c" and r[letra_aleatorio] == "papel":
        print(f"tu elegiste Tijeras y la maquina {r[letra_aleatorio]}, entonces: Ganaste")
            
        again = input("quieres continuar jugando, si o no ")
        if again == "si":
            continue
        else:
            break
    else:
        print(f"has elegido {user} pero esto no es valido T-T, pero antes te pregunto: ")

        again = input("quieres continuar jugando, si o no ")
        if again == "si":
            continue
        else:
            break

