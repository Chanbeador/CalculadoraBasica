def agregar_equipo(equipo, rut, nombre, peso, estatura, posicion):
    if (rut not in equipo):
        equipo[rut] = [nombre, peso, estatura, posicion];
        print(f"Jugador '{nombre}', añadido con exito!");
    else:
        print("-"*50);
        print("JUGADOR YA REGISTRADO!");
        print("-"*50);


def mostrar_equipo(equipo):
    if (len(equipo) == 0):
        print("No hay jugadores registrados!");
    else:
        for clave, valor in equipo.items():
            print(f"RUT: {clave} | Nombre: {valor[0]} | Peso: {valor[1]}(Kg) | Estatura: {valor[2]}(mt) | Posición : {valor[3]}");
