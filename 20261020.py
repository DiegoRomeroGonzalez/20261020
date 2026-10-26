Name = input("What is your name? ")
print("Every imput must be in spanish")
Country = input(f"Hello, {Name}. If you could live in any country, which one would it be? ")

CURRENT_YEAR = 2026
CURRENT_MONTH = 10
CURRENT_DAY = 20

if Country == "Israel":
    print("Wow! That is a great option, Nethanyahu would be proud. When should we book our flights to Tel Aviv?")
    Meses_validos = {
        "enero": 1,
         "febrero": 2, 
         "marzo": 3,
         "abril": 4,
         "mayo": 5, 
         "junio": 6,
        "julio": 7, 
        "agosto": 8, 
        "septiembre": 9, 
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12,
    }
    Mes_viaje = input("In which month would you like to book our flight to go kiss the wall? ").strip().lower()

    while Mes_viaje not in Meses_validos:
        raise ValueError("Invalid month, enter a real month.")
    else:
        print(f"Your flight has been already booked for the 13th of {Mes_viaje}")

    Año_nacimiento = int(input("I want to know more about you, what year were you born? "))
    while  Año_nacimiento >2026:
        raise ValueError("Invalid year, enter a real date ")
    if Año_nacimiento <= 2026 and Año_nacimiento >= 2010:
        print("Go to sleep, Epstein is looking for you")
    elif Año_nacimiento >= 2000 and Año_nacimiento < 2010:
        print("You are in the best part of your life. Nethanya will personally educate you, you will learn how to have a lot of money and throw bombs. It had been promised to us 3000 years ago!")
    elif Año_nacimiento < 2000:
        print("You are already a grown adult, your place in our masons club is already there")

    Mes_Nacimiento = input("In which month were you born? ")

    if Mes_Nacimiento not in Meses_validos:
        raise ValueError("Invalid month, enter a real month.")
    else:
        print("I like that month")

    Dia_nacimiento = int(input("In which day of the month were you born? "))
    print("Perfect! I am going to calculate your exact age.")
    #formula para edad
    
    if CURRENT_MONTH > Mes_Nacimiento:
        Edad = int(CURRENT_YEAR - Año_nacimiento - 1)
    else:
        Edad = int(CURRENT_YEAR - Año_nacimiento)

    if CURRENT_DAY > Dia_nacimiento:
        Mes_Edad = (12 - Mes_Nacimiento + 1)
    else:
        Mes_Edad = (12 - Mes_Nacimiento)
        



else:
    print("Be careful with the pigeons! They are going to chase you, and you will be followed for the next months for security reasons")

