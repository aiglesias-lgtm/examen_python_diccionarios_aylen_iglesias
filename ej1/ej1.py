# PERDON POR LA TARDANZA AL PUBLICAR MI REPOSITORIO, ME DABA VARIOS ERRORES Y ME COSTO ARREGLARLO
# EN LA CLASE QUE VIENE DESEO DEFENDER MI CODIGO Y REHACER EL EXAMEN (obvio si se pude sin problema)

tienda = {
    "terror": ["jason","chuckie"],
    "accion":  ["avengers","iron man"],
    "ciencia ficcion": ["robocop","terminator"]
}

biblioteca = {}
id_juego = 1

while True:
    print ("n\  MENU  ")
    print ("__________")
    print ("1.Tienda")
    print ("2. Jugar juego")
    print ("3. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        while True:
            print ("  TIENDA  ")
            print ("1.Comprar jugeo")
            print ("2.Jugar juego")
            print ("3.Salir")

            opcion_tienda = input("Ingrese una opcion: ")

            if opcion_tienda == "1":
                print ("GENEROS: ")
                for key in tienda:
                    print ("- " + key)

                    genero_elegido = input ("Ingrese un genero: ")

            if opcion_tienda == "2":
                genero = input("genero: ")
                titulo = input ("titulo: ")

                if genero in tienda:
                    tienda [genero].append(titulo)
                else:
                    tienda[genero] = [titulo]
                print ("Juego agregado")
            if opcion_tienda == "3":
                break

    if opcion == "2":
      print( " BIBLIOTECA ")

      if len(biblioteca) == 0:
             print ("No hay juegos en la biblioteca")
      else:
                for id_juego in biblioteca:
                    print (f"{id_juego}. {biblioteca[id_juego]}")
                id_elegido = int(input("Ingresar el id del juego: "))
                
                if id_elegido in biblioteca:
                    juego = biblioteca[id_juego]
                    input (f"Jugando a {juego}")
                else:
                    print ("ID no encontrado")
    if opcion == "3":
       print ("Saliendo...")
       break