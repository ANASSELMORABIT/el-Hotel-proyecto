"""
Programa de reserva de un hotel
Versión: 0.1
Author: A.Guardiola
"""
import json #Del módulo json sólo se utilizará la función dumps(), que sirve para imprimir de
            # manera amigable los diccionarios ("pretty printing") 

# SECCIÓN 1: INICIALIZACIÓN DE VARIABLES GLOBALES ###########################################

# Declaramos la variable hotel
hotel = [[{},{},{},{},{}],      # piso 1: 5 habitaciones sin inicializar
         [{},{},{},{},{}],      # piso 2: 5 habitaciones sin inicializar
         [{},{},{},{},{}],      # piso 3: 5 habitaciones sin inicializar
         [{},{},{},{},{}]]      # piso 4: 5 habitaciones sin inicializar

# Inicializamos las distintas habitaciones del hotel
    # (Esta sección podría estar incluida en una función inicializarHotel)
for piso, habitaciones in enumerate(hotel):                 # iteramos pisos   
    for numHab, habitacion in enumerate(habitaciones):      # iteramos habitaciones
        habitacion["numero"] = (piso+1)*10 + (numHab+1)     # inicializamos cada habitación
        habitacion["ocupada"] = False
        habitacion["fechaIngreso"] = ""
        habitacion["numNoches"] = 0
        if numHab + 1 == 1:
            habitacion["clase"] = "suite"
        else:
            habitacion["clase"] = "normal"
        habitacion["precio"] =0.0

# SECCIÓN 2: DECLARACIÓN DE FUNCIONES ######################################################

# Función 'hacerReserva' para rellenar una habitación con una reserva
def hacerReserva(piso,hab,fechaIngreso,numNoches):
    habitacion = hotel[piso-1][hab-1]
    habitacion["ocupada"] = True
    habitacion["fechaIngreso"] = fechaIngreso
    habitacion["numNoches"] = numNoches
    if hab == 1:
        habitacion["precio"] = habitacion["numNoches"] * 100
    else:
        habitacion["precio"] = habitacion["numNoches"] * 50
    return None

# Función 'consultarReserva' que muestra por pantalla los datos de la reserva si la habitación
    # está ocupada o el mensaje "Habitación sin reserva" en caso contrario
def consultarReserva(numHab):
    for piso,habitaciones in enumerate(hotel):
        for num,habitacion in enumerate(habitaciones):
            if habitacion["numero"] == numHab:
                if habitacion ["ocupada"]:
                    print("Habitación ocupada")
                else:
                    print("Habitación sin reserva")
                return habitacion        
    return None        

# Función 'anularReserva' para eliminar la reserva de una habitación
    # La habitación debe devolverse a su estado inicial
def anularReserva(numHab):
    for piso,habitaciones in enumerate(hotel):
        for num,habitacion in enumerate(habitaciones):
            habitacion["numero"] =numHab     # inicializamos la  habitación
            habitacion["ocupada"] = False
            habitacion["fechaIngreso"] = ""
            habitacion["numNoches"] = 0
            if numHab + 1 == 1:
                habitacion["clase"] = "suite"
            else:
                habitacion["clase"] = "normal"
            habitacion["precio"] =0.0
            return habitacion
    return None

# Función 'modificarReserva' para modificar la reserva de una habitación
    # La función sólo debe dejar modificar las claves "fechaIngreso" y "numNoches"
    # La función debe recalcular el precio de la reserva
def modificarReserva(clave ,valorNuevo,numHab):
    for piso,habitaciones in enumerate(hotel):
        for num,habitacion in enumerate(habitaciones):
            if habitacion["numero"] == numHab:
                habitacion[clave] = valorNuevo
                if habitacion["clase"] == "suite":
                    habitacion["precio"] = habitacion["numNoches"] * 100
                else:
                    habitacion["precio"] = habitacion["numNoches"] * 50
                return habitacion
    return None

#Función 'listarOcupadas' que devuelve la lista de habitaciones ocupadas (habsLibres)
def listarOcupadas():
    habsLibres = []
    for piso,habitaciones in enumerate(hotel):
        for num,habitacion in enumerate(habitaciones):
            if not habitacion["ocupada"]:
                habsLibres.append(habitacion["numero"])
    return habsLibres

#Función 'estaLibre' que devuelve False si la habitación está ocupada y True si está libre
def estaLibre(numHab):
    for piso,habitaciones in enumerate(hotel):
        for num,habitacion in enumerate(habitaciones):
            if habitacion["numero"] == numHab:
                return  habitacion["ocupada"]     
    return None

# SECCIÓN 3: PROGRAMA PRINCIPAL ###########################################################

print(json.dumps(hotel, indent=4))        # Mostramos estado inicial del hotel
hacerReserva(3,1,"20221117",4)              # Hacemos tres reservas 
hacerReserva(1,3,"20221123",5)
hacerReserva(4,2,"20221201",1)
print(json.dumps(hotel, indent=4))        # Mostramos estado del hotel
for X,Y in consultarReserva(45).items():  # Consultamos la reserva de la habitación 45
    print(f"{X}: {Y}")
for X,Y in anularReserva(42).items():
    print(f"{X}: {Y}")                    # Anulamos la reserva de la habitación 42
modificarReserva("numNoches",2,42)        # Modificamos la reserva de la habitación 42
print(json.dumps(hotel, indent=4))        # Mostramos estado del hotel
print(listarOcupadas())                   # Listamos las habitaciones no ocupadas
print(estaLibre(42))                       # Comprobamos si la habitación 42 está libre

# CÓDIGO AQUÍ (para ir probando las funciones declaradas en la SECCIÓN 2)
