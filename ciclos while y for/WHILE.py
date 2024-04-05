while(True):
    print("Personas - 1")
    print("Vehiculos - 2")
    print("Universidades - 3")
    print("Notas - 4")
    print("Salir - 5")

 
    opcion = int(input("elija una de las opciones de la lista anterior: "))
  
    if opcion== 1:
     print( "Elegiste: personas")
        
    elif opcion == 2:
       print("Elegiste: vehiculos")
    
    elif opcion == 3:
        print( "Elegiste: universidades")
            
    elif opcion == 4:
       print( "Elegiste: notas")

    elif opcion == 5:
        print("ciclo terminado")
        break
    else: 
        print("Opcion incorrecta")
       
       
  