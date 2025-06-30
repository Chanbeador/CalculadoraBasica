# EJERCICIO EQUIPO

# Se crean funciones
from FuncionesEquipo import agregar_equipo, mostrar_equipo

# Se inicia contador
con_arquero = 0;
con_defensa = 0;
con_medio = 0;
con_delant = 0;

# Se crea diccionario
equipo = {};

# Se empieza bucle While

while True:

    print("-"*50);
    print("         Sistema Equipo de Futbol");
    print("-"*50);
    print("1) Registrar jugadores");
    print("2) Buscar jugador por RUT");
    print("3) Mostrar estado nutricional");
    print("4) Listar equipo completo");
    print("5) Contar jugadores por posición: ");
    print("6) Salir")
    print("-"*50);

    try:
        menu = int(input("Ingrese una opción: "));
    except ValueError:
        print("La opción debe ser entre 1 a 6!");

    if (menu == 1):
        rut = int(input("Ingrese rut de jugador (sin digito verificador): "))
        if (rut in equipo):
            print("Jugador registrado!");
            continue;
        else:
            nombre = str(input("Ingrese el nombre del jugador: "));
            try:
                peso = float(input("Ingrese peso del jugador (Kg): "));
                if (peso <= 0):
                    raise ValueError;
            
                estatura = float(input("Ingrese estatura de jugador (Mt): "));
                if (estatura <= 0):
                    raise ValueError;
            except ValueError:
                print("Peso y altura de jugador deben ser valores numericos positivos!");
                continue;
            
            try:
                posicion = int(input("Ingrese posicion del jugador en el equipo:" \
                "\n 1) Arquero" \
                "\n 2) Defensa" \
                "\n 3) Medio Campo" \
                "\n 4) Delantero"));
            
                if (posicion not in [1,2,3,4]):
                    raise ValueError;
            except ValueError:
                print("La posición de jugador solo puede ser un valor numerico del 1 al 4!");
                continue;
            
            if (posicion == 1):
                posicion = "Arquero";
                con_arquero += 1;
            elif (posicion == 2):
                posicion = "Defensa";
                con_defensa += 1;
            elif (posicion == 3):
                posicion = "Medio Campo";
                con_medio += 1;
            elif (posicion == 4):
                posicion = "Delantero";
                con_delant += 1;
            agregar_equipo(equipo, rut, nombre, peso, estatura, posicion);
    elif (menu == 2):
        buscar = int(input("Ingrese RUT de jugador (sin digito verificador): "));
        if (buscar in equipo):
            print(equipo[rut]);
        else:
            print("Jugador no registrado!");
    elif (menu == 3):
        print("-"*50);
        print("   INDICE MASA CORPORAL ");
        print("-"*50);
        rut = int(input("Ingrese RUT de jugador: "));
        IMC = peso/(estatura**2);
        if (rut in equipo):
            if (IMC <= 25):
                print("IMC: Normal!");
                print("-"*50);
            elif (IMC > 25 and IMC <= 30):
                print("IMC: Sobrepeso!");
                print("-"*50);
            elif (IMC > 30):
                print("IMC: Obeso!");
                print("-"*50);
            else:
                print("Rut invalido!");
                print("-"*50);
        else:
            print("Jugador no registrado!");
    elif (menu == 4):
        mostrar_equipo(equipo);
    elif (menu == 5):
        print("-"*50);
        print("      POSICIONES EQUIPO");
        print("-"*50);
        print(f"Arqueros: {con_arquero}\nDefensa: {con_defensa}\nMedio Campo: {con_medio}\nDelantero: {con_delant}");
        print("-"*50);
            
    elif (menu == 6):
        print("Hasta luego!");
        break;
    else:
        print("Opcion invalida!");