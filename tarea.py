####El laberinto encantado✨✨✨
#Nivel 1
print("Bienvenido al laberinto encantado")
print("Estas al borde de un laberinto y ya comienza a oscurecerse")
print("Ves dos caminos uno de tierra y muchas hojas y otro de piedra")
decision_1 = input("\nCual tomas? TIERRA o PIEDRA").lower()
if decision_1 == "tierra":
    print("\nEl camino de tierra te a llevado a un lindo paraiso muy bien")
elif  decision_1 == "piedra":
    print("\nEl camino de piedra te a llevado a un gran hoyo te has caido y has perdido. Fin del juego😔!")
else:
    print("Opcion no valida. Intentalo de nuevo")

    #Nivel 2
    print("Sigues caminando y ves un portal, que haces ignoras el portal o entras al portal")
    decision_2 = input("\nQue haras? IGNORAS o SIGUES").lower()
    if decision_2 == "ignoras":
        print("\nMuy bien puedes seguir con tu camino")
    elif    decision_2  == "entras":
       print("Al entar al portal te a llevado al calabozo. Has perdido. Fin del juego😩!")
    else:
        print("opcion no valida")

        #Nivel 3
        print("Sigues caminando y ves dos caminos mas.")
        print("El de la izquierda parece normal y el de la derecha es tenebroso se escuchan ruidos algunos pasos como si algo o alguien ya estuviera ahi")
        decision_3 = input("\nCual escoges? la IZQUIERDA o la DERECHA").lower()
        if decision_3 == "izquierda":
          print("Muy bien te has encontrado con una hada quien te dara una pista")
          print("La hada ha dicho que sigas adelante y ignores cualquier ruido")
        elif decision_3 == "derecha":
            print("te has topado con un leon muy hambriento. has perdido. Fin del juego!")
        else:
            print("opcion no valida. Intenta de nuevo")

            #Nivel 4
            print("hasta ahora vas muy bien.👌🏽👌🏽")
            print("sigues caminando y te topas con dos rutas mas")
            print("Ahora que haras, que camino te parece mejor? El de la izquierda es muy oscuro y el de la dereccha tiene buena luz pero muchas ramas")
            decision_4 = input("\nCual escoges el de la IZQUIERDA o el de la DERECHA?").lower()
            if decision_4 == "izquierda":
                print("Al caminar por unos minutos te encuentras con una lampara y siges con tu camino traquilamente. Te has salvado👌🏽")
            elif decision_4 == "derecha":    
                print("Al comenzar a caminar te has tropesado y caido por una de las ramas y te has enredado. Has perdido. Fin del juego😔!")
            else:
                print("Opcion no valida") 

                #Nivel 5
                print("Wow ya estas muy cerca")
                print("sigues caminando y te topas con dos caminos mas")
                print("El camino de la izquierda parece un cuento de hadas tiene un cielo azul pajaros y un arcoiris y el camino de la derecha tiene buena luz varios arboles")
                decision_5 = input("\nPor cual iras? IZQUIERDA o DERECHA?").lower()
                if decision_5 == "izquierda":
                    print("Al caminar te das cuenta que todo era una ilusion y te esperaba un monstruo gigante. Has perdido. Fin del juego😶!")
                elif decision_5 == "derecha":
                    print("Al caminar te das cuenta que los arboles tenian manzanas y comes algunas ya que no habias logrado encontrar nada que fuera comestible🍎") 
                else:
                    print("opcion no valida")

                    #Nivel 6
                    print("sigues caminando y ves dos rutas mas")
                    print("En el camino de la izquierda esta un bote y mucha agua y el camino de la derecha esta nevando")
                    decision_6 = input("Por cual iras? IZQUIERDA o DERECHA?").lower()
                    if decision_6 == "izquierda":
                        print("Comienzas a remar y te das cuenta que las corrientes son muy fuertes intentas regresar pero ya es muy tarde. Has perdido. Fin del juego")
                    elif decision_6 == "derecha":
                        print("Vas caminando y el frio es demasido fuerte pero despues de unos segundos de encuentras con abrigo lo tomas y logras salir. GANASTE🤩!")
                        print("\nFIN DEL JUEGO")   

                        