alumno = []
notas = []
asignatura = []
opcion = 0
nombre =""
while opcion != 4:
    print(f" SISTEMA CALIFICACIONES\n 1. Ingreso nombre alumno \n 2. Ingreso Notas alumno \n 3. Mostrar promedio alumno \n 4. Salir")
    try:
        opcion = int(input("Ingrese su opcion "))
        match opcion:
            case 1:
                 notas = []
                 nombre = input("Ingrese nombre de Alumno ")
                 alumno.append(nombre)
                 asignatura.append(notas)
                 print(alumno)
                 print(asignatura)
            case 2:
                 conta_alum = 0
                 nombre = input("Ingrese nombre de Alumno ")
                 for i in range(len(alumno)):
                     if alumno[i] == nombre:
                            conta_alum = i
                 continua = "S"
                 notas = []
                 while continua == "S":
                       try:
                            nota = float(input("Ingrese la nota alumno "))
                            if nota >= 1 and nota <= 7:
                                 notas.append(nota)
                            else:
                                 print("nota Incorrecta, vuelva a ingresar nota ")      
                       except:
                            print("Valor incorrecto ")
                       continua = input("Desea ingresar mas notas (S/N)" )
                 print(notas)
                 asignatura[conta_alum] = notas
                 print(alumno)
                 print(asignatura)   
            case 3:
                 conta_alum = 0
                 nombre = input("Ingrese nombre de Alumno ")
                 for i in range(len(alumno)):
                     if alumno[i] == nombre:
                            conta_alum = i
                 suma_nota = 0
                 conta_nota = 0
                 for nota_suma in asignatura[conta_alum]:
                      suma_nota += nota_suma
                      conta_nota += 1
                 print(f" El promedio del alumno {alumno[conta_alum]}, es {round(suma_nota/ conta_nota,1)}")     
                 print(Suave)


            case 4:
                print("Salir del sistema ") 
    except:
        print("Opcion invalida")  
