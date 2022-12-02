import os

def ibw (genero,altura):

    if genero == "M":
        pesoIdeal = 56.2+1.41*(altura/2.54-60)
    elif genero == "F":
        pesoIdeal = 53.1+1.36 *(altura/2.54-60)

    os.system("clear")
    
    return (print("\nEl peso ideal para su estatura es : " + str(int(pesoIdeal)) + " kg\n"))

def calorias (tiempo,met,peso):

    #   VALORES DEL MET
    #     • Caminar = 2
    #     • Tenis = 5
    #     • Montar en bicicleta = 14
    #     • Correr = 6
    #     • Nadar = 9.8

    if(met == 1):
        valorMet = 2 #Caminar
        caloriasQuemadas = (tiempo * valorMet * peso ) /200
    elif(met == 2):
        valorMet = 5 #Tenis
        caloriasQuemadas = (tiempo * valorMet * peso ) /200
    elif(met == 3):
        valorMet = 14 #Tenis
        caloriasQuemadas = (tiempo * valorMet * peso ) /200
    elif(met == 4):
        valorMet = 14 #Correr
        caloriasQuemadas = (tiempo * valorMet * peso ) /200
    elif(met == 5):
        valorMet = 14 #Nadar
        caloriasQuemadas = (tiempo * valorMet * peso ) /200
    
    os.system("clear")
    
    return print("\nTotal de calorias quemadas : " + str(caloriasQuemadas) + "\n")

def grasaCorporal (peso,altura2,edad,genero):

    IMC = peso / altura2

    if edad >= 18:
        if genero == "M":
            porcentajeGrasaCoporal = 1.20 * IMC + 0.23 * edad - 16.2
         
        elif genero == "F":
            porcentajeGrasaCoporal = 1.20 * IMC + 0.23 * edad - 5.4

        os.system("clear")

        return print("\nSu procentaje de grasa corporal es : " + str(round(porcentajeGrasaCoporal)) + " % \n")

    else:

       os.system("clear")

       return print("\nTienes que ser mayor de edad para realizar el calculo")

    
def metabolicoBasal (peso,altura,edad,genero):

    if genero == "M":
      indiceBasal = 13.397*peso + 4.799*edad - 5.677*altura + 88.362
    if genero == "F":
      indiceBasal = 9.247*peso + 3.098*edad - 4.330*altura + 447.593

    os.system("clear")

    return print("\nSu índice metabólico basal es : " + str(indiceBasal) + "\n")

opcion = 0


while( opcion !=5 ):

    print("=====================================")
    print("LA CALCULADORA SALUDABLE")
    print("=====================================")
    print("1. Peso Ideal (IBW)")
    print("2. Calorías Quemadas")
    print("3. Porcentaje De Grasa Corporal")
    print("4. Índice Metabólico Basal")
    print("5. Salir")
    print("=====================================\n")

    opcion = int(input("Seleccione una opción : "))

    if opcion == 1:
        print("\n=====================================")
        print("       EL PESO IDEAL (IBW)           ")
        print("=====================================\n")
        
        genero = input(
            """Ingrese su genero 
M = Masculino  F = Femenino

> """
        ).upper()
        
        if genero == "F" or genero == "M":

            altura = int( input("\nIngrese su altura en cm : ") )

            ibw(genero,altura)
        else:
            os.system("clear")
            print("\nEl genero ingresado es incorrecto\n")

    elif opcion == 2:
        print("\n=====================================")
        print("         QUEMANDO CALORÍAS           ")
        print("=====================================")

        met = int(input("""\nIngrese la actividad realizada :

1. Caminar   
2. Tenis
3. Montar en bicicleta
4. Correr
5. Nadar

> """))

        tiempo = int( input("\nIngrese el tiempo de la duración de la actividad en minutos : ") )
        
        peso = int( input("\nIngrese su peso en Kg : ") )

        if met > 0 and met <=5:
            calorias (tiempo, met, peso)
        else:
            os.system("clear")
            print("\nLa actividad ingresada no es valida\n")

    elif opcion == 3:
        print("\n=====================================")
        print("   PORCENTAJE DE GRASA CORPORAL      ")
        print("=====================================")

        genero = input(
            """\nIngrese su genero 
M = Masculino  F = Femenino

> """
        ).upper()
        if genero == "F" or genero == "M":
    
            edad = int( input("\nIngrese su edad : ") )

            altura2 = float( input("\nIngrese su altura en metros : ") )

            peso = int( input("\nIngrese su peso en Kg : ") )

            grasaCorporal (peso,altura2,edad,genero)

        else:
            os.system("clear")
            print("\nEl genero ingresado es incorrecto\n")
    
    elif opcion == 4:

        print("\n=====================================")
        print("      ÍNDICE METABÓLICO BASAL        ")
        print("=====================================")

        genero = input(
            """\nIngrese su genero 
M = Masculino  F = Femenino

> """
        ).upper()

        if genero == "F" or genero == "M":
    
            edad = int( input("\nIngrese su edad : ") )

            altura = int( input("\nIngrese su altura en centimetros : ") )

            peso = int( input("\nIngrese su peso en Kg : ") )

            metabolicoBasal(peso,altura,edad,genero)
        else:
            os.system("clear")
            print("\nEl genero ingresado es incorrecto")

    elif opcion == 5:

        os.system("clear")
        print("\nSaliendo del programa...")

    else:

         os.system("clear")
         print("\nLa opción ingresada es invalida\n")

